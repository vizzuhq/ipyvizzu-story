"""A module for testing the ipyvizzustory.storylib.story.Slide class."""

import unittest

from ipyvizzu import Data

from ipyvizzustory.storylib.story import Slide, Step


class TestSlide(unittest.TestCase):
    """A class for testing Slide() class."""

    def test_init_if_not_valid_step_was_set(self) -> None:
        """A method for testing Slide().__init__() if not valid step was set."""

        with self.assertRaises(TypeError):
            Slide({"filter": None})  # type: ignore

    def test_init_if_no_step_was_set(self) -> None:
        """A method for testing Slide().__init__() if no step was set."""

        self.assertEqual(Slide(), [])

    def test_init_if_step_was_set(self) -> None:
        """A method for testing Slide().__init__() if step was set."""

        self.assertEqual(Slide(Step(Data.filter(None))), [{"filter": None}])

    def test_add_step_if_not_valid_step_was_set(self) -> None:
        """A method for testing Slide().add_step() if not valid step was set."""

        slide = Slide()
        with self.assertRaises(TypeError):
            slide.add_step(None)  # type: ignore

    def test_add_step_if_initialized_without_step(self) -> None:
        """A method for testing Slide().add_step() if initialized without step."""

        slide = Slide()
        slide.add_step(Step(Data.filter(None)))
        self.assertEqual(slide, [{"filter": None}])

    def test_add_step_if_initialized_with_step(self) -> None:
        """A method for testing Slide().add_step() if initialized with step."""

        slide = Slide(Step(Data.filter(None)))
        slide.add_step(Step(Data.filter(None)))
        self.assertEqual(slide, [{"filter": None}, {"filter": None}])
