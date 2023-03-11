"""A module for working with presentation stories in `Python` environment."""

from typing import Optional

from ipyvizzu import Data, Style

from ipyvizzustory.storylib.story import Story as StoryLib


class Story(StoryLib):
    """A class for representing a presentation story in `Python` environment."""

    def __init__(self, data: Data, style: Optional[Style] = None):
        """
        Presentation Story constructor.

        Args:
            data: Data set for the whole presentation story.
                After initialization `data` can not be modified,
                but it can be filtered.
            style: Style settings for the presentation story.
                `style` can be changed at each presentation step.
        """

        super().__init__(data=data, style=style)

    def play(self) -> str:
        """
        A method for returning the assembled `HTML` code in `Python` environment.

        Returns:
            The assembled `HTML` code as string.
        """

        return self.to_html()
