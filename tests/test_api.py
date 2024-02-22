# pyright: reportPrivateUsage=false
from pathlib import Path

import pytest

from maritime_schema.api import MaritimeSchemaProcess, run


def test_file_not_found_exception():
    # Prepare
    config_file = Path("this_file_does_not_exist")
    # Execute and Assert
    with pytest.raises(FileNotFoundError):
        _ = run(config_file)


def test_run():
    # Prepare
    config_file = Path("test_config_file")
    # Execute
    run(config_file=config_file)
    # Assert
    # (nothing to assert. Assertion is that no exception is thrown.)


class TestMaritimeSchemaProcess:
    def test_init(self):
        # Prepare
        config_file = Path("test_config_file.json")
        # Execute
        process = MaritimeSchemaProcess(config_file=config_file)
        # Assert
        assert process.config_file is config_file

    def test_init_with_empty_config_file(self):
        # sourcery skip: class-extract-method
        # Prepare
        config_file = Path("test_config_file_empty.json")
        # Execute
        process = MaritimeSchemaProcess(config_file=config_file)
        # Assert
        assert process.config_file is config_file


# @TODO: To be implemented
@pytest.mark.skip(reason="To be implemented")
def test_example_skip():
    """Example of a test skipped because it is not yet implemented."""
    pass
