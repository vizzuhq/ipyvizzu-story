"""A module for working with Vizzu."""

import importlib.metadata
from pathlib import Path
import re


REPO_PATH = Path(__file__).parent / ".." / ".." / ".."
MKDOCS_PATH = REPO_PATH / "tools" / "mkdocs"

IPYVIZZUSTORY_VERSION = ""
IPYVIZZU_VERSION = ""

IPYVIZZUSTORY_SITE_URL = "https://ipyvizzu.vizzuhq.com"
IPYVIZZU_SITE_URL = "https://ipyvizzu-story.vizzuhq.com"


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
    def set_version(content: str, restore: bool = False) -> str:
        """
        A static method for setting vizzu version in content.

        Args:
            content: Content to be modified.
            restore: A flag to restore the content.

        Returns:
            Modified content.
        """

        ipyvizzu_version = Vizzu.get_ipyvizzu_version()
        ipyvizzustory_version = Vizzu.get_ipyvizzustory_version()
        if not restore:
            content = content.replace(
                f"{IPYVIZZUSTORY_SITE_URL}/latest/",
                f"{IPYVIZZUSTORY_SITE_URL}/{ipyvizzustory_version}/",
            )
            content = content.replace(
                f"{IPYVIZZU_SITE_URL}/latest/",
                f"{IPYVIZZU_SITE_URL}/{ipyvizzu_version}/",
            )
        else:
            content = content.replace(
                f"{IPYVIZZUSTORY_SITE_URL}/{ipyvizzustory_version}/",
                f"{IPYVIZZUSTORY_SITE_URL}/latest/",
            )
            content = content.replace(
                f"{IPYVIZZU_SITE_URL}/{ipyvizzu_version}/",
                f"{IPYVIZZU_SITE_URL}/latest/",
            )

        return content
