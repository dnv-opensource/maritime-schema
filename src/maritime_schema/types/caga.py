# pyright: reportCallIssue=false
# pyright: reportIncompatibleVariableOverride=false
import logging
import os
from datetime import datetime, timedelta
from enum import Enum
from pathlib import Path
from typing import Any, Dict, List, Optional, Union
from uuid import UUID, uuid4

from pydantic import BaseModel, ConfigDict
from pydantic.fields import Field  # , FieldInfo

from maritime_schema.utils.strings import to_camel

__ALL__ = ["TrafficSituation", "OutputSchema", "publish_schema"]

logger = logging.getLogger(__name__)


class BaseModelConfig(BaseModel):
    """This BaseModelConfig class enables the alias_generator for all cases"""

    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)


class AISNavStatus(str, Enum):
    UNDER_WAY_USING_ENGINE = "Under way using engine"
    AT_ANCHOR = "At anchor"
    NOT_UNDER_COMMAND = "Not under command"
    RESTRICTED_MANOEUVERABILITY = "Restricted manoeuverability"
    CONSTRAINED_BY_HER_DRAUGHT = "Constrained by her draught"
    MOORED = "Moored"
    AGROUND = "Aground"
    ENGAGED_IN_FISHING = "Engaged in fishing"
    UNDER_WAY_SAILING = "Under way sailing"
    RESERVED_FOR_FUTURE_AMENDMENT_OF_NAVIGATIONAL_STATUS_FOR_HSC = (
        "Reserved for future amendment of navigational status for HSC"
    )
    RESERVED_FOR_FUTURE_AMENDMENT_OF_NAVIGATIONAL_STATUS_FOR_WIG = (
        "Reserved for future amendment of navigational status for WIG"
    )
    RESERVED_FOR_FUTURE_USE_1 = "Reserved for future use 1"
    RESERVED_FOR_FUTURE_USE_2 = "Reserved for future use 2"
    RESERVED_FOR_FUTURE_USE_3 = "Reserved for future use 3"
    AIS_SART_IS_ACTIVE = "AIS SART is active"
    NOT_DEFINED_DEFAULT = "Not defined (default)"


class GeneralShipType(str, Enum):
    WING_IN_GROUND = "Wing in ground"
    FISHING = "Fishing"
    TOWING = "Towing"
    DREDGING_OR_UNDERWATER_OPS = "Dredging or underwater ops"
    DIVING_OPS = "Diving ops"
    MILITARY_OPS = "Military ops"
    SAILING = "Sailing"
    PLEASURE_CRAFT = "Pleasure Craft"
    HIGH_SPEED_CRAFT = "High speed craft"
    PILOT_VESSEL = "Pilot Vessel"
    SEARCH_AND_RESCUE_VESSEL = "Search and Rescue vessel"
    TUG = "Tug"
    PORT_TENDER = "Port Tender"
    ANTI_POLLUTION = "Anti-pollution"
    LAW_ENFORCEMENT = "Law Enforcement"
    MEDICAL_TRANSPORT = "Medical Transport"
    NONCOMBATANT_SHIP = "Noncombatant ship"
    PASSENGER = "Passenger"
    CARGO = "Cargo"
    TANKER = "Tanker"
    OTHER_TYPE = "Other Type"


class InterpolationMethod(str, Enum):
    LINEAR = "linear"
    COSINE = "cosine"
    SMOOTHSTEP = "smoothstep"
    ACCELERATE = "accelerate"
    DECELERATE = "decelerate"
    ORDINAL = "ordinal"


class WaveSpectra(Enum):
    JONSWAP = "JONSWAP"
    PiersonMoskowitz = "Pierson-Moskowitz"
    Bretschneider = "Bretschneider"


class WeatherCondition(Enum):
    Clear = "Clear"
    Cloudy = "Cloudy"
    Foggy = "Foggy"
    Rainy = "Rainy"
    Snowy = "Snowy"


