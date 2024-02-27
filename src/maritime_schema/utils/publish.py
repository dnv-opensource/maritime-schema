import json
import logging
import os
from glob import glob
from pathlib import Path
from typing import List, Union

from dictIO.utils.path import relative_path
from json_schema_for_humans.generate import (
    SchemaToRender,
    TemplateRenderer,
    generate_schemas_doc,
)
from json_schema_for_humans.generation_configuration import GenerationConfiguration
from pydantic import BaseModel
from pydantic._internal._model_construction import ModelMetaclass

__all__ = ["generate_schema", "generate_docs"]


logger = logging.getLogger(__name__)


def generate_schema(
    model: Union[BaseModel, ModelMetaclass],
    name: str,
    schema_dir: Union[str, os.PathLike[str], None] = None,
    by_alias: bool = False,
):
    """Generate json schema in the given target folder.

    Parameters
    ----------
    model : BaseModel
        The pydantic model for which the schema shall be generated
    name : str
        The filename the schema shall be given (without extension)
    schema_dir : Union[str, os.PathLike[str], None], optional
        The folder in which the schema file shall be generated in.
        If None, schema file will be generated in ./schema.
        , by default None
    by_alias : bool, optional
        Whether to serialize using field aliases., by default False
    """
    schema_dir_default = Path.cwd() / "schema"
    schema_dir = schema_dir or schema_dir_default

    # Assert model argument is a pydantic BaseModel
    # Background: ModelMetaClass is added just to please static type checking,
    #             which would otherwise complain.
    #             Behind the scenes in pdyantic, models always inherit the attributes of BaseModel.
    assert hasattr(model, "model_json_schema")

    # Make sure schema_dir argument is of type Path. If not, cast it to Path type.
    schema_dir = schema_dir if isinstance(schema_dir, Path) else Path(schema_dir)

    # Create schema_dir if it does not exist
    schema_dir.mkdir(parents=True, exist_ok=True)

    # Generate json schema
    json_file: Path = schema_dir / f"{name}.json"
    schema = json.dumps(
        model.model_json_schema(by_alias=by_alias),  # pyright: ignore
        indent=4,
    )
    with open(json_file, "w", encoding="utf-8") as f:
        _ = f.write(schema)

    return


def generate_docs(
    schema_dir: Union[str, os.PathLike[str], None] = None,
    docs_dir: Union[str, os.PathLike[str], None] = None,
):
    """Generate schema documentation in the given docs folder.

    The documentation will be generated in html format.

    Parameters
    ----------
    schema_dir : Union[str, os.PathLike[str], None], optional
        The source folder containing the json schemata
        for which the html documentation shall be generated.
        If None, schemata will be read from in ./schema.
        , by default None
    docs_dir : Union[str, os.PathLike[str]]
        The folder in which the html documentation files shall be generated in.
        If None, html files will be generated in ./docs/schema.
        , by default None
    """
    schema_dir_default = Path.cwd() / "schema"
    schema_dir = schema_dir or schema_dir_default

    docs_dir_default = Path.cwd() / "docs/schema"
    docs_dir = docs_dir or docs_dir_default

    # Make sure schema_dir argument is of type Path. If not, cast it to Path type.
    schema_dir = schema_dir if isinstance(schema_dir, Path) else Path(schema_dir)

    # Make sure docs_dir argument is of type Path. If not, cast it to Path type.
    docs_dir = docs_dir if isinstance(docs_dir, Path) else Path(docs_dir)

    # Create schema_dir if it does not exist
    schema_dir.mkdir(parents=True, exist_ok=True)

    # Create docs_dir if it does not exist
    docs_dir.mkdir(parents=True, exist_ok=True)

    # Collect all schemata in schema dir
    pattern: str = f"{str(schema_dir.absolute())}/**.json"
    schemata: List[Path] = [Path(file) for file in glob(pattern)]

    # Generate html documentation for schemata
    config: GenerationConfiguration = GenerationConfiguration(
        template_name="js",
        expand_buttons=True,
        link_to_reused_ref=False,
        show_breadcrumbs=False,
    )

    schemas_to_render: List[SchemaToRender] = []

    for schema in schemata:
        rel_path: Path = relative_path(from_path=schema_dir, to_path=schema.parent)
        name: str = schema.stem
        html_file: Path = docs_dir / rel_path / f"{name}.html"
        schema_to_render: SchemaToRender = SchemaToRender(
            schema_file=schema,
            result_file=html_file,
            output_dir=None,
        )
        schemas_to_render.append(schema_to_render)

    _ = generate_schemas_doc(
        schemas_to_render=schemas_to_render,
        template_renderer=TemplateRenderer(config),
    )

    return
