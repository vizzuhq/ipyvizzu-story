# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring

from pathlib import Path
from subprocess import Popen
import sys


REPO_PATH = Path(__file__).parent / ".." / ".."
TOOLS_PATH = REPO_PATH / "tools"
MKDOCS_PATH = TOOLS_PATH / "docs"

sys.path.insert(0, str(TOOLS_PATH / "modules"))

from chdir import (  # pylint: disable=import-error, wrong-import-position, wrong-import-order
    chdir,
)
from vizzu import (  # pylint: disable=import-error, wrong-import-position, wrong-import-order
    Vizzu,
    IPYVIZZU_SITE_URL,
)


class Deploy:
    latest: bool = True

    @staticmethod
    def mike() -> None:
        version = Vizzu.get_ipyvizzustory_version()

        params = [
            "mike",
            "deploy",
        ]
        if Deploy.latest:
            params.append("-u")
        params.append(version)
        if Deploy.latest:
            params.append("latest")
        params.append("-F")
        params.append("tools/docs/mkdocs.yml")

        with Popen(
            params,
        ) as process:
            process.communicate()

        if process.returncode:
            raise RuntimeError("failed to run mike")

    @staticmethod
    def set_config(restore: bool) -> None:
        ipyvizzu_version = Vizzu.get_ipyvizzu_version()

        with open(MKDOCS_PATH / "mkdocs.yml", "r", encoding="utf8") as fh_readme:
            content = fh_readme.read()

        if not restore:
            content = content.replace(
                f"{IPYVIZZU_SITE_URL}/latest/objects.inv",
                f"{IPYVIZZU_SITE_URL}/{ipyvizzu_version}/objects.inv",
            )

            if not Deploy.latest:
                content = content.replace(
                    "- content.action.edit",
                    "# - content.action.edit",
                )
        else:
            content = content.replace(
                f"{IPYVIZZU_SITE_URL}/{ipyvizzu_version}/objects.inv",
                f"{IPYVIZZU_SITE_URL}/latest/objects.inv",
            )

            if not Deploy.latest:
                content = content.replace(
                    "# - content.action.edit",
                    "- content.action.edit",
                )

        with open(MKDOCS_PATH / "mkdocs.yml", "w", encoding="utf8") as fh_readme:
            fh_readme.write(content)


def main() -> None:
    with chdir(REPO_PATH):
        Deploy.set_config(restore=False)
        Deploy.mike()
        Deploy.set_config(restore=True)


main()