class PrecipitationType(Enum):
    None_ = "None"
    Rain = "Rain"
    Snow = "Snow"
    Sleet = "Sleet"
    Hail = "Hail"


class Environment(BaseModelConfig):
    air_temperature: float = Field(None, description="The air temperature in degrees Celsius", examples=[20.0])
    water_remperature: float = Field(None, description="The water temperature in degrees Celsius", examples=[15.0])
    precipitation: PrecipitationType = Field(
        None, description="The type of precipitation", examples=[PrecipitationType.Rain]
    )
    wind_speed: float = Field(None, description="The wind speed in m/s", examples=[10.0])
    wind_direction: float = Field(None, description="The wind direction in degrees", examples=[180.0])
    current_speed: float = Field(None, description="The current speed in m/s", examples=[1.0])
    current_direction: float = Field(None, description="The current direction in degrees", examples=[90.0])
    wave_spectrum: WaveSpectra = Field(None, description="The wave spectrum", examples=[WaveSpectra.JONSWAP])
    significant_wave_height: float = Field(None, description="The significant wave height in meters", examples=[3.0])
    wave_period: float = Field(None, description="The wave period in seconds", examples=[12.0])
    wave_direction: float = Field(None, description="The wave direction in degrees", examples=[270.0])
    visibility: float = Field(None, description="The visibility in nautical miles", examples=[5.0])
    conditions: WeatherCondition = Field(
        None, description="The overall weather conditions", examples=[WeatherCondition.Clear]
    )


environment = Environment(
    air_temperature=20.0,
    water_remperature=15.0,
    precipitation=PrecipitationType.Rain,
    wind_speed=10.0,
    wind_direction=180.0,
    current_speed=1.0,
    current_direction=90.0,
    wave_spectrum=WaveSpectra.JONSWAP,
    significant_wave_height=3.0,
    wave_period=12.0,
    wave_direction=270.0,
    visibility=5.0,
    conditions=WeatherCondition.Clear,
)


class Position(BaseModelConfig):
    latitude: float = Field(..., ge=-90, le=90, description="WGS-84 latitude", examples=[51.2131])
    longitude: float = Field(..., ge=-180, le=180, description="WGS-84 longitude", examples=[11.2131])


position_example = Position(latitude=57.2343, longitude=10.3432)


class ShipStatic(BaseModelConfig):
    """Static ship data that will not change during the scenario."""

    id: UUID = Field(..., description="Unique Identifier", examples=[uuid4()])
    length: float = Field(gt=0, description="Length of the ship in meters", examples=[230.0])
    width: float = Field(gt=0, description="Width of the ship in meters", examples=[30.0])
    height: Optional[float] = Field(10, gt=0, description="Height of the ship in meters", examples=[15.0])
    mmsi: Optional[int] = Field(
        None, ge=100000000, le=999999999, description="Maritime Mobile Service Identity (MMSI)", examples=[123456789]
    )
    imo: Optional[int] = Field(None, ge=1000000, le=9999999, description="IMO Number", examples=[1234567])
    name: Optional[str] = Field(None, description="Ship title", examples=["RMS Titanic"])
    ship_type: GeneralShipType = Field(description="General ship type, based on AIS")


ship_static_example = ShipStatic(
    id=uuid4(),
    length=230.0,
    width=30.0,
    height=15.0,
    mmsi=123456789,
    name="RMS Titanic",
    ship_type=GeneralShipType.FISHING,
)


class Initial(BaseModelConfig):
    position: Position = Field(
        ...,
        title="Longitude and Latitude Values",
        description="A geographical coordinate",
        examples=[Position(latitude=51.2123, longitude=11.2313)],
    )
    sog: float = Field(
        ...,
        ge=0,
        title="Initial ship speed over ground",
        description="Initial ship speed over ground in knots",
        examples=[10.0],
    )
    cog: float = Field(
        ...,
        ge=0,
        le=360,
        title="Initial ship course over ground",
        description="Initial ship course over ground in degrees",
        examples=[45.0],
    )
    heading: Optional[float] = Field(
        None, ge=0, le=360, title="Initial ship heading", description="Initial ship heading in degrees", examples=[45.2]
    )
    nav_status: AISNavStatus = Field(..., description="AIS Navigational Status")


