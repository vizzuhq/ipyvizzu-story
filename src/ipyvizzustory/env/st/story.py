"""A module for working with presentation stories in `Streamlit` environment."""

from typing import Optional, Tuple

from streamlit.components.v1 import html

from ipyvizzu import Data, Style

from ipyvizzustory.storylib.story import StorySize, Story as StoryLib


class Story(StoryLib):
    """A class for representing a presentation story in `Streamlit` environment."""

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

    def _get_width_height(self) -> Tuple[Optional[int], int]:
        if self._size.width == "100%" and StorySize.is_pixel(self._size.height):
            return None, int(float(self._size.height[:-2]))  # type: ignore
        try:
            return self._size.get_width_height_in_pixels()
        except ValueError as error:
            if str(error) == StorySize.ERROR_MSG_WIDTH_AND_HEIGHT:
                raise ValueError(
                    f"{StorySize.ERROR_MSG_WIDTH_AND_HEIGHT} or width should be 100%"
                ) from error
            raise error

    def play(self) -> None:
        """A method for displaying the assembled `HTML` code in `Streamlit` environment."""

        _width, _height = self._get_width_height()

        html(
            self.to_html(),
            width=_width,
            height=_height,
        )
