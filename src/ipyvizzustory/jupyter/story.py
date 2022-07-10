"""A module for working with ipyvizzu-story presentations."""

from typing import Optional

from IPython.display import display, HTML

from ipyvizzu import Data, Style

from ipyvizzustory.storylib.story import Story as StoryLib


class Story(StoryLib):
    """A class for representing a presentation story in Jupyter environment."""

    def __init__(self, data: Data, style: Optional[Style] = None):
        super().__init__(data=data, style=style)

    def _repr_html_(self) -> str:
        return self.to_html()

    def play(self) -> None:
        """A method for displaying the html code."""

        html = HTML(self.to_html())
        display(html)
