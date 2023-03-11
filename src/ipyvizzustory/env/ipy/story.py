"""A module for working with presentation stories in `Jupyter`/`IPython` environment."""

from typing import Optional

from IPython.display import display as display_html, HTML  # type: ignore

from ipyvizzu import Data, Style

from ipyvizzustory.storylib.story import Story as StoryLib


class Story(StoryLib):
    """A class for representing a presentation story in `Jupyter`/`IPython` environment."""

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

    def play(self) -> None:
        """A method for displaying the assembled `HTML` code in `Jupyter`/`IPython` environment."""

        display_html(HTML(self.to_html()))
