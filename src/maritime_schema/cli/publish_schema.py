#!/usr/bin/env python
# coding: utf-8

import argparse
import logging
from pathlib import Path
from typing import Union

from maritime_schema.api import publish_schema
from maritime_schema.utils.logging import configure_logging

logger = logging.getLogger(__name__)


def _argparser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="publish-schema",
        usage="%(prog)s  [options [args]]",
        epilog="_________________publish-schema___________________",
        prefix_chars="-",
        add_help=True,
        description=("publish-schema"),
    )

    console_verbosity = parser.add_mutually_exclusive_group(required=False)

    _ = console_verbosity.add_argument(
        "-q",
        "--quiet",
        action="store_true",
        help=("console output will be quiet."),
        default=False,
    )

    _ = console_verbosity.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help=("console output will be verbose."),
        default=False,
    )

    _ = parser.add_argument(
        "--log",
        action="store",
        type=str,
        help="name of log file. If specified, this will activate logging to file.",
        default=None,
        required=False,
    )

    _ = parser.add_argument(
        "--log-level",
        action="store",
        type=str,
        help="log level applied to logging to file.",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        default="WARNING",
        required=False,
    )

    return parser


def main():
    """Entry point for console script as configured in setup.cfg.

    Runs the command line interface and parses arguments and options entered on the console.
    """

    parser = _argparser()
    args = parser.parse_args()

    # Configure Logging
    # ..to console
    log_level_console: str = "WARNING"
    if any([args.quiet, args.verbose]):
        log_level_console = "ERROR" if args.quiet else log_level_console
        log_level_console = "INFO" if args.verbose else log_level_console
    # ..to file
    log_file: Union[Path, None] = Path(args.log) if args.log else None
    log_level_file: str = args.log_level
    configure_logging(log_level_console, log_file, log_level_file)

    logger.info("Start publish-schema.py")

    # Invoke API
    publish_schema()


if __name__ == "__main__":
    main()
