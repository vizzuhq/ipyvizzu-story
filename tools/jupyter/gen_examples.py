"""A module for generating Jupyter Notebook examples."""

import subprocess
import sys
from pathlib import Path
from shutil import copytree, rmtree


def copy_examples(root: Path) -> None:
    """
    A method for copying examples directory to the site.

    Args:
        root: The path of the root directory.
    """

    src = root / "assets" / "docs" / "examples"
    dst = root / "docs" / "examples"
    if dst.exists():
        rmtree(dst)
    copytree(src, dst)


def run_nbconvert(root: Path, jupyter: str) -> None:
    """
    A method for running jupyter nbconvert.

    Args:
        root: The path of the root directory.
        jupyter: The path of jupyter.

    Raises:
        RuntimeError: If jupyter nbconvert return code is not 0.
    """

    # pylint: disable=duplicate-code

    command = [
        str(root / jupyter),
        "nbconvert",
        "--to",
        "html",
        "--template",
        "classic",
        "--execute",
        str(root / "docs" / "examples") + "/**/*.ipynb",
    ]
    with subprocess.Popen(command, stdout=subprocess.PIPE) as process:
        output_str, error_str = "", ""
        output, error = process.communicate()
        if output is not None:
            output_str = output.decode()
        if error is not None:
            error_str = error.decode()
        if process.returncode != 0:
            raise RuntimeError(
                f"jupyter nbconvert failed {process.returncode} {output_str} {error_str}"
            )


root_path = Path(__file__).parent / ".." / ".."
"""The path of the root directory."""

copy_examples(root=root_path)
run_nbconvert(root=root_path, jupyter=sys.argv[1])
