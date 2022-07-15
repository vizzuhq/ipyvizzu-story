"""A module for working with ipyvizzu-story presentations."""

from typing import Optional

from streamlit.components.v1 import html

from ipyvizzu import Data, Style

from ipyvizzustory.storylib.story import Story as StoryLib


class Story(StoryLib):
    """A class for representing a presentation story in Streamlit environment."""

    def __init__(self, data: Data, style: Optional[Style] = None):
        super().__init__(data=data, style=style)
        self.set_size(800, 480)

    def set_size(  # type: ignore  # pylint: disable=signature-differs
        self, width: int, height: int
    ) -> None:
        """A method for overwriting StoryLib().set_size() method."""

        if any([not isinstance(width, int), not isinstance(height, int)]):
            raise ValueError("width and height should be in pixels as int")
        super().set_size(width=str(width) + "px", height=str(height) + "px")

    def play(self) -> None:
        """A method for displaying the html code."""

        html(
            self.to_html(),
            width=int(self._size.width[:-2]),  # type: ignore
            height=int(self._size.height[:-2]),  # type: ignore
        )
