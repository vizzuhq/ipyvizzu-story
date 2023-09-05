"""A module for working with presentation stories."""

from typing import Any, List, Optional, Tuple, Union
from os import PathLike
import json
import re
import uuid

from ipyvizzu import RawJavaScriptEncoder, Data, Style, Config  # , PlainAnimation

from ipyvizzustory.storylib.animation import DataFilter
from ipyvizzustory.storylib.template import (
    VIZZU_STORY,
    DISPLAY_TEMPLATE,
    DISPLAY_INDENT,
)
from ipyvizzustory.__version__ import __version__


class Step(dict):
    """A class for representing a step of a slide."""

    def __init__(
        self,
        *animations: Union[Data, Style, Config],
        **anim_options: Optional[Union[str, int, float, dict]],
    ):
        """
        Step constructor.

        Args:
            *animations: List of [Data][ipyvizzu.Data],
                [Config][ipyvizzu.Config] and [Style][ipyvizzu.Style] objects.
                A `Step` can contain each of the above once.
            **anim_options: Animation options such as duration.

        Raises:
            ValueError: If `animations` are not set.

        Example:
            Initialize a step with a [Config][ipyvizzu.Config] object:

                step = Step(
                    Config({"x": "Foo", "y": "Bar"})
                )
        """

        super().__init__()
        if not animations:
            raise ValueError("No animation was set.")
        self._update(*animations)

        if anim_options:
            self["animOptions"] = anim_options

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
    """A class for representing a slide of a presentation story."""

    def __init__(self, step: Optional[Step] = None):
        """
        Slide constructor.

        Args:
            step: The first step can also be added to the slide in the constructor.

        Example:
            Initialize a slide without step:

                slide = Slide()

            Initialize a slide with a step:

                slide = Slide(
                    Step(
                        Config({"x": "Foo", "y": "Bar"})
                    )
                )
        """

        super().__init__()
        if step:
            self.add_step(step)

    def add_step(self, step: Step) -> None:
        """
        A method for adding a step for the slide.

        Args:
            step: The next step of the slide.

        Raises:
            TypeError: If the type of the `step` is not
                [Step][ipyvizzustory.storylib.story.Step].

        Example:
            Add steps to a slide:

                slide = Slide()
                slide.add_step(
                    Step(
                        Config({"x": "Foo", "y": "Bar"})
                    )
                )
                slide.add_step(
                    Step(
                        Config({"color": "Foo", "x": "Baz", "geometry": "circle"})
                    )
                )
        """

        if not step or type(step) != Step:  # pylint: disable=unidiomatic-typecheck
            raise TypeError("Type must be Step.")
        self.append(step)


