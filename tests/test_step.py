"""A module for testing the ipyvizzustory.storylib.story.Step class."""

import unittest

from ipyvizzu import Data, Config, Style, PlainAnimation

from ipyvizzustory.storylib.story import Step


class TestStep(unittest.TestCase):
    """A class for testing Step() class."""

    def test_init_if_no_animation_was_set(self) -> None:
        """A method for testing Step().__init__() if no animation was set."""

        with self.assertRaises(ValueError):
            Step()

    def test_init_if_anim_option_was_set(self) -> None:
        """A method for testing Step().__init__() if anim option was set."""

        with self.assertRaises(NotImplementedError):
            Step(Data.filter(None), duration=1)

    def test_init_if_animation_was_data(self) -> None:
        """A method for testing Step().__init__() if animation was data."""

        self.assertEqual(Step(Data.filter(None)), {"filter": None})

    def test_init_if_animation_was_config(self) -> None:
        """A method for testing Step().__init__() if animation was config."""

        self.assertEqual(Step(Config({"title": "test"})), {"config": {"title": "test"}})

    def test_init_if_animation_was_style(self) -> None:
        """A method for testing Step().__init__() if animation was style."""

        self.assertEqual(Step(Style(None)), {"style": None})

    def test_init_if_animations_were_set(self) -> None:
        """A method for testing Step().__init__() if animations were set."""

        self.assertEqual(
            Step(Data.filter(None), Config({"title": "test"}), Style(None)),
            {"filter": None, "config": {"title": "test"}, "style": None},
        )

    def test_init_if_same_animations_were_set(self) -> None:
        """A method for testing Step().__init__() if same animations were set."""

        with self.assertRaises(ValueError):
            Step(Data.filter(None), Data.filter(None))

    def test_init_if_not_valid_animation_was_set(self) -> None:
        """A method for testing Step().__init__() if not valid animation was set."""

        with self.assertRaises(TypeError):
            Step(PlainAnimation({}))