initial_example = Initial(
    position=Position(latitude=51.2123, longitude=11.2313),
    sog=12.3,
    cog=284.2,
    heading=283.1,
    nav_status=AISNavStatus.UNDER_WAY_USING_ENGINE,
)


class DataPoint(BaseModelConfig):
    value: float = Field(..., description="the value of the data at the current timestep", examples=[12.3])
    m_before_leg_change: float = Field(
        ..., description="meters before the waypoint to start interpolating to the new value", examples=[10]
    )
    m_after_leg_change: float = Field(
        ..., description="meters after the waypoint to finish interpolating to the new value", examples=[10]
    )
    interp_method: Union[InterpolationMethod, str] = Field("linear", description="Method used for interpolation")


data_point_example1 = DataPoint(value=12.3, m_before_leg_change=100, m_after_leg_change=100, interp_method="linear")
data_point_example2 = DataPoint(value=200, m_before_leg_change=500, m_after_leg_change=500, interp_method="cosine")


class Data(BaseModelConfig):
    sog: DataPoint = Field(
        None,
        description="Speed data point",
        examples=[DataPoint(value=12.3, m_before_leg_change=100, m_after_leg_change=100, interp_method="linear")],
    )
    heading: DataPoint = Field(
        None,
        description="Heading data point",
        examples=[DataPoint(value=180, m_before_leg_change=100, m_after_leg_change=100, interp_method="linear")],
    )

    model_config = ConfigDict(
        json_schema_extra={
            "additionalProperties": {
                "type": "object",
                "properties": {
                    "value": {"type": "number"},
                    "mBeforeLegChange": {"type": "number"},
                    "mAfterLegChange": {"type": "number"},
                    "interpMethod": {"type": "string"},
                },
                "required": ["value", "mBeforeLegChange", "mAfterLegChange", "interpMethod"],
                "description": "The 'data' field can include additional properties. All additional properties should be DataPoint objects.",
            }
        },
    )


class Waypoint(BaseModelConfig):
    position: Position = Field(
        description="A geographical coordinate", examples=[Position(latitude=51.2123, longitude=11.2313)]
    )
    turn_radius: float = Field(0, description="Orthodrome turn radius as defined in RTZ format", examples=[200])
    data: Data = Field(None, description="A `Data` object that includes `speed`, `course`, and `heading` data points")


waypoint_example = Waypoint(
    position=position_example, turn_radius=500, data=Data(sog=data_point_example1, cog=data_point_example2)
)


class Ship(BaseModelConfig):
    static: Optional[ShipStatic] = Field(
        description="Static ship information which does not change during a scenario.", examples=[ship_static_example]
    )
    initial: Initial = Field(title="Initial own ship Initial", examples=[initial_example])
    waypoints: Optional[List[Waypoint]] = Field(
        None,
        description="An array of `Waypoint` objects. Each waypoint object must have a `position` property. <br /> If no turn radius is provided, it will be assumed to be `0`. <br /> Additional data can be added to each waypoint leg. This allows varying parameters on a per-leg basis, such as speed and heading, or navigational status ",
        examples=[waypoint_example],
    )


ship_example = Ship(static=ship_static_example, initial=initial_example, waypoints=[waypoint_example])


class OwnShip(Ship):
    pass


class TargetShip(Ship):
    pass