class StorySize:
    """A class for representing the size of a presentation story."""

    def __init__(
        self,
        width: Optional[Union[int, float, str]] = None,
        height: Optional[Union[int, float, str]] = None,
        aspect_ratio: Optional[Union[int, float, str]] = None,
    ):
        """
        StorySize constructor.

        Args:
            width: The width of a presentation story.
            height: The height of a presentation story.
            aspect_ratio: The aspect ratio of a presentation story.

        Raises:
            ValueError: If width, height and aspect_ratio are set together.
        """

        width = self._convert_to_pixel_or_return(width)
        height = self._convert_to_pixel_or_return(height)

        self._width = width
        self._height = height
        self._aspect_ratio = aspect_ratio

        self._style = ""
        if None not in [width, height, aspect_ratio]:
            raise ValueError(
                "width, height and aspect ratio cannot be set at the same time"
            )
        if all([height is not None, aspect_ratio is not None]):
            width = "unset"
        if any([width is not None, height is not None, aspect_ratio is not None]):
            _width = "" if width is None else f"width: {width};"
            _height = "" if height is None else f"height: {height};"
            _aspect_ratio = (
                ""
                if aspect_ratio is None
                else f"aspect-ratio: {aspect_ratio} !important;"
            )
            self._style = f"vp.style.cssText = '{_aspect_ratio}{_width}{_height}'"

    @staticmethod
    def _convert_to_pixel_or_return(value: Any) -> Optional[str]:
        if StorySize._is_int(value) or StorySize._is_float(value):
            return str(value) + "px"
        return value

    @staticmethod
    def _is_int(value: Any) -> bool:
        if isinstance(value, int):
            return True
        if isinstance(value, str):
            if re.search(r"^[-+]?[0-9]+$", value):
                return True
        return False

    @staticmethod
    def _is_float(value: Any) -> bool:
        if isinstance(value, float):
            return True
        if isinstance(value, str):
            if re.search(r"^[+-]?[0-9]+\.[0-9]+$", value):
                return True
        return False

    @property
    def width(self) -> Optional[str]:
        """
        A property for storing the width of a presentation story.

        Returns:
            The width of a presentation story.
        """

        return self._width

    @property
    def height(self) -> Optional[str]:
        """
        A property for storing the height of a presentation story.

        Returns:
            The height of a presentation story.
        """

        return self._height

    @property
    def aspect_ratio(self) -> Optional[Union[int, float, str]]:
        """
        A property for storing the aspect ratio of a presentation story.

        Returns:
            The aspect ratio of a presentation story.
        """

        return self._aspect_ratio

    @property
    def style(self) -> str:
        """
        A property for storing the style of a presentation story.

        Note:
            If neither `width`, `height` nor `aspect_ratio` is set, it returns an empty string.

        Returns:
            The cssText width and height of a presentation story.
        """

        return self._style

    @staticmethod
    def is_pixel(value: Any) -> bool:
        """
        A static method for checking the type of the given value.

        Args:
            value: The value to check.

        Returns:
            `True` if the value is pixel, `False` otherwise.
        """

        if StorySize._is_int(value) or StorySize._is_float(value):
            return True
        if isinstance(value, str) and value.endswith("px"):
            if StorySize._is_int(value[0:-2]) or StorySize._is_float(value[0:-2]):
                return True
        return False

    def get_width_height_in_pixels(self) -> Tuple[int, int]:
        """
        A method for returning the width and height in pixels.

        Raises:
            ValueError: If width and height are not in pixels when aspect_ratio is not set.
            ValueError: If width or height is not in pixel when aspect_ratio is set.
            ValueError: If aspect_ratio is not a float when aspect_ratio is set.

        Returns:
            The width and height in pixels as int.
        """

        if self.aspect_ratio is None:
            if any(
                [
                    not StorySize.is_pixel(self.width),
                    not StorySize.is_pixel(self.height),
                ]
            ):
                raise ValueError("width and height should be in pixels")
            _width = int(float(self.width[:-2]))  # type: ignore
            _height = int(float(self.height[:-2]))  # type: ignore
        else:
            if not any(
                [
                    StorySize._is_int(self.aspect_ratio),
                    StorySize._is_float(self.aspect_ratio),
                ]
            ):
                raise ValueError("aspect_ratio should be a float")
            if not any(
                [StorySize.is_pixel(self.width), StorySize.is_pixel(self.height)]
            ):
                raise ValueError("width or height should be in pixels")
            _aspect_ratio = float(self.aspect_ratio)
            if StorySize.is_pixel(self.width):
                _width = float(self.width[:-2])  # type: ignore
                _height = int(_width / _aspect_ratio)
                _width = int(_width)
            else:
                _height = float(self.height[:-2])  # type: ignore
                _width = int(_height * _aspect_ratio)
                _height = int(_height)
        return (_width, _height)


