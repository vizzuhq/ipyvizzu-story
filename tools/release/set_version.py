"""A module for setting versions before release."""

import json
from pathlib import Path
import sys


REPO_PATH = Path(__file__).parent / ".." / ".."
MKDOCS_PATH = REPO_PATH / "tools" / "mkdocs"


sys.path.insert(0, str(MKDOCS_PATH / "modules"))

from context import (  # pylint: disable=import-error, wrong-import-position, wrong-import-order
    chdir,
)
from vizzu import (  # pylint: disable=import-error, wrong-import-position, wrong-import-order
    Vizzu,
)


class Version:
    """A class for setting versions before release."""

    # pylint: disable=too-few-public-methods

    @staticmethod
    def set_readme_version(restore: bool) -> None:
        """
        A method for setting versions in readme.

        Args:
            restore: A flag to restore the content.
        """

        with open("README.md", "r", encoding="utf8") as fh_readme:
            content = fh_readme.read()

        content = Vizzu.set_version(content, restore)

        with open("README.md", "w", encoding="utf8") as fh_readme:
            fh_readme.write(content)


def main() -> None:
    """
    The main method.
    It set versions before release.
    """

    with chdir(REPO_PATH):
        restore = json.loads(sys.argv[1].lower())
        Version.set_readme_version(restore)


main()
