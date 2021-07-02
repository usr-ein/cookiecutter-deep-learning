"""Argument parser for {{cookiecutter.project_slug}}"""

import os
import argparse
import toml
from path_type import PathType, ValType

with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "..", "pyproject.toml"), 'r') as f:
    pyproject = toml.load(f)

DEFAULT_DESC = pyproject['tool']['poetry']['description']

class InvalidCLIArgumentError(ValueError):
    pass

def validate_args(args):
    if False:
        raise InvalidCLIArgumentError("No bueno")

def parse_args():
    global DEFAULT_DESC

    # You can edit the desc manually here... or edit it in pyproject.toml once and for all
    parser = argparse.ArgumentParser(description=DEFAULT_DESC)

    parser.add_argument(
        "input",
        type=PathType(exists=True, val_type=ValType.DIR),
        help="Input dataset",
    )

    parser.add_argument(
        "-o",
        "--output",
        type=PathType(exists=None, val_type=ValType.ANY),
        help="Where to write the output",
        default=".",
    )

    parser.add_argument(
        "-i",
        "--int_param",
        type=int,
        help="Cool int param.",
    )

    parser.add_argument(
        "--float_param_optional",
        type=float,
        default=0.1,
        help="Cool optional float param.",
    )

    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Displays helpful information along.",
    )

    args = parser.parse_args()
    validate_args(args)
    return args
