"""A module for working with ipyvizzu-story presentations."""

from typing import Optional, Union

from ipyvizzu import Data, Style, Config  # , PlainAnimation

from ipyvizzustory.storylib.animation import DataFilter


class Step(dict):
    """A class for representing a step of a slide."""

    def __init__(
        self,
        *animations: Union[Data, Style, Config],
        **anim_options: Optional[dict],
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
            if all(
                [
                    not isinstance(animation, Data),
                    not isinstance(animation, Style),
                    not isinstance(animation, Config),
                ]
            ):
                raise TypeError("Type must be Data, Style or Config.")
            if isinstance(animation, Data):
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

        self.append(step)


class Story(dict):
    """A class for representing a presentation story."""

    def __init__(self, data: Data, style: Optional[Style] = None):
        super().__init__()

        if any([not isinstance(data, Data), not isinstance(style, Style)]):
            raise TypeError("Type must be Data or Style.")

        self.update(data.build())
        self.update(style.build())
        self["slides"] = []

    def add_slide(self, slide: Slide) -> None:
        """A method for adding a slide for the story."""

        self["slides"].append(slide)
