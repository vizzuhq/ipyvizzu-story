# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring

import unittest

from ipyvizzu import Data

from ipyvizzustory.storylib.story import Slide, Step


class TestSlide(unittest.TestCase):
    def test_init_if_not_valid_step_was_set(self) -> None:
        with self.assertRaises(TypeError):
            Slide({"filter": None})  # type: ignore

    def test_init_if_no_step_was_set(self) -> None:
        self.assertEqual(Slide(), [])

    def test_init_if_step_was_set(self) -> None:
        self.assertEqual(Slide(Step(Data.filter(None))), [{"filter": None}])

    def test_add_step_if_not_valid_step_was_set(self) -> None:
        slide = Slide()
        with self.assertRaises(TypeError):
            slide.add_step(None)  # type: ignore

    def test_add_step_if_initialized_without_step(self) -> None:
        slide = Slide()
        slide.add_step(Step(Data.filter(None)))
        self.assertEqual(slide, [{"filter": None}])

    def test_add_step_if_initialized_with_step(self) -> None:
        slide = Slide(Step(Data.filter(None)))
        slide.add_step(Step(Data.filter(None)))
        self.assertEqual(slide, [{"filter": None}, {"filter": None}])
