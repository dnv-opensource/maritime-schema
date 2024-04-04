import datetime
from uuid import uuid4

from maritime_schema.types.caga import (
    AISNavStatus,
    CagaConfiguration,
    CagaData,
    CagaEvent,
    CagaTimeStep,
    Data,
    DataPoint,
    DetectedShip,
    EncounterType,
    OutputSchema,
    Position,
    TrafficSituation,
    Waypoint,
)

# create a caga_configuration
caga_configuration = CagaConfiguration(name="CAGA System 1", vendor="VendorABC", version="1.2.3")
# The generated route and waypoints. Note these are random values in this example, and do not reflect a real route.

# Each route leg should have an associated speed.
wp1_sog_data = DataPoint(value=10, m_after_leg_change=0, m_before_leg_change=0, interp_method="linear")
wp2_sog_data = DataPoint(value=10, m_after_leg_change=0, m_before_leg_change=0, interp_method="linear")

# The sog data is added to a Data class.
wp1_data = Data(sog=wp1_sog_data)  # type: ignore
wp2_data = Data(sog=wp2_sog_data)  # type: ignore

# Create the indivitual waypoints.
wp1 = Waypoint(position=Position(latitude=1, longitude=1), turn_radius=10, data=wp1_data)
wp2 = Waypoint(position=Position(latitude=1.1, longitude=1.2), turn_radius=10, data=wp2_data)

# create the event - a route was generated
event_1 = CagaEvent(time=datetime.datetime.now(), route=[wp1, wp2], calculation_time=1.32)

detected_ship_1_t1 = DetectedShip(
    id=uuid4(),
    position=Position(latitude=1.23, longitude=1.24),
    sog=2.31,
    cog=11,
    heading=10,
    nav_status=AISNavStatus.ENGAGED_IN_FISHING,
    encounter_type=EncounterType.HEAD_ON,
    colreg_rules_applied=[],
    distance_to_target=1023.21,
    dcpa=100,
    tcpa=121,
    predictions=None,
)

detected_ship_1_t2 = DetectedShip(
    id=uuid4(),
    position=Position(latitude=1.231, longitude=1.242),
    sog=2.31,
    cog=11,
    heading=9,
    nav_status=AISNavStatus.ENGAGED_IN_FISHING,
    encounter_type=EncounterType.HEAD_ON,
    colreg_rules_applied=[],
    distance_to_target=1023.21,
    dcpa=100,
    tcpa=121,
    predictions=None,
)

ts0 = CagaTimeStep(time=datetime.datetime.now(), target_ships=[detected_ship_1_t1], internal_status={"cpu_temp": 55})
ts1 = CagaTimeStep(
    time=datetime.datetime.now() + datetime.timedelta(seconds=1),
    target_ships=[detected_ship_1_t2],
    internal_status={"cpu_temp": 57},
)


# add the event to caga_data
caga_data = CagaData(configuration=caga_configuration, time_series_data=[ts0, ts1], event_data=[event_1])

# include the original traffic situation in the output file, in this example, we will load it from a file
with open("traffic_situation.json", "r") as f:
    data = f.read()
traffic_situation = TrafficSituation.model_validate_json(data)

# create the output_schema
output_schema = OutputSchema(
    creation_time=datetime.datetime.now(),
    traffic_situation=traffic_situation,
    caga_data=caga_data,
    simulation_data=None,
)

# serialize the output_schema as a json string
output_schema_file_json = output_schema.model_dump_json(by_alias=True, indent=4)

# save the json string to a file
with open("output_schema_file.json", "w") as f:
    _ = f.write(output_schema_file_json)
