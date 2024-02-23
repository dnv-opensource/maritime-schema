# pyright: reportPrivateUsage=false
import sys
from argparse import ArgumentError
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Union

import pytest
from pytest import MonkeyPatch

from maritime_schema.cli import publish_schema
from maritime_schema.cli.publish_schema import _argparser, main

# *****Test commandline interface (CLI)************************************************************


@dataclass()
class CliArgs:
    # Expected default values for the CLI arguments when publish-schema gets called via the commandline
    quiet: bool = False
    verbose: bool = False
    log: Union[str, None] = None
    log_level: str = field(default_factory=lambda: "WARNING")


@pytest.mark.parametrize(
    "inputs, expected",
    [
        ([], CliArgs()),
        (["-q"], CliArgs(quiet=True)),
        (["--quiet"], CliArgs(quiet=True)),
        (["-v"], CliArgs(verbose=True)),
        (["--verbose"], CliArgs(verbose=True)),
        (["-qv"], ArgumentError),
        (["--log", "logFile"], CliArgs(log="logFile")),
        (["--log"], ArgumentError),
        (["--log-level", "INFO"], CliArgs(log_level="INFO")),
        (["--log-level"], ArgumentError),
    ],
)
def test_cli(
    inputs: List[str],
    expected: Union[CliArgs, type],
    monkeypatch: MonkeyPatch,
):
    # sourcery skip: no-conditionals-in-tests
    # sourcery skip: no-loop-in-tests
    # Prepare
    monkeypatch.setattr(sys, "argv", ["publish-schema"] + inputs)
    parser = _argparser()
    # Execute
    if isinstance(expected, CliArgs):
        args_expected: CliArgs = expected
        args = parser.parse_args()
        # Assert args
        for key in args_expected.__dataclass_fields__:
            assert args.__getattribute__(key) == args_expected.__getattribute__(key)
    elif issubclass(expected, Exception):
        exception: type = expected
        # Assert that expected exception is raised
        with pytest.raises((exception, SystemExit)):
            args = parser.parse_args()
    else:
        raise AssertionError()


# *****Ensure the CLI correctly configures logging*************************************************


@dataclass()
class ConfigureLoggingArgs:
    # Values that main() is expected to pass to ConfigureLogging() by default when configuring the logging
    log_level_console: str = field(default_factory=lambda: "WARNING")
    log_file: Union[Path, None] = None
    log_level_file: str = field(default_factory=lambda: "WARNING")


@pytest.mark.parametrize(
    "inputs, expected",
    [
        ([], ConfigureLoggingArgs()),
        (["-q"], ConfigureLoggingArgs(log_level_console="ERROR")),
        (["--quiet"], ConfigureLoggingArgs(log_level_console="ERROR")),
        (["-v"], ConfigureLoggingArgs(log_level_console="INFO")),
        (["--verbose"], ConfigureLoggingArgs(log_level_console="INFO")),
        (["-qv"], ArgumentError),
        (["--log", "logFile"], ConfigureLoggingArgs(log_file=Path("logFile"))),
        (["--log"], ArgumentError),
        (["--log-level", "INFO"], ConfigureLoggingArgs(log_level_file="INFO")),
        (["--log-level"], ArgumentError),
    ],
)
def test_logging_configuration(
    inputs: List[str],
    expected: Union[ConfigureLoggingArgs, type],
    monkeypatch: MonkeyPatch,
):
    # sourcery skip: no-conditionals-in-tests
    # sourcery skip: no-loop-in-tests
    # Prepare
    monkeypatch.setattr(sys, "argv", ["publish-schema"] + inputs)
    args: ConfigureLoggingArgs = ConfigureLoggingArgs()

    def fake_configure_logging(
        log_level_console: str,
        log_file: Union[Path, None],
        log_level_file: str,
    ):
        args.log_level_console = log_level_console
        args.log_file = log_file
        args.log_level_file = log_level_file

    def fake_publish_schema():
        pass

    monkeypatch.setattr(publish_schema, "configure_logging", fake_configure_logging)
    monkeypatch.setattr(publish_schema, "publish_schema", fake_publish_schema)
    # Execute
    if isinstance(expected, ConfigureLoggingArgs):
        args_expected: ConfigureLoggingArgs = expected
        main()
        # Assert args
        for key in args_expected.__dataclass_fields__:
            assert args.__getattribute__(key) == args_expected.__getattribute__(key)
    elif issubclass(expected, Exception):
        exception: type = expected
        # Assert that expected exception is raised
        with pytest.raises((exception, SystemExit)):
            main()
    else:
        raise AssertionError()
