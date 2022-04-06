"""{{cookiecutter.project_short_description}}"""
import logging
from argparse import ArgumentParser


def main(*argv) -> None:
    """Main program entry point for CLI."""
    arg_parser = ArgumentParser(
        description="{{cookiecutter.project_short_description}}"
    )
    arg_parser.add_argument(
        "--verbose",
        "-v",
        action="count",
        default=0,
        help="-v for info level logs, -vv for debug",
    )
    args = arg_parser.parse_args(argv) if argv else arg_parser.parse_args()
    if args.verbose > 1:
        logging.basicConfig(level=logging.DEBUG)
    elif args.verbose == 1:
        logging.basicConfig(level=logging.INFO)
    else:
        logging.basicConfig()