class TrafficSituation(BaseModelConfig):
    title: str = Field(description="The title of the traffic situation", examples=["overtaking_18"])
    description: str = Field(
        description="A description of the traffic situation",
        examples=["Crossing situation with 3 target vessels in the Oslofjord"],
    )
    start_time: Optional[datetime] = Field(
        None,
        title="Situation starting time",
        description="Starting time of the situation in `ISO 8601` format `YYYY-MM-DDThh:mm:ssZ`",
        examples=[datetime.now()],
    )
    own_ship: OwnShip = Field(title="Own Ship data", description="Own Ship data", examples=[ship_example])
    target_ships: List[TargetShip] = Field(
        None, title="Target Ship data", description="Target Ship data", examples=[[ship_example]]
    )
    environment: Optional[Environment] = Field(None, description="environmental parameters", examples=[environment])

    model_config = ConfigDict(
        title="Test Input Schema",
        json_schema_extra={"additionalProperties": True, "omit_default": True},
    )


# Ownship
ownship_initial = Initial(
    position=Position(latitude=57.7089, longitude=11.9746),  # Gothenburg
    sog=20.0,
    cog=90.0,
    nav_status=AISNavStatus.UNDER_WAY_USING_ENGINE,
)

ownship = OwnShip(
    static=ShipStatic(id=uuid4(), length=230.0, width=30.0, ship_type=GeneralShipType.PASSENGER),
    initial=ownship_initial,
)

# Target vessel 1 (Head-on)
target1_initial = Initial(
    position=Position(latitude=57.7089, longitude=10.9746),  # West of Gothenburg
    sog=20.0,
    cog=270.0,
    nav_status=AISNavStatus.UNDER_WAY_USING_ENGINE,
)

target1 = TargetShip(
    static=ShipStatic(id=uuid4(), length=180.0, width=28.0, ship_type=GeneralShipType.CARGO), initial=target1_initial
)


# Traffic situation
traffic_situation = TrafficSituation(
    title="head-on scenario",
    description="One vessel is approaching head-on",
    start_time=datetime.now(),
    own_ship=ownship,
    target_ships=[target1],
)


name_example = "AutoNavigation-System 1"
name_example1 = "Simulator-System 1"
version_example = "1.2.3"
vendor_example = "CompanyABC"


class SoftwareConfig(BaseModelConfig):
    name: str = Field(..., description="The name of the system", examples=[name_example])
    version: str = Field(..., description="The software version", examples=["1.2.3"])
    vendor: str = Field(..., description="The name of the system vendor", examples=["CompanyABC"])

    model_config = ConfigDict(json_schema_extra={"additionalProperties": True})


software_config_example = SoftwareConfig(name=name_example, version=version_example, vendor=vendor_example)
software_config_example1 = SoftwareConfig(name=name_example1, version=version_example, vendor=vendor_example)


class CagaConfiguration(SoftwareConfig):
    vendor_minimum_distance_to_targets: float = Field(
        None, description="Minimum distance in meters that the system will keep to other Vessels", examples=[100]
    )
    vendor_critical_TCPA: float = Field(  # noqa: N815
        None,
        description="If the projected CPA is less than minimumDistanceToTargets, and TCPA falls below criticalTCPA, a new manoeuver should be calculated",
        examples=[1000],
    )
    vendor_manoeuver_delay: float = Field(
        None,
        description="Time given in seconds to the navigator / system, before the proposed manoeuver is no longer able to be excecuted",
        examples=[20],
    )
    vendor_safety_depth: float = Field(None, description="Minimum safety depth", examples=[30])
    vendor_automatic_manoeuver_acceptance_time: float = Field(
        None,
        description="If automatic maneuver acceptance is enabled, the new route will be activated after a specified number of seconds",
        examples=[20],
    )

    model_config = ConfigDict(json_schema_extra={"additionalProperties": True})


caga_config_example = CagaConfiguration(
    name=name_example,
    version=version_example,
    vendor=vendor_example,
    minimum_distance_to_targets=100,
    critical_TCPA=1000,
    manoeuver_delay=20,
    safety_depth=20,
    automatic_manoeuver_acceptance_time=7,
)


class EncounterType(str, Enum):
    OVERTAKING_STAND_ON = "Overtaking stand-on"
    OVERTAKING_GIVE_WAY = "Overtaking give-way"
    HEAD_ON = "Head-on"
    CROSSING_GIVE_WAY = "Crossing give-way"
    CROSSING_STAND_ON = "Crossing stand-on"
    NO_RISK = "No Risk"


