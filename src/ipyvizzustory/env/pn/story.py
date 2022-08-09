"""A module for working with presentation stories in Panel environment."""

from typing import Optional

import panel as pn
from panel.pane import HTML

from ipyvizzu import Data, Style

from ipyvizzustory.storylib.story import Story as StoryLib


class Story(StoryLib):
    """A class for representing a presentation story in Panel environment."""

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

    def play(self, width: int = 800, height: int = 480) -> None:
        """
        A method for displaying the assembled html code in Panel environment.

        Args:
            width: Width of the presentation story in pixels.
            height: Height of the presentation story in pixels.

        Raises:
            ValueError: If size is already set.
            ValueError: If `width` or `height` is not instance of `int`.
        """

        if self._size.style:
            raise ValueError("size is already set")

        if any([not isinstance(width, int), not isinstance(height, int)]):
            raise ValueError("width and height should be in pixels as int")

        self.set_size(width=str(width) + "px", height=str(height) + "px")

        pn.extension(sizing_mode="stretch_width", template="fast")

        pn.state.template.param.update(  # type: ignore
            title="ipyvizzu-story",
        )

        HTML(self.to_html(), height=height + 10, sizing_mode="stretch_both").servable()
