# pyright: reportPrivateUsage=false

from pathlib import Path

from maritime_schema.types.caga import publish_schema


def test_publish_schema():
    # Prepare
    target_dir: Path = Path(__file__).parent.parent.parent / "src/maritime_schema/schema/caga"
    docs_dir: Path = Path(__file__).parent.parent.parent / "docs/source/schema/caga"
    input_schema_json_file: Path = target_dir / "input_schema.json"
    input_schema_html_file: Path = docs_dir / "input_schema.html"
    output_schema_json_file: Path = target_dir / "output_schema.json"
    output_schema_html_file: Path = docs_dir / "output_schema.html"
    input_schema_json_file.unlink(missing_ok=True)
    input_schema_html_file.unlink(missing_ok=True)
    output_schema_json_file.unlink(missing_ok=True)
    output_schema_html_file.unlink(missing_ok=True)
    # Execute
    publish_schema()
    # Assert
    assert target_dir.exists()
    print(f"location of input_schema_json_file: {input_schema_json_file.absolute()}")
    assert input_schema_json_file.exists()
    assert input_schema_html_file.exists()
    assert output_schema_json_file.exists()
    assert output_schema_html_file.exists()
