# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring

from contextlib import chdir
import json
from pathlib import Path
import sys


REPO_PATH = Path(__file__).parent / ".." / ".."
TOOLS_PATH = REPO_PATH / "tools"

sys.path.insert(0, str(TOOLS_PATH / "modules"))

from vizzu import (  # pylint: disable=import-error, wrong-import-position, wrong-import-order
    Vizzu,
)


class Version:
    # pylint: disable=too-few-public-methods

    @staticmethod
    def set_readme_version(restore: bool) -> None:
        with open("README.md", "r", encoding="utf8") as fh_readme:
            content = fh_readme.read()

        content = Vizzu.set_version(content, restore)

        with open("README.md", "w", encoding="utf8") as fh_readme:
            fh_readme.write(content)


def main() -> None:
    with chdir(REPO_PATH):
        restore = json.loads(sys.argv[1].lower())
        Version.set_readme_version(restore)


main()
