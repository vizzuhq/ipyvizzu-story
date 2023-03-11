"""A module for working with presentation stories in `Streamlit` environment."""

from typing import Optional

from streamlit.components.v1 import html

from ipyvizzu import Data, Style

from ipyvizzustory.storylib.story import Story as StoryLib


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

    def set_size(  # type: ignore  # pylint: disable=signature-differs
        self, width: int, height: int
    ) -> None:
        """
        A method for overwriting
        [storylib.story.Story.set_size][ipyvizzustory.storylib.story.Story.set_size] method.
        In `Streamlit` environment `width` and `height` must be specified in pixels.

        Args:
            width: Width of the presentation story in pixels.
            height: Height of the presentation story in pixels.

        Raises:
            ValueError: If `width` or `height` is not instance of `int`.
        """

        if any([not isinstance(width, int), not isinstance(height, int)]):
            raise ValueError("width and height should be in pixels as int")
        super().set_size(width=str(width) + "px", height=str(height) + "px")

    def play(self) -> None:
        """A method for displaying the assembled `HTML` code in `Streamlit` environment."""

        html(
            self.to_html(),
            width=int(self._size.width[:-2]),  # type: ignore
            height=int(self._size.height[:-2]),  # type: ignore
        )