class PredictedPoint(BaseModelConfig):
    time: Union[datetime, int] = Field(
        ...,
        description="Date and Time of the predicted value `ISO 8601` format `YYYY-MM-DDThh:mm:ssZ`",
        examples=[datetime.now()],
    )
    value: Union[float, Any] = Field(..., description="Value of the prediction", examples=[position_example, 100])


position_example = Position(latitude=57.2343, longitude=10.3432)
position_example2 = Position(latitude=57.2345, longitude=10.3432)
position_example3 = Position(latitude=57.2349, longitude=10.3430)

predicted_point_example = PredictedPoint(time=datetime.now(), value=position_example)
predicted_point_example2 = PredictedPoint(time=datetime.now() + timedelta(seconds=10), value=position_example2)
predicted_point_example3 = PredictedPoint(time=datetime.now() + timedelta(seconds=20), value=position_example3)

waypoint_example2 = Waypoint(position=position_example2, turn_radius=500, data=Data(sog=data_point_example1))
waypoint_example3 = Waypoint(position=position_example3, turn_radius=500, data=Data(sog=data_point_example1))


class DetectedShip(BaseModelConfig):
    id: UUID = Field(..., description="Unique Identifier", examples=[uuid4()])

    position: Position = Field(
        ...,
        title="Longitude and Latitude Values",
        description="A geographical coordinate",
        examples=[Position(latitude=51.2123, longitude=11.2313)],
    )
    sog: float = Field(
        ...,
        ge=0,
        title="ship speed over ground",
        description="Initial ship speed over ground in knots",
        examples=[10.0],
    )
    cog: float = Field(
        ...,
        ge=0,
        le=360,
        title="ship course over ground",
        description="Initial ship course over ground in degrees",
        examples=[45.0],
    )
    heading: Optional[float] = Field(
        None, ge=0, le=360, title="ship heading", description="Initial ship heading in degrees", examples=[45.2]
    )
    nav_status: AISNavStatus = Field(None, description="AIS Navigational Status")

    encounter_type: Optional[EncounterType] = Field(
        None, description="COLREG encounter type", examples=["Overtaking stand-on"]
    )
    colreg_rules_applied: List[int] = Field(
        None,
        description="COLREG rules the system is applying to the vessel. Each item in the list must be of type `int` corresponding to the COLREG rule number",
        examples=[[16, 17]],
    )
    distance_to_target: float = Field(
        None, description="Calculated distance from the own ship to the target vessel", examples=[1900.2]
    )
    dcpa: Optional[float] = Field(None, description="Calculated closest point of approach", examples=[100.3])
    tcpa: Optional[float] = Field(
        None, description="calculated time to closest point of approach in seconds", examples=[2131]
    )

    predictions: Dict[str, List[PredictedPoint]] = Field(
        None,
        description="List of predicted future values. This can be used to store data like a predicted path for each target vessel. The `value` field supports both numbers and objects",
        examples=[[predicted_point_example, predicted_point_example2, predicted_point_example3]],
    )

    model_config = ConfigDict(json_schema_extra={"additionalProperties": True})


detected_ship_example = DetectedShip(
    id=uuid4(),
    position=position_example,
    sog=10.2,
    cog=181,
    nav_status=AISNavStatus.UNDER_WAY_USING_ENGINE,
    encounter_type=EncounterType.HEAD_ON,
    colreg_rules_applied=[12],
    distance_to_target=874.00,
    dcpa=300,
    tcpa=1200,
    predictions={"position": [predicted_point_example, predicted_point_example2, predicted_point_example3]},
)

# %%


