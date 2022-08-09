"""A module for generating mkdocs of ipyvizzu-story."""

import subprocess
import sys
from pathlib import Path


def run_mkdocs(mkdocs: str) -> None:
    """
    A method for running mkdocs build.

    Args:
        mkdocs: The path of mkdocs.

    Raises:
        RuntimeError: If mkdocs return code is not 0.
    """

    root = Path(__file__).parent / ".." / ".."

    command = [
        str(root / mkdocs),
        "build",
        "-s",
        "-f",
        str(root / "tools" / "mkdocs" / "mkdocs.yml"),
        "-d",
        "../../site",
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
                f"mkdocs failed {process.returncode} {output_str} {error_str}"
            )


run_mkdocs(mkdocs=sys.argv[1])
