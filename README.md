# maritime-schema

Python package containing data classes and corresponding JSON schemata for common types used in generating traffic scenarios and testing of autonomous navigation systems.

The data classes in the package are implemented as data models using the [pydantic](https://docs.pydantic.dev/) framework. <br>

All data classes reside in subpackage `maritime_schema.types.caga` and can be imported from there.

## Installation

```sh
pip install maritime-schema
```

## Getting Started

### Creating an Input Schema File (Traffic Situation)

First, let’s see how we can create a ship. We will start off using the `ShipStatic` class. This allows us to define static information relating to a ship - information which will not change during the scenario. This includes things such as length, the ship type, name, and MMSI and IMO numbers.

Each ship must have a unique id, in the form of a UUID. for this, the uuid module from the standard library can be used.

The `GeneralShipType` lists several general ship types, like those found in AIS.

Note that some of these fields (such as MMSI & IMO) can be left as None, as not all ships might have this data.

```py
from maritime_schema.types.caga import ShipStatic, GeneralShipType
from uuid import uuid4

my_own_ship_static = ShipStatic(
    id=uuid4(),
    length=200, width=30, height=10,
    ship_type=GeneralShipType.FISHING,
    name="Starfish 2",
    mmsi=None, imo=None,
)
```

Next, we can define the initial conditions for this ship. To do this we will use the `Initial` and `Position` classes.

We can use the `AISNavStatus` class to set the `nav_status` of the ship. This contains several navigational statuses from AIS.

```py
from maritime_schema.types.caga import Initial, Position, AISNavStatus

initial_state = Initial(
    position=Position(latitude=58.61, longitude=10.59),
    sog=10, cog=100, heading=200,
    nav_status=AISNavStatus.UNDER_WAY_USING_ENGINE
)

```

Now let's put it all together into a ship object. An OwnShip has static information, and initial state, and could also have waypoints. However in this simple example, waypoints will be set to `None`.

```py
from maritime_schema.types.caga import OwnShip

own_ship = OwnShip(static=my_own_ship_static, initial=initial_state, waypoints=None)

```

Let's put the `own_ship` we just created into a traffic situation.

```py
from maritime_schema.types.caga import TrafficSituation

traffic_situation = TrafficSituation(
    title="example situation",
    description="an example traffic situation generated using the maritime-schema python package",
    start_time=datetime.datetime.now(),
    own_ship=own_ship,
    target_ships=[],
    environment=None,
)
```

If we now want to save this traffic situation to a file, it's very easy to do, by simply calling `traffic_situation.model_dump_json()`.

```py
traffic_situation_json = traffic_situation.model_dump_json(by_alias=True, indent=4)

with open("traffic_situation.json", "w") as f:
    _ = f.write(traffic_situation_json)
```

Let's see the output:

```JSON
{
    "title": "example situation",
    "description": "an example traffic situation generated using the python package maritime-schema",
    "startTime": "2024-04-03T09:51:07.665082",
    "ownShip": {
        "static": {
            "id": "a342770d-8900-4f2f-9cea-608e840b2a51",
            "length": 200.0,
            "width": 30.0,
            "height": 10.0,
            "mmsi": null,
            "imo": null,
            "name": "Starfish 2",
            "shipType": "Fishing"
        },
        "initial": {
            "position": {
                "latitude": 58.61,
                "longitude": 10.59
            },
            "sog": 10.0,
            "cog": 100.0,
            "heading": 200.0,
            "navStatus": "Under way using engine"
        },
        "waypoints": [
            {
                "position": {
                    "latitude": 58.61,
                    "longitude": 10.59,
                    "data": {
                        "sog": {
                            "value": 10.0,
                            "mBeforeLegChange": 0.0,
                            "mAfterLegChange": 0.0,
                            "interpMethod": null
                        },
                        "heading": null,
                        "cog": {
                            "value": 100.0,
                            "mBeforeLegChange": 0.0,
                            "mAfterLegChange": 0.0,
                            "interpMethod": null
                        }
                    }
                },
                "turnRadius": null,
                "data": null
            },
            {
                "position": {
                    "latitude": 58.594299006647965,
                    "longitude": 10.759356798943921
                },
                "turnRadius": null,
                "data": null
            }
        ]
    },
    "targetShips": [],
    "environment": null
}
```

### Creating an Output Schema File

Creating output schema files is similar to creating traffic situations, however, some additional classes are required.

## Usage Example

API:

```py
from maritime_schema.types import ...
```

CLI:

The JSON schemata are contained in the repository in folder ./schema
If you did not clone the repository but installed the maritime-schema package as a dependency in your project you can call `publish-schema` on the command line to (re-)generate the schemata:

```sh
publish-schema
```

The `publish-schema` command will generate the JSON schemata in `(current working directory)/schema` <br>
and a corresponding html documentation of the schemata in `(current working directory)/docs/schema`

_For more examples and usage, please refer to maritime-schema's [documentation][maritime_schema_docs]._

## Development Setup

1. Install Python 3.9 or higher, i.e. [Python 3.10](https://www.python.org/downloads/release/python-3104/) or [Python 3.11](https://www.python.org/downloads/release/python-3114/)

2. Update pip and setuptools:

    ```sh
    python -m pip install --upgrade pip setuptools
    ```

3. git clone the maritime-schema repository into your local development directory:

    ```sh
    git clone https://github.com/dnv-opensource/maritime-schema path/to/your/dev/maritime-schema
    ```

4. In the maritime-schema root folder:

    Create a Python virtual environment:

    ```sh
    python -m venv .venv
    ```

    Activate the virtual environment:

    ..on Windows:

    ```sh
    > .venv\Scripts\activate.bat
    ```

    ..on Linux:

    ```sh
    source .venv/bin/activate
    ```

    Update pip and setuptools:

    ```sh
    (.venv) $ python -m pip install --upgrade pip setuptools
    ```

    Install maritime-schema's dependencies:

    ```sh
    (.venv) $ pip install -r requirements-dev.txt
    ```

    This should return without errors.

    Finally, install maritime-schema itself, yet not as a regular package but as an _editable_ package instead, using the pip install option -e:

    ```sh
    (.venv) $ pip install -e .
    ```

5. Test that the installation works (in the maritime-schema root folder):

    ```sh
    (.venv) $ pytest .
    ```

## Meta

Copyright (c) 2024 [DNV](https://www.dnv.com) AS. All rights reserved.

Minos Hemrich - minos.hemrich@dnv.com

Tom Arne Pedersen - tom.arne.pedersen@dnv.com

Claas Rostock - [@LinkedIn](https://www.linkedin.com/in/claasrostock/?locale=en_US) - claas.rostock@dnv.com

Distributed under the MIT license. See [LICENSE](LICENSE.md) for more information.

[https://github.com/dnv-opensource/maritime-schema](https://github.com/dnv-opensource/maritime-schema)

## Contributing

1. Fork it (<https://github.com/dnv-opensource/maritime-schema/fork>)
2. Create your branch (`git checkout -b my-branch-name`)
3. Commit your changes (`git commit -am 'place a descriptive commit message here'`)
4. Push to the branch (`git push origin my-branch-name`)
5. Create a new Pull Request in GitHub

For your contribution, please make sure you follow the [STYLEGUIDE](STYLEGUIDE.md) before creating the Pull Request.

<!-- Markdown link & img dfn's -->

[maritime_schema_docs]: https://dnv-opensource.github.io/maritime-schema/README.html