class SimulatedShip(BaseModelConfig):
    id: UUID = Field(..., description="Unique Identifier", examples=[uuid4()])

    position: Position = Field(
        ...,
        title="Longitude and Latitude Values",
        description="A geographical coordinate",
        examples=[Position(latitude=51.2123, longitude=11.2313)],
    )
    sog: float = Field(
        ...,
        ge=0,
        title="ship speed over ground",
        description="Initial ship speed over ground in knots",
        examples=[10.0],
    )
    cog: float = Field(
        ...,
        ge=0,
        le=360,
        title="ship course over ground",
        description="Initial ship course over ground in degrees",
        examples=[45.0],
    )
    heading: Optional[float] = Field(
        None, ge=0, le=360, title="ship heading", description="Initial ship heading in degrees", examples=[45.2]
    )
    nav_status: AISNavStatus = Field(..., description="AIS Navigational Status")

    acceleration: float = Field(None, description="Ship acceleration in `ms^-2`", examples=[0.01])
    rate_of_turn: float = Field(None, description="Ship rate of turn in `deg/s`", examples=[1.8])

    model_config = ConfigDict(json_schema_extra={"additionalProperties": True})


simulated_ship_example1 = SimulatedShip(
    id=uuid4(),
    position=position_example,
    sog=10.0,
    cog=181,
    nav_status=AISNavStatus.ENGAGED_IN_FISHING,
    acceleration=0.01,
    rate_of_turn=1,
)
simulated_ship_example2 = SimulatedShip(
    id=uuid4(),
    position=position_example3,
    sog=14.0,
    cog=7,
    nav_status=AISNavStatus.UNDER_WAY_USING_ENGINE,
    rate_of_turn=0,
    mmsi=123456789,
)
simulated_ship_example3 = SimulatedShip(
    id=uuid4(),
    position=position_example2,
    sog=20.0,
    cog=97,
    nav_status=AISNavStatus.UNDER_WAY_USING_ENGINE,
    rate_of_turn=3,
    mmsi=987654321,
)

# %%


class CagaTimeFrame(BaseModelConfig):
    time: Union[datetime, int] = Field(
        ...,
        description="Date and Time of the predicted value `ISO 8601` format `YYYY-MM-DDThh:mm:ssZ`",
        examples=[datetime.now()],
    )
    target_ships: List[DetectedShip] = Field(
        ..., description="list of target ships detected by the CAGA system", examples=[[detected_ship_example]]
    )
    internal_status: Any = Field(
        None, description="Dictionary containing additional internal  information about the system (health, status..)"
    )


caga_time_frame_example = CagaTimeFrame(time=datetime.now(), target_ships=[detected_ship_example])


waypoint_list_example = [waypoint_example, waypoint_example2, waypoint_example3]


class CagaEvent(BaseModelConfig):
    time: Union[datetime, int] = Field(..., description="Date and Time of the event", examples=[datetime.now()])
    route: List[Waypoint] = Field(None, description="Planned CAGA Route", examples=[waypoint_list_example])

    calculation_time: Optional[float] = Field(None, description="Time to calculate new route")

    model_config = ConfigDict(json_schema_extra={"additionalProperties": True})


caga_event_example = CagaEvent(time=datetime.now(), route=waypoint_list_example)


class SimulatorEvent(BaseModelConfig):
    time: Union[datetime, int] = Field(..., description="Date and Time of the event", examples=[datetime.now()])

    model_config = ConfigDict(json_schema_extra={"additionalProperties": True})


class CagaData(BaseModelConfig):
    configuration: CagaConfiguration = Field(..., description="System Configuration", examples=[caga_config_example])
    time_series_data: List[CagaTimeFrame] = Field(
        ..., description="Time series data from the system", examples=[[caga_time_frame_example]]
    )
    event_data: List[CagaEvent] = Field(None, description="Event data from the system", examples=[[caga_event_example]])


auto_navigation_data_example = CagaData(
    configuration=caga_config_example, time_series_data=[caga_time_frame_example], event_data=[caga_event_example]
)


