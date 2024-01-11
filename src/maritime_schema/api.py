import logging
import os
from pathlib import Path
from typing import Union

from dictIO import DictReader

from maritime_schema.subpackage1.module1 import int_to_str
from maritime_schema.subpackage2.module2 import str_to_int

__ALL__ = ["run", "MaritimeSchemaProcess"]

logger = logging.getLogger(__name__)


def run(
    config_file: Union[str, os.PathLike[str]],
    option: bool = False,
):
    """Run the maritime-schema process.

    Run the maritime-schema process and .. (long description).

    Parameters
    ----------
    config_file : Union[str, os.PathLike[str]]
        file containing the maritime-schema configuration
    option : bool, optional
        if True, does something differently, by default False

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

    if option:
        logger.info("option is True. maritime-schema process will do something differently.")

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
        self._run_number: int = 0
        self._max_number_of_runs: int = 1
        self.terminate: bool = False
        self._read_config_file()
        return

    def run(self):
        """Run the maritime-schema process.

        Runs the maritime-schema process in a self-terminated loop.
        """

        # Run maritime-schema process until termination is flagged
        while not self.terminate:
            self._run_process()
            self.terminate = self._run_number >= self._max_number_of_runs
        return

    @property
    def run_number(self) -> int:
        """Example for a read only property."""
        return self._run_number

    @property
    def max_number_of_runs(self) -> int:
        """Example for a read/write property implemented through a pair of explicit
        getter and setter methods (see below for the related setter method).
        """
        return self._max_number_of_runs

    @max_number_of_runs.setter
    def max_number_of_runs(self, value: int):
        """Setter method that belongs to above getter method.

        Note that implementing specific getter- and setter methods is in most cases not necessary.
        The same can be achieved by simply making the instance variable a public attribute.
        I.e., declaring the instance variable in __init__() not as
        self._max_number_of_runs: int = ..  # (-> private instance variable)
        but as
        self.max_number_of_runs: int = ..   # (-> public attribute)

        However, in some cases the additional effort of implementing explicit getter- and setter- methods
        as in this example can be reasoned, for instance if you have a need for increased control
        and want be able to cancel or alter code execution, or write log messages whenever a property
        gets reads or written from outside.
        """

        self._max_number_of_runs = value
        return

    def _run_process(self):
        """Execute a single run of the maritime-schema process."""
        self._run_number += 1

        logger.info(f"Start run {self._run_number}")

        # Do stuff
        _string: str = _do_cool_stuff(self._run_number)
        _number: int = _do_even_cooler_stuff(_string)
        logger.debug(f"\t _string: {_string} _number: {_number}")

        logger.info(f"Successfully finished run {self._run_number}")

        return

    def _read_config_file(self):
        """Read config file."""
        config = DictReader.read(self.config_file)
        if "max_number_of_runs" in config:
            self._max_number_of_runs = config["max_number_of_runs"]
        return


def _do_cool_stuff(run_number: int) -> str:
    """Do cool stuff.

    Converts the passed in run number to a string.

    Parameters
    ----------
    run_number : int
        the run number

    Returns
    -------
    str
        the run number converted to string
    """
    result: str = int_to_str(run_number)
    return result


def _do_even_cooler_stuff(string: str) -> int:
    """Do even cooler stuff.

    Converts the passed in string-formatted integer back to an integer.

    Parameters
    ----------
    string : str
        the string-formatted integer to be converted back to an integer

    Returns
    -------
    int
        the resulting integer
    """
    result: int = str_to_int(string)
    return result
