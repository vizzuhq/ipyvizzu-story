# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring

import importlib.metadata
from pathlib import Path
import re
import requests

import ipyvizzustory

from ipyvizzustory.storylib.template import VIZZU_STORY


REPO_PATH = Path(__file__).parent / ".." / ".."

IPYVIZZUSTORY_VERSION = ""
VIZZUSTORY_VERSION = ""
IPYVIZZU_VERSION = ""
VIZZU_VERSION = ""

IPYVIZZUSTORY_SITE_URL = "https://ipyvizzu-story.vizzuhq.com"
VIZZUSTORY_SITE_URL = "https://vizzu-story.vizzuhq.com"
IPYVIZZU_SITE_URL = "https://ipyvizzu.vizzuhq.com"
VIZZU_SITE_URL = "https://lib.vizzuhq.com"

VIZZUSTORY_CDN_URL = "https://cdn.jsdelivr.net/npm/vizzu-story"


class Vizzu:
    _ipyvizzustory_version = ""
    _vizzustory_version = ""
    _ipyvizzu_version = ""
    _vizzu_version = ""

    @staticmethod
    def get_ipyvizzustory_version() -> str:
        if IPYVIZZUSTORY_VERSION:
            return IPYVIZZUSTORY_VERSION
        if not Vizzu._ipyvizzustory_version:
            version = ipyvizzustory.__version__
            Vizzu._ipyvizzu_version = re.search(r"(\d+.\d+).\d+", version).group(1)  # type: ignore
        return Vizzu._ipyvizzustory_version

    @staticmethod
    def get_vizzustory_version() -> str:
        if VIZZUSTORY_VERSION:
            return VIZZUSTORY_VERSION
        if not Vizzu._vizzustory_version:
            version = re.search(r"vizzu-story@(\d+).(\d+)/", VIZZU_STORY)
            Vizzu._vizzustory_version = f"{version.group(1)}.{version.group(2)}"  # type: ignore
        return Vizzu._vizzustory_version

    @staticmethod
    def get_ipyvizzu_version() -> str:
        if IPYVIZZU_VERSION:
            return IPYVIZZU_VERSION
        if not Vizzu._ipyvizzu_version:
            metadata = importlib.metadata.version("ipyvizzu")
            version = re.search(r"(\d+).(\d+).(\d+)", metadata)
            Vizzu._ipyvizzu_version = f"{version.group(1)}.{version.group(2)}"  # type: ignore
        return Vizzu._ipyvizzu_version

    @staticmethod
    def get_vizzu_version() -> str:
        if VIZZU_VERSION:
            return VIZZU_VERSION
        if not Vizzu._vizzu_version:
            vizzustory_version = Vizzu.get_vizzustory_version()
            response = requests.get(
                f"{VIZZUSTORY_CDN_URL}@{vizzustory_version}/package.json", timeout=10
            )
            content = response.content.decode("utf-8")
            version = re.search(r"\"vizzu\": \"~(\d+).(\d+).(\d+)\"", content)
            Vizzu._vizzu_version = f"{version.group(1)}.{version.group(2)}"  # type: ignore
        return Vizzu._vizzu_version

    @staticmethod
    def set_version(content: str, restore: bool = False) -> str:
        ipyvizzu_version = Vizzu.get_ipyvizzu_version()
        vizzustory_version = Vizzu.get_vizzustory_version()
        ipyvizzustory_version = Vizzu.get_ipyvizzustory_version()
        vizzu_version = Vizzu.get_vizzu_version()
        if not restore:
            content = content.replace(
                f"{IPYVIZZUSTORY_SITE_URL}/latest/",
                f"{IPYVIZZUSTORY_SITE_URL}/{ipyvizzustory_version}/",
            )
            content = content.replace(
                f"{VIZZUSTORY_SITE_URL}/latest/",
                f"{VIZZUSTORY_SITE_URL}/{vizzustory_version}/",
            )
            content = content.replace(
                f"{IPYVIZZUSTORY_SITE_URL}/latest/",
                f"{IPYVIZZUSTORY_SITE_URL}/{ipyvizzustory_version}/",
            )
            content = content.replace(
                f"{VIZZUSTORY_CDN_URL}@latest/dist/vizzu-story.min.js",
                f"{VIZZUSTORY_CDN_URL}@{vizzustory_version}/dist/vizzu-story.min.js",
            )
            content = content.replace(
                f"{IPYVIZZU_SITE_URL}/latest/",
                f"{IPYVIZZU_SITE_URL}/{ipyvizzu_version}/",
            )
            content = content.replace(
                f"{VIZZU_SITE_URL}/latest/",
                f"{VIZZU_SITE_URL}/{vizzu_version}/",
            )
        else:
            content = content.replace(
                f"{IPYVIZZUSTORY_SITE_URL}/{ipyvizzustory_version}/",
                f"{IPYVIZZUSTORY_SITE_URL}/latest/",
            )
            content = content.replace(
                f"{VIZZUSTORY_SITE_URL}/{vizzustory_version}/",
                f"{VIZZUSTORY_SITE_URL}/latest/",
            )
            content = content.replace(
                f"{VIZZUSTORY_CDN_URL}@{vizzustory_version}/dist/vizzu-story.min.js",
                f"{VIZZUSTORY_CDN_URL}@latest/dist/vizzu-story.min.js",
            )
            content = content.replace(
                f"{IPYVIZZU_SITE_URL}/{ipyvizzu_version}/",
                f"{IPYVIZZU_SITE_URL}/latest/",
            )
            content = content.replace(
                f"{VIZZU_SITE_URL}/{vizzu_version}/",
                f"{VIZZU_SITE_URL}/latest/",
            )

        return content
