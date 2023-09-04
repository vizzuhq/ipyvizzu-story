"""A module for working with presentation stories in `Panel` environment."""

from typing import Optional

from panel.pane import HTML

from ipyvizzu import Data, Style

from ipyvizzustory.storylib.story import Story as StoryLib


class Story(StoryLib):
    """A class for representing a presentation story in `Panel` environment."""

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
        """A method for displaying the assembled `HTML` code in `Panel` environment."""

        _width, _height = self._size.get_width_height_in_pixels()

        HTML(
            self.to_html(),
            width=_width,
            height=_height,
        ).servable()
