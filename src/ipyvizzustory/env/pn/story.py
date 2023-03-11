"""A module for working with presentation stories in `Panel` environment."""

from typing import Optional

from panel.pane import HTML

from ipyvizzu import Data, Style

from ipyvizzustory.storylib.story import StorySize, Story as StoryLib


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
        """
        A method for displaying the assembled `HTML` code in `Panel` environment.

        Raises:
            ValueError: If `width` or `height` is not in pixel.
        """

        if any(
            [
                not StorySize.is_pixel(self._size.width),
                not StorySize.is_pixel(self._size.height),
            ]
        ):
            raise ValueError("width and height should be in pixels")

        HTML(
            self.to_html(),
            width=int(self._size.width[:-2]),  # type: ignore
            height=int(self._size.height[:-2]),  # type: ignore
        ).servable()
