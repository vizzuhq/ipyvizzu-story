"""A module for generating navigation of the site."""

from pathlib import Path
import json

import mkdocs_gen_files  # type: ignore


def gen_toc_nav(root: Path) -> None:
    """
    A method for generating navigation of the table of content.

    Args:
        root: The path of the root directory.
    """

    mkdocs = root / "tools" / "mkdocs"

    with open(mkdocs / "toc.json", encoding="utf8") as f_json:
        toc = json.load(f_json)
        for item in toc:
            nav[item["nav"]] = item["md"]


def gen_api_nav(root: Path) -> None:
    """
    A method for generating navigation of the generated api documentation.

    Args:
        root: The path of the root directory.
    """

    api = root / "docs" / "api"

    for html in api.glob("**/*.html"):
        with open(html, encoding="utf8") as f_html:
            content = f_html.read()
            with mkdocs_gen_files.open(
                html.relative_to(api).with_suffix(".md"), "w"
            ) as f_md:
                print(content, file=f_md)
                parts = str(html.with_suffix("")).split("/")
                parts = parts[6:]
                parts.insert(0, "API")
                nav[parts] = html.relative_to(api).with_suffix(".md")


def write_nav() -> None:
    """A method for writing navigation into toc.md."""

    with mkdocs_gen_files.open("toc.md", "w") as f_nav:
        f_nav.writelines(nav.build_literate_nav())


root_path = Path(__file__).parent / ".." / ".."
"""The path of the root directory."""

nav = mkdocs_gen_files.Nav()
"""Mkdocs navigation object."""

gen_toc_nav(root=root_path)
gen_api_nav(root=root_path)
write_nav()
