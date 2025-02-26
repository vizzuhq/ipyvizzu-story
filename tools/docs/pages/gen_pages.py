# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring

from contextlib import chdir
import os
from pathlib import Path
from typing import Union, Optional, List
import sys

import mkdocs_gen_files  # type: ignore


REPO_PATH = Path(__file__).parent / ".." / ".." / ".."
TOOLS_PATH = REPO_PATH / "tools"
MKDOCS_PATH = TOOLS_PATH / "docs"

sys.path.insert(0, str(TOOLS_PATH / "modules"))
sys.path.insert(0, str(TOOLS_PATH / "ci"))
sys.path.insert(0, str(MKDOCS_PATH))

from vizzu import (  # pylint: disable=import-error, wrong-import-position, wrong-import-order
    Vizzu,
)
from markdown_format import (  # pylint: disable=import-error, wrong-import-position, wrong-import-order
    Markdown,
)
from config import (  # pylint: disable=import-error, wrong-import-position, wrong-import-order
    MkdocsConfig,
)


class IndexPages:
    # pylint: disable=too-few-public-methods

    @staticmethod
    def _write_index_file(file: str, toc: list) -> None:
        for item in toc:
            if isinstance(item, str):
                IndexPages._write_str_index(file, item)
            elif isinstance(item, dict):
                IndexPages._write_dict_index(file, item)
            else:
                raise NotImplementedError(f"{item}")

    @staticmethod
    def _write_str_index(file: str, item: str) -> None:
        with mkdocs_gen_files.open(file, "a") as f_index:
            parts = item.split("/")
            part = parts[-1].replace(".md", "").capitalize()
            link = Path(os.path.relpath(item, Path(file).parent))
            f_index.write(f"* [{part}]({link})\n")

    @staticmethod
    def _write_dict_index(file: str, item: dict) -> None:
        with mkdocs_gen_files.open(file, "a") as f_index:
            for key in item:
                if isinstance(item[key], str):
                    link = Path(os.path.relpath(item[key], Path(file).parent))
                    f_index.write(f"* [{key}]({link})\n")
                    continue
                if item[key] and isinstance(item[key], list):
                    if isinstance(item[key][0], str):
                        if item[key][0].endswith("index.md"):
                            link = Path(
                                os.path.relpath(item[key][0], Path(file).parent)
                            )
                            f_index.write(f"* [{key}]({link})\n")
                            continue
                raise NotImplementedError(f"{item}")

    @staticmethod
    def generate(
        nav_item: Union[list, dict, str], skip: Optional[List[str]] = None
    ) -> None:
        if isinstance(nav_item, list):
            if (
                nav_item
                and isinstance(nav_item[0], str)
                and nav_item[0].endswith("index.md")
            ):
                if not skip or nav_item[0] not in skip:
                    original = Path("docs", nav_item[0])
                    if original.exists():
                        mkdocs_gen_files.set_edit_path(nav_item[0], nav_item[0])
                    with mkdocs_gen_files.open(nav_item[0], "a") as f_index:
                        f_index.write("\n")
                    IndexPages._write_index_file(file=nav_item[0], toc=nav_item[1:])
            for item in nav_item:
                IndexPages.generate(nav_item=item, skip=skip)
        elif isinstance(nav_item, dict):
            for key in nav_item:
                IndexPages.generate(nav_item=nav_item[key], skip=skip)


class Page:
    # pylint: disable=too-few-public-methods

    @staticmethod
    def generate(src: Path, dst: str, pos: str, site: str, keep: bool = False) -> None:
        with open(src, "rt", encoding="utf8") as f_src:
            content = f_src.read()

        content = content.replace(f"{site}/latest/", pos).replace(f"{site}/latest", pos)
        content = Vizzu.set_version(content)
        if keep:
            content = f"<pre>{content}</pre>"

        mkdocs_gen_files.set_edit_path(dst, ".." / Path(dst).parent / Path(src).name)
        with mkdocs_gen_files.open(dst, "w") as f_dst:
            f_dst.write(content)


class Docs:
    # pylint: disable=too-few-public-methods

    @staticmethod
    def generate(skip: Optional[List[str]] = None) -> None:
        docs_path = REPO_PATH / "docs"
        for path in list(docs_path.rglob("*.md")) + list(docs_path.rglob("*.js")):
            if skip and path.name in skip:
                continue
            with open(path, "rt", encoding="utf8") as f_src:
                dst = path.relative_to(docs_path)
                content = f_src.read()
                if path.suffix == ".md":
                    content = Vizzu.set_version(content)
                    content = Markdown.format(content)
                    mkdocs_gen_files.set_edit_path(dst, dst)
                with mkdocs_gen_files.open(dst, "w") as f_dst:
                    f_dst.write(content)


def main() -> None:
    with chdir(REPO_PATH):
        config = MkdocsConfig.load(MKDOCS_PATH / "mkdocs.yml")

        Docs.generate()

        IndexPages.generate(nav_item=config["nav"])

        Page.generate(
            src=REPO_PATH / "README.md",
            dst="index.md",
            pos="./",
            site=config["site_url"],
        )

        Page.generate(
            src=REPO_PATH / "CONTRIBUTING.md",
            dst="CONTRIBUTING.md",
            pos="../",
            site=config["site_url"],
        )

        Page.generate(
            src=REPO_PATH / "CODE_OF_CONDUCT.md",
            dst="CODE_OF_CONDUCT.md",
            pos="../",
            site=config["site_url"],
        )

        Page.generate(
            src=REPO_PATH / "LICENSE",
            dst="LICENSE.md",
            pos="../",
            site=config["site_url"],
            keep=True,
        )


main()
