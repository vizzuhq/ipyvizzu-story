# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring

import unittest

from ipyvizzu import Config, Data, PlainAnimation, Style

from ipyvizzustory.storylib.story import Step


class TestStep(unittest.TestCase):
    def test_init_if_no_animation_was_set(self) -> None:
        with self.assertRaises(ValueError):
            Step()

    def test_init_if_anim_option_was_set(self) -> None:
        self.assertEqual(
            Step(Data.filter(None), duration=1),
            {"filter": None, "animOptions": {"duration": 1}},
        )

    def test_init_if_animation_was_data(self) -> None:
        self.assertEqual(Step(Data.filter(None)), {"filter": None})

    def test_init_if_animation_was_config(self) -> None:
        self.assertEqual(Step(Config({"title": "test"})), {"config": {"title": "test"}})

    def test_init_if_animation_was_style(self) -> None:
        self.assertEqual(Step(Style(None)), {"style": None})

    def test_init_if_animations_were_set(self) -> None:
        self.assertEqual(
            Step(Data.filter(None), Config({"title": "test"}), Style(None)),
            {"filter": None, "config": {"title": "test"}, "style": None},
        )

    def test_init_if_same_animations_were_set(self) -> None:
        with self.assertRaises(ValueError):
            Step(Data.filter(None), Data.filter(None))

    def test_init_if_not_valid_animation_was_set(self) -> None:
        with self.assertRaises(TypeError):
            Step(PlainAnimation({}))  # type: ignore
