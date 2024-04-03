import datetime

from maritime_schema.types.caga import (
    CagaConfiguration,
    CagaData,
    CagaEvent,
    OutputSchema,
    Position,
    TrafficSituation,
    Waypoint,
)

caga_configuration = CagaConfiguration(name="CAGA System 1", vendor="VendorABC", version="1.2.3")

wp1 = Waypoint(position=Position(latitude=1, longitude=1), turn_radius=10, data=None)
wp2 = Waypoint(position=Position(latitude=1.1, longitude=1.2), turn_radius=10, data=None)

event_1 = CagaEvent(time=datetime.datetime.now(), route=[wp1, wp2], calculation_time=None)

caga_data = CagaData(configuration=caga_configuration, time_series_data=[], event_data=[event_1])


# Load the traffic situation file into a string
with open("traffic_situation.json", "r") as f:
    data = f.read()

# Use the string data to create the model
traffic_situation = TrafficSituation.model_validate_json(data)


output_schema = OutputSchema(
    creation_time=datetime.datetime.now(),
    traffic_situation=traffic_situation,
    caga_data=caga_data,
    simulation_data=None,
)


output_schema_file_json = output_schema.model_dump_json(by_alias=True, indent=4)

with open("output_schema_file.json", "w") as f:
    _ = f.write(output_schema_file_json)
