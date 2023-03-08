"""A module for working with Vizzu."""

import importlib.metadata
from pathlib import Path
import re


REPO_PATH = Path(__file__).parent / ".." / ".." / ".."
MKDOCS_PATH = REPO_PATH / "tools" / "mkdocs"

IPYVIZZUSTORY_VERSION = ""
IPYVIZZU_VERSION = ""


class Vizzu:
    """A class for working with Vizzu."""

    @staticmethod
    def get_ipyvizzustory_version() -> str:
        """
        A static method for returning ipyvizzu-story major.minor version.

        Returns:
            ipyvizzu-story major.minor version.
        """

        if IPYVIZZUSTORY_VERSION:
            return IPYVIZZUSTORY_VERSION
        with open(
            REPO_PATH / "setup.py",
            "r",
            encoding="utf8",
        ) as f_version:
            content = f_version.read()
            version = re.search(r"version=\"(\d+).(\d+).(\d+)\"", content)
            return f"{version.group(1)}.{version.group(2)}"  # type: ignore

    @staticmethod
    def get_ipyvizzu_version() -> str:
        """
        A static method for returning ipyvizzu major.minor version.

        Returns:
            ipyvizzu major.minor version.
        """

        if IPYVIZZU_VERSION:
            return IPYVIZZU_VERSION
        metadata = importlib.metadata.version("ipyvizzu")
        version = re.search(r"(\d+).(\d+).(\d+)", metadata)
        return f"{version.group(1)}.{version.group(2)}"  # type: ignore

    @staticmethod
    def set_version(content: str) -> str:
        """
        A static method for setting vizzu version in content.

        Args:
            content: Content to be modified.

        Returns:
            Modified content.
        """

        ipyvizzu_version = Vizzu.get_ipyvizzu_version()
        ipyvizzustory_version = Vizzu.get_ipyvizzustory_version()
        content = content.replace(
            "https://ipyvizzu-story.vizzuhq.com/latest/",
            f"https://ipyvizzu-story.vizzuhq.com/{ipyvizzustory_version}/",
        )
        content = content.replace(
            "https://ipyvizzu.vizzuhq.com/latest/",
            f"https://ipyvizzu.vizzuhq.com/{ipyvizzu_version}/",
        )

        return content
