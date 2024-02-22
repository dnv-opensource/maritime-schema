import logging
import os
from pathlib import Path
from typing import Union

from maritime_schema.types import caga

__ALL__ = ["run", "MaritimeSchemaProcess"]

logger = logging.getLogger(__name__)


def run(
    config_file: Union[str, os.PathLike[str]],
):
    """Run the maritime-schema process.

    Run the maritime-schema process and .. (long description).

    Parameters
    ----------
    config_file : Union[str, os.PathLike[str]]
        file containing the maritime-schema configuration

    Raises
    ------
    FileNotFoundError
        if config_file does not exist
    """

    # Make sure config_file argument is of type Path. If not, cast it to Path type.
    config_file = config_file if isinstance(config_file, Path) else Path(config_file)

    # Check whether config file exists
    if not config_file.exists():
        logger.error(f"run: File {config_file} not found.")
        raise FileNotFoundError(config_file)

    process = MaritimeSchemaProcess(config_file)
    process.run()

    return


class MaritimeSchemaProcess:
    """Top level class encapsulating the maritime-schema process."""

    def __init__(
        self,
        config_file: Path,
    ):
        self.config_file: Path = config_file
        self._read_config_file()
        return

    def run(self):
        """Publish the maritime schema."""

        logger.info("Start publishing schema")

        caga.publish_schema()

        logger.info("Successfully published schema")

        return

    def _read_config_file(self):
        """Read config file."""
        # from dictIO import DictReader
        # config = DictReader.read(self.config_file)
        # do something with the config
        return
