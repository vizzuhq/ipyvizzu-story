"""A module for working with ipyvizzu-story presentations."""

from typing import Optional, Union, List
import json
import uuid

from ipyvizzu import RawJavaScriptEncoder, Data, Style, Config  # , PlainAnimation

from ipyvizzustory.storylib.animation import DataFilter
from ipyvizzustory.storylib.template import (
    VIZZU_STORY,
    DISPLAY_TEMPLATE,
    DISPLAY_INDENT,
)


class Step(dict):
    """A class for representing a step of a slide."""

    def __init__(
        self,
        *animations: Union[Data, Style, Config],
        **anim_options: Optional[Union[str, int, float, dict]],
    ):
        super().__init__()
        if not animations:
            raise ValueError("No animation was set.")
        self._update(*animations)

        if anim_options:
            # self["animOptions"] = PlainAnimation(**anim_options).build()
            raise NotImplementedError("Anim options are not supported.")

    def _update(self, *animations: Union[Data, Style, Config]) -> None:
        for animation in animations:
            if not animation or type(animation) not in [
                Data,
                Style,
                Config,
            ]:  # pylint: disable=unidiomatic-typecheck
                raise TypeError("Type must be Data, Style or Config.")
            if type(animation) == Data:  # pylint: disable=unidiomatic-typecheck
                animation = DataFilter(animation)

            builded_animation = animation.build()
            common_keys = set(builded_animation).intersection(set(self))
            if common_keys:
                raise ValueError(f"Animation is already merged: {common_keys}")
            self.update(builded_animation)


class Slide(list):
    """A class for representing a slide of a story."""

    def __init__(self, step: Optional[Step] = None):
        super().__init__()
        if step:
            self.add_step(step)

    def add_step(self, step: Step) -> None:
        """A method for adding a step for the slide."""

        if not step or type(step) != Step:  # pylint: disable=unidiomatic-typecheck
            raise TypeError("Type must be Step.")
        self.append(step)


class StorySize:
    """A class for representing a story's size."""

    def __init__(self, width: Optional[str] = None, height: Optional[str] = None):
        self._width = width
        self._height = height

        self._style = ""
        if any([width is not None, height is not None]):
            width = "" if width is None else f"width: {width};"
            height = "" if height is None else f"height: {height};"
            self._style = f"vizzuPlayer.style.cssText = '{width}{height}'"

    @property
    def width(self) -> Optional[str]:
        """A property for storing story's width."""

        return self._width

    @property
    def height(self) -> Optional[str]:
        """A property for storing story's height."""

        return self._height

    @property
    def style(self) -> str:
        """A property for storing story's height."""

        return self._style


class Story(dict):
    """A class for representing a presentation story."""

    def __init__(self, data: Data, style: Optional[Style] = None):
        super().__init__()

        self._size: StorySize = StorySize()

        self._features: List[str] = []
        self._events: List[str] = []

        if not data or type(data) != Data:  # pylint: disable=unidiomatic-typecheck
            raise TypeError("Type must be Data.")
        self.update(data.build())

        if style:
            if type(style) != Style:  # pylint: disable=unidiomatic-typecheck
                raise TypeError("Type must be Style.")
            self.update(style.build())

        self["slides"] = []

    def add_slide(self, slide: Slide) -> None:
        """A method for adding a slide for the story."""

        if not slide or type(slide) != Slide:  # pylint: disable=unidiomatic-typecheck
            raise TypeError("Type must be Slide.")
        self["slides"].append(slide)

    def set_feature(self, name: str, enabled: bool) -> None:
        """A method for turning on/off a feature of the story."""
        self._features.append(f"chart.feature('{name}', {json.dumps(enabled)});")

    def add_event(self, event: str, handler: str) -> None:
        """A method for creating and turning on an event handler."""
        self._events.append(
            f"chart.on('{event}', event => {{{' '.join(handler.split())}}});"
        )

    def set_size(
        self, width: Optional[str] = None, height: Optional[str] = None
    ) -> None:
        """A method for setting width/height settings."""

        self._size = StorySize(width=width, height=height)

    def to_html(self) -> str:
        """A method for assembling the html code."""

        vizzu_player_data = f"{json.dumps(self, cls=RawJavaScriptEncoder)}"
        return DISPLAY_TEMPLATE.format(
            id=uuid.uuid4().hex[:7],
            vizzu_story=VIZZU_STORY,
            vizzu_player_data=vizzu_player_data,
            chart_size=self._size.style,
            chart_features=f"\n{DISPLAY_INDENT * 3}".join(self._features),
            chart_events=f"\n{DISPLAY_INDENT * 3}".join(self._events),
        )
