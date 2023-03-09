"""A module for generating notebooks."""

from pathlib import Path
import sys
import re

import mkdocs_gen_files  # type: ignore


REPO_PATH = Path(__file__).parent / ".." / ".." / ".."
MKDOCS_PATH = REPO_PATH / "tools" / "mkdocs"

sys.path.insert(0, str(MKDOCS_PATH / "modules"))

from context import (  # pylint: disable=import-error, wrong-import-position, wrong-import-order
    chdir,
)
from vizzu import (  # pylint: disable=import-error, wrong-import-position, wrong-import-order
    Vizzu,
)


class Notebook:
    """A class for generating notebooks."""

    # pylint: disable=too-few-public-methods

    CSV = re.compile(r"(.*)(\.\/)(.*)(\.csv)(.*)")

    @staticmethod
    def _replace_csv_url(match_obj) -> str:
        url = f"https://ipyvizzu-story.vizzuhq.com/{Vizzu.get_ipyvizzustory_version()}/"
        before = match_obj.group(1)
        example = match_obj.group(3)
        after = match_obj.group(5)
        new_string = f"{before}{url}{example}.csv{after}"
        return new_string

    @staticmethod
    def generate_shareable() -> None:
        """A method for generating shareable notebooks."""

        example_path = REPO_PATH / "docs" / "examples"
        for path in example_path.glob("*.ipynb"):
            with open(path, "rt", encoding="utf8") as f_src:
                content = f_src.read()
                content = re.sub(Notebook.CSV, Notebook._replace_csv_url, content)
                with mkdocs_gen_files.open(
                    f"examples/{path.stem}/{path.stem}_share.ipynb", "w"
                ) as f_dst:
                    f_dst.write(content)

    @staticmethod
    def generate_csv_url_script(file: str) -> None:
        """
        A method for generating an external JavaScript file that sets csv urls.

        Args:
            file: The destination file.
        """

        # pylint: disable=anomalous-backslash-in-string

        with mkdocs_gen_files.open(file, "w") as f_js:
            ipyvizzustory_version = Vizzu.get_ipyvizzustory_version()
            f_js.write(
                f"""
document.addEventListener("DOMContentLoaded", (event) => {{
  if (window.location.href.includes("/examples/")) {{
    const elements = document.getElementsByClassName("highlight-ipynb");
    const regex = /(".\/)(.*)(.csv")/g;
    for (let i = 0; i < elements.length; i++) {{
      elements[i].innerHTML = elements[i].innerHTML.replace(
        regex,
        '"https://ipyvizzu-story.vizzuhq.com/{ipyvizzustory_version}/$2$3'
      );
    }}
  }}
}});
            """
            )


def main() -> None:
    """
    The main method.
    It prepares files for the documentation site.
    """

    with chdir(REPO_PATH):
        Notebook.generate_shareable()
        Notebook.generate_csv_url_script("assets/javascripts/notebooklinks.js")


main()
