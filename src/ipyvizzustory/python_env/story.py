"""A module for working with ipyvizzu-story presentations."""

from typing import Optional

from ipyvizzu import Data, Style

from ipyvizzustory.storylib.story import Story as StoryLib


class Story(StoryLib):
    """A class for representing a presentation story in Python environment."""

    def __init__(self, data: Data, style: Optional[Style] = None):
        super().__init__(data=data, style=style)

    def play(self) -> str:
        """A method for displaying the html code."""

        return self.to_html()
