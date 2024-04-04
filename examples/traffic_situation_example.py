import datetime
from uuid import uuid4

from maritime_schema.types.caga import (
    AISNavStatus,
    GeneralShipType,
    Initial,
    OwnShip,
    Position,
    ShipStatic,
    TrafficSituation,
)

my_own_ship_static = ShipStatic(
    id=uuid4(),
    length=200,
    width=30,
    height=10,
    ship_type=GeneralShipType.FISHING,
    name="Starfish 2",
    mmsi=None,
    imo=None,
    speed_max=20,
)

start_position = Position(latitude=58.61, longitude=10.59)

initial_state = Initial(
    position=start_position, sog=10, cog=100, heading=200, nav_status=AISNavStatus.UNDER_WAY_USING_ENGINE
)

own_ship = OwnShip(static=my_own_ship_static, initial=initial_state, waypoints=None)


traffic_situation = TrafficSituation(
    title="example situation",
    description="an example traffic situation generated using the python package maritime-schema",
    start_time=datetime.datetime.now(),
    own_ship=own_ship,
    target_ships=[],
    environment=None,
)

traffic_situation_json = traffic_situation.model_dump_json(by_alias=True, indent=4)

with open("traffic_situation.json", "w") as f:
    _ = f.write(traffic_situation_json)
