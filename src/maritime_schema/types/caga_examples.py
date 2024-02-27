# flake8: noqa: D103
import uuid
from datetime import datetime


def generate_uuid():
    return uuid.UUID("6ba7b810-9dad-11d1-80b4-00c04fd430c8")


def create_environment_example():
    from maritime_schema.types.caga import Environment, PrecipitationType, WaveSpectra, WeatherCondition

    return Environment(
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


def create_position_example():
    from maritime_schema.types.caga import Position

    return Position(latitude=57.2343, longitude=10.3432)


def create_ship_static_example():
    from maritime_schema.types.caga import GeneralShipType, ShipStatic

    return ShipStatic(
        id=generate_uuid(),
        length=230.0,
        width=30.0,
        height=15.0,
        mmsi=123456789,
        name="RMS Titanic",
        ship_type=GeneralShipType.FISHING,
        imo=1000001,
    )


def create_initial_example():
    from maritime_schema.types.caga import AISNavStatus, Initial

    return Initial(
        position=create_position_example(),
        sog=12.3,
        cog=284.2,
        heading=283.1,
        nav_status=AISNavStatus.UNDER_WAY_USING_ENGINE,
    )


def create_data_point_example():
    from maritime_schema.types.caga import DataPoint

    return DataPoint(value=12.3, m_before_leg_change=100, m_after_leg_change=100, interp_method="linear")


def create_waypoint_example():
    from maritime_schema.types.caga import Data, Waypoint

    return Waypoint(
        position=create_position_example(),
        turn_radius=500,
        data=Data(sog=create_data_point_example(), heading=create_data_point_example()),
    )


def create_ship_example():
    from maritime_schema.types.caga import Ship

    return Ship(
        static=create_ship_static_example(), initial=create_initial_example(), waypoints=[create_waypoint_example()]
    )


def create_own_ship_example():
    from maritime_schema.types.caga import OwnShip

    return OwnShip(static=create_ship_static_example(), initial=create_initial_example(), waypoints=None)


def create_target_example():
    from maritime_schema.types.caga import TargetShip

    return TargetShip(static=create_ship_static_example(), initial=create_initial_example(), waypoints=None)


def create_traffic_situation():
    from maritime_schema.types.caga import TrafficSituation

    return TrafficSituation(
        title="head-on scenario",
        description="One vessel is approaching head-on",
        start_time=datetime.now(),
        own_ship=create_own_ship_example(),
        target_ships=[create_target_example()],
        environment=None,
    )


def create_software_config_example():
    from maritime_schema.types.caga import SoftwareConfig

    name_example = "AutoNavigation-System 1"
    version_example = "1.2.3"
    vendor_example = "CompanyABC"

    return SoftwareConfig(name=name_example, version=version_example, vendor=vendor_example)


def create_caga_config_example():
    from maritime_schema.types.caga import CagaConfiguration

    software_config = create_software_config_example()

    return CagaConfiguration(
        name=software_config.name,
        version=software_config.version,
        vendor=software_config.vendor,
        vendor_minimum_distance_to_targets=100,
        vendor_critical_TCPA=1000,
        vendor_manoeuver_delay=20,
        vendor_safety_depth=20,
        vendor_automatic_manoeuver_acceptance_time=7,
    )


def create_predicted_point_example():
    from maritime_schema.types.caga import PredictedPoint

    return PredictedPoint(time=datetime.now(), value=create_position_example())


def create_detected_ship_example():
    from maritime_schema.types.caga import AISNavStatus, DetectedShip, EncounterType

    return DetectedShip(
        id=generate_uuid(),
        position=create_position_example(),
        sog=10.2,
        cog=181,
        heading=182,
        nav_status=AISNavStatus.UNDER_WAY_USING_ENGINE,
        encounter_type=EncounterType.HEAD_ON,
        colreg_rules_applied=[12],
        distance_to_target=874.00,
        dcpa=300,
        tcpa=1200,
        predictions={
            "position": [
                create_predicted_point_example(),
                create_predicted_point_example(),
                create_predicted_point_example(),
            ]
        },
    )


def create_simulated_ship_example():
    from maritime_schema.types.caga import AISNavStatus, SimulatedShip

    return SimulatedShip(
        id=generate_uuid(),
        position=create_position_example(),
        sog=10.0,
        cog=181,
        heading=182,
        nav_status=AISNavStatus.ENGAGED_IN_FISHING,
        acceleration=0.01,
        rate_of_turn=1,
    )


def create_caga_time_frame_example():
    from maritime_schema.types.caga import CagaTimeFrame

    return CagaTimeFrame(time=datetime.now(), target_ships=[create_detected_ship_example()], internal_status=None)


def create_caga_event_example():
    from maritime_schema.types.caga import CagaEvent

    return CagaEvent(
        time=datetime.now(),
        route=[create_waypoint_example(), create_waypoint_example(), create_waypoint_example()],
        calculation_time=1.242,
    )


def create_caga_data_example():
    from maritime_schema.types.caga import CagaData

    return CagaData(
        configuration=create_caga_config_example(),
        time_series_data=[create_caga_time_frame_example()],
        event_data=[create_caga_event_example()],
    )


def create_simulation_timeframe_example():
    from maritime_schema.types.caga import SimulationTimeFrame

    return SimulationTimeFrame(
        time=datetime.now(),
        own_ship=create_simulated_ship_example(),
        target_ships=[create_simulated_ship_example(), create_simulated_ship_example()],
    )


def create_simulation_data_example():
    from maritime_schema.types.caga import SimulationData

    return SimulationData(
        configuration=create_software_config_example(),
        time_series_data=[create_simulation_timeframe_example(), create_simulation_timeframe_example()],
        event_data=[],
    )
