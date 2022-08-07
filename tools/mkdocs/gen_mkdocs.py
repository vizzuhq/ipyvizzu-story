"""A module for generating mkdocs of ipyvizzu-story."""

import subprocess
import sys
from pathlib import Path
from shutil import copy


def gen_index(root: Path) -> None:
    """
    A method for generating the index file.

    Args:
        root: The path of the root directory.
    """

    index = root / "assets" / "docs" / "index.md"
    copy(root / "README.md", index)

    with open(index, "rt", encoding="utf8") as f_index:
        index_content = f_index.read()

    index_content = index_content.replace(
        "https://vizzuhq.github.io/ipyvizzu-story/", ""
    )

    with open(index, "wt", encoding="utf8") as f_index:
        f_index.write(index_content)


def run_mkdocs(root: Path, mkdocs: str) -> None:
    """
    A method for running mkdocs build.

    Args:
        root: The path of the root directory.
        mkdocs: The path of mkdocs.

    Raises:
        RuntimeError: If mkdocs return code is not 0.
    """

    # pylint: disable=duplicate-code

    command = [
        str(root / mkdocs),
        "build",
        "-f",
        str(root / "tools" / "mkdocs" / "mkdocs.yml"),
        "-d",
        "../../docs",
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


root_path = Path(__file__).parent / ".." / ".."
"""The path of the root directory."""

gen_index(root=root_path)
run_mkdocs(root=root_path, mkdocs=sys.argv[1])
