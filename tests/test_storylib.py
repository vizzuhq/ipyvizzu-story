"""A module for testing the ipyvizzustory.storylib.story.Story class."""

import unittest

from ipyvizzu import Data, Style

from ipyvizzustory.storylib.story import Story, Slide, Step


class TestStory(unittest.TestCase):
    """A class for testing Story() class."""

    def test_init_if_no_data_was_passed(self) -> None:
        """A method for testing Story().__init__() if no data was passed."""

        with self.assertRaises(TypeError):
            Story()  # pylint: disable=no-value-for-parameter

    def test_init_if_no_data_was_set(self) -> None:
        """A method for testing Story().__init__() if no data was set."""

        with self.assertRaises(ValueError):
            Story(data={})

    def test_init_if_not_valid_data_was_set(self) -> None:
        """A method for testing Story().__init__() if not valid data was set."""

        with self.assertRaises(TypeError):
            Story(data={"filter": None})

    def test_init_if_data_was_set(self) -> None:
        """A method for testing Story().__init__() if data was set."""

        self.assertEqual(
            Story(data=Data.filter(None)), {"data": {"filter": None}, "slides": []}
        )

    def test_init_if_no_style_was_set(self) -> None:
        """A method for testing Story().__init__() if no style was set."""

        self.assertEqual(
            Story(data=Data.filter(None), style={}),
            {"data": {"filter": None}, "slides": []},
        )

    def test_init_if_not_valid_style_was_set(self) -> None:
        """A method for testing Story().__init__() if not valid style was set."""

        with self.assertRaises(TypeError):
            Story(data=Data.filter(None), style={"style": None})

    def test_init_if_style_was_set(self) -> None:
        """A method for testing Story().__init__() if data was set."""

        self.assertEqual(
            Story(data=Data.filter(None), style=Style(None)),
            {"data": {"filter": None}, "style": None, "slides": []},
        )

    def test_add_slide_if_no_slide_was_set(self) -> None:
        """A method for testing Story().add_slide() if no slide was set."""

        story = Story(data=Data.filter(None))
        with self.assertRaises(TypeError):
            story.add_slide({})

    def test_add_slide_if_not_valid_slide_was_set(self) -> None:
        """A method for testing Story().add_slide() if not valid slide was set."""

        story = Story(data=Data.filter(None))
        with self.assertRaises(TypeError):
            story.add_slide({"filter": None})

    def test_add_slide_if_slides_were_set(self) -> None:
        """A method for testing Story().add_slide() if slides were set."""

        story = Story(data=Data.filter(None))
        story.add_slide(Slide(Step(Data.filter(None))))
        story.add_slide(Slide(Step(Data.filter(None))))
        self.assertEqual(
            story,
            {
                "data": {"filter": None},
                "slides": [[{"filter": None}], [{"filter": None}]],
            },
        )
