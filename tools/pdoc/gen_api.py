"""A module for generating api of ipyvizzu-story."""

import subprocess
import os
import sys
from pathlib import Path


def run_pdoc(root: Path, pdoc: str) -> None:
    """
    A method for running pdoc.

    Args:
        root: The path of the root directory.
        pdoc: The path of pdoc.

    Raises:
        RuntimeError: If pdoc return code is not 0.
    """

    # pylint: disable=duplicate-code

    command = [
        str(root / pdoc),
        "-t",
        str(root / "tools" / "pdoc"),
        "--docformat",
        "google",
        str(root / "src" / "ipyvizzustory"),
        "-o",
        str(root / "docs" / "api"),
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
                f"pdoc failed {process.returncode} {output_str} {error_str}"
            )

    os.remove(root / "docs" / "api" / "index.html")


root_path = Path(__file__).parent / ".." / ".."
"""The path of the root directory."""

run_pdoc(root=root_path, pdoc=sys.argv[1])