class Story(dict):
    """A class for representing a presentation story."""

    # pylint: disable=too-many-instance-attributes

    def __init__(self, data: Data, style: Optional[Style] = None):
        """
        Presentation Story constructor.

        Args:
            data: Data set for the whole presentation story.
                After initialization `data` can not be modified,
                but it can be filtered.
            style: Style settings for the presentation story.
                `style` can be changed at each presentation step.

        Raises:
            TypeError: If the type of the `data` is not `ipyvizzu.Data`.
            TypeError: If the type of the `style` is not `ipyvizzu.Style`.

        Example:
            Initialize a story with data and without style:

                data = Data()
                data.add_series("Foo", ["Alice", "Bob", "Ted"])
                data.add_series("Bar", [15, 32, 12])
                data.add_series("Baz", [5, 3, 2])

                story = Story(data=data)
        """

        super().__init__()

        self._analytics = True
        self._vizzu: Optional[str] = None
        self._vizzu_story: str = VIZZU_STORY
        self._start_slide: Optional[int] = None

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

    @property
    def analytics(self) -> bool:
        """
        A property for enabling/disabling the usage statistics feature.

        The usage statistics feature allows aggregate usage data collection
        using Plausible's algorithm.
        Enabling this feature helps us follow the progress and overall trends of our library,
        allowing us to focus our resources effectively and better serve our users.

        We do not track, collect, or store any personal data or personally identifiable information.
        All data is isolated to a single day, a single site, and a single device only.

        Please note that even when this feature is enabled,
        publishing anything made with `ipyvizzu-story` remains GDPR compatible.

        Returns:
            The value of the property (default `True`).
        """

        return self._analytics

    @analytics.setter
    def analytics(self, analytics: Optional[bool]):
        self._analytics = bool(analytics)

    @property
    def vizzu(self) -> Optional[str]:
        """
        A property for changing `vizzu` url.

        Note:
            If `None`, vizzu url is set by `vizzu-story`.

        Returns:
            `Vizzu` url.
        """

        return self._vizzu

    @vizzu.setter
    def vizzu(self, url: str) -> None:
        self._vizzu = url

    @property
    def vizzu_story(self) -> str:
        """
        A property for changing `vizzu-story` url.

        Returns:
            `Vizzu-story` url.
        """

        return self._vizzu_story

    @vizzu_story.setter
    def vizzu_story(self, url: str) -> None:
        self._vizzu_story = url

    @property
    def start_slide(self) -> Optional[int]:
        """
        A property for setting the starter slide.

        Returns:
            Number of the starter slide.
        """

        return self._start_slide

    @start_slide.setter
    def start_slide(self, number: int) -> None:
        self._start_slide = number

    def add_slide(self, slide: Slide) -> None:
        """
        A method for adding a slide for the story.

        Args:
            slide: The next slide of the story.

        Raises:
            TypeError: If the type of the `slide` is not
                [Slide][ipyvizzustory.storylib.story.Slide].

        Example:
            Add a slide to the story:

                story.add_slide(
                    Slide(
                        Step(
                            Config({"x": "Foo", "y": "Bar"})
                        )
                    )
                )
        """

        if not slide or type(slide) != Slide:  # pylint: disable=unidiomatic-typecheck
            raise TypeError("Type must be Slide.")
        self["slides"].append(slide)

    def set_feature(self, name: str, enabled: bool) -> None:
        """
        A method for enabling or disabling a feature of the story.

        Args:
            name: The name of the feature.
            enabled: `True` if enabled or `False` if disabled.

        Example:
            Set a feature of the story, for example enable the tooltip:

                story.set_feature("tooltip", True)
        """

        self._features.append(f"chart.feature('{name}', {json.dumps(enabled)});")

    def add_event(self, event: str, handler: str) -> None:
        """
        A method for creating and turning on an event handler.

        Args:
            event: The type of the event.
            handler: The handler `JavaScript` expression as string.

        Example:
            Add an event handler to the story:

                story.add_event("click", "alert(JSON.stringify(event.data));")
        """

        self._events.append(
            f"chart.on('{event}', event => {{{' '.join(handler.split())}}});"
        )

    def set_size(
        self,
        width: Optional[Union[int, float, str]] = None,
        height: Optional[Union[int, float, str]] = None,
        aspect_ratio: Optional[Union[int, float, str]] = None,
    ) -> None:
        """
        A method for setting width/height settings.

        Args:
            width: The width of the presentation story.
            height: The height of the presentation story.
            aspect_ratio: The aspect ratio of the presentation story.

        Example:
            Change the size of the story:

                story.set_size("100%", "400px")
        """

        self._size = StorySize(width=width, height=height, aspect_ratio=aspect_ratio)

    def _repr_html_(self) -> str:
        return self.to_html()

    def to_html(self) -> str:
        """
        A method for assembling the `HTML` code.

        Returns:
            The assembled `HTML` code as string.
        """

        vizzu_player_data = f"{json.dumps(self, cls=RawJavaScriptEncoder)}"
        return DISPLAY_TEMPLATE.format(
            id=uuid.uuid4().hex[:7],
            version=__version__,
            analytics=str(self._analytics).lower(),
            vizzu=f'vizzu-url="{self._vizzu}"' if self._vizzu else "",
            vizzu_story=self._vizzu_story,
            vizzu_player_data=vizzu_player_data,
            start_slide=f'start-slide="{self._start_slide}"'
            if self._start_slide
            else "",
            chart_size=self._size.style,
            chart_features=f"\n{DISPLAY_INDENT * 3}".join(self._features),
            chart_events=f"\n{DISPLAY_INDENT * 3}".join(self._events),
        )

    def export_to_html(self, filename: PathLike) -> None:
        """
        A method for exporting the story into `HTML` file.

        Args:
            filename: The path of the target `HTML` file.
        """

        with open(filename, "w", encoding="utf8") as file_desc:
            file_desc.write(self.to_html())
