# pyright: reportPrivateUsage=false

from pathlib import Path

from maritime_schema.types.caga import publish_schema
from maritime_schema.types.caga_examples import create_own_ship_example


def test_publish_schema():
    # Prepare
    schema_dir: Path = Path.cwd() / "schema/caga"
    docs_dir: Path = Path.cwd() / "docs/schema/caga"
    input_schema_json_file: Path = schema_dir / "input_schema.json"
    input_schema_html_file: Path = docs_dir / "input_schema.html"
    output_schema_json_file: Path = schema_dir / "output_schema.json"
    output_schema_html_file: Path = docs_dir / "output_schema.html"
    input_schema_json_file.unlink(missing_ok=True)
    input_schema_html_file.unlink(missing_ok=True)
    output_schema_json_file.unlink(missing_ok=True)
    output_schema_html_file.unlink(missing_ok=True)
    # Execute
    publish_schema(
        schema_dir=schema_dir,
        docs_dir=docs_dir,
    )
    # Assert
    assert schema_dir.exists()
    assert docs_dir.exists()
    print(f"location of input_schema_json_file: {input_schema_json_file.absolute()}")
    assert input_schema_json_file.exists()
    assert input_schema_html_file.exists()
    assert output_schema_json_file.exists()
    assert output_schema_html_file.exists()


def test_generate_waypoints():
    """Test that automatic waypoint generation works. create_own_ship_example creates a ship with no waypoints, but upon creation, we see that the ship has 2 waypoints!"""
    ship = create_own_ship_example()
    assert ship.waypoints is not None and len(ship.waypoints) == 2