class SimulationTimeFrame(BaseModelConfig):
    time: Union[datetime, int] = Field(
        ...,
        description="Date and Time of the predicted value `ISO 8601` format `YYYY-MM-DDThh:mm:ssZ`",
        examples=[datetime.now()],
    )
    own_ship: SimulatedShip
    target_ships: List[SimulatedShip]


simulation_time_frame_example = SimulationTimeFrame(
    time=datetime.now(),
    own_ship=simulated_ship_example3,
    target_ships=[simulated_ship_example1, simulated_ship_example2],
)
simulation_time_frame_example1 = SimulationTimeFrame(
    time=datetime.now() + timedelta(seconds=10),
    own_ship=simulated_ship_example3,
    target_ships=[simulated_ship_example1, simulated_ship_example2],
)


class SimulationData(BaseModelConfig):
    configuration: SoftwareConfig = Field(
        ..., description="Simulator software configuration", examples=[software_config_example1]
    )
    time_series_data: List[SimulationTimeFrame] = Field(
        ...,
        description="TimeSeries data originating from the Simulator",
        examples=[[simulation_time_frame_example, simulation_time_frame_example1]],
    )
    event_data: List[SimulatorEvent] = Field(None, description="Event data from the simulator")


simulation_data_example = SimulationData(
    configuration=software_config_example1,
    time_series_data=[simulation_time_frame_example, simulation_time_frame_example1],
)


class OutputSchema(BaseModelConfig):
    creation_time: datetime = Field(
        ...,
        description="Date and Time that this file was created, in `ISO 8601` format `YYYY-MM-DDThh:mm:ssZ`. This should be the simulation end time.",
        examples=[datetime.now()],
    )
    traffic_situation: Optional[TrafficSituation] = Field(
        None,
        description="The traffic situation that was simulated (input file). This should remain unmofidied.",
    )
    caga_data: Optional[CagaData] = Field(
        None,
        description="Data generated by the system under test (auto-navigation / collision and grounding avoidance system) during the scenario.",
        examples=[auto_navigation_data_example],
    )
    simulation_data: Optional[SimulationData] = Field(
        None, description="Data generated by the simulator duirng the scenario", examples=[simulation_data_example]
    )

    model_config = ConfigDict(
        title="Test Output Schema",
        json_schema_extra={
            "description": "#### This is a JSON schema for result data originating from Collision and Grounding Avoidance systems",
            "additionalProperties": True,
        },
    )


def publish_schema(
    schema_dir: Union[str, os.PathLike[str], None] = None,
    docs_dir: Union[str, os.PathLike[str], None] = None,
):
    """Generate input and output schema and the corresponding html documentation.

    Parameters
    ----------
    schema_dir : Union[str, os.PathLike[str], None], optional
        The folder in which the schema files shall be generated in.
        If None, schema files will be generated in ./schema/caga.
        , by default None
    docs_dir : Union[str, os.PathLike[str]]
        The folder in which the html documentation files shall be generated in.
        If None, html files will be generated in ./docs/schema/caga.
        , by default None
    """
    from maritime_schema.utils.publish import generate_docs, generate_schema

    schema_dir_default = Path.cwd() / "schema/caga"
    schema_dir = schema_dir or schema_dir_default

    docs_dir_default = Path.cwd() / "docs/schema/caga"
    docs_dir = docs_dir or docs_dir_default

    # Make sure schema_dir argument is of type Path. If not, cast it to Path type.
    schema_dir = schema_dir if isinstance(schema_dir, Path) else Path(schema_dir)

    # Make sure docs_dir argument is of type Path. If not, cast it to Path type.
    docs_dir = docs_dir if isinstance(docs_dir, Path) else Path(docs_dir)

    # Generate input schema
    generate_schema(
        model=TrafficSituation,
        name="input_schema",
        schema_dir=schema_dir,
    )

    # Generate output schema
    generate_schema(
        model=OutputSchema,
        name="output_schema",
        schema_dir=schema_dir,
        by_alias=True,
    )

    # Generate html documentation
    generate_docs(
        schema_dir=schema_dir,
        docs_dir=docs_dir,
    )
