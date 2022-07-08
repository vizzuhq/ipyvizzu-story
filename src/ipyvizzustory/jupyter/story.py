"""A module for working with ipyvizzu-story presentations."""

from typing import Optional
import json
import uuid

from ipyvizzu import Data, Style, RawJavaScriptEncoder

from ipyvizzustory.storylib.story import Story as StoryLib


class Story(StoryLib):
    """A class for representing a presentation story in Jupyter environment."""

    def __init__(self, data: Data, style: Optional[Style] = None):
        super().__init__(data=data, style=style)

        self._id = uuid.uuid4().hex[:7]
        self._played = False

    def _repr_html_(self) -> str:
        assert not self._played, "cannot be used after story played."
        self._played = True
        vpd = f"{json.dumps(self, cls=RawJavaScriptEncoder)}"
        print(vpd)
        return f'<div id="{self._id}"><script>console.log({vpd})</script></div>'
