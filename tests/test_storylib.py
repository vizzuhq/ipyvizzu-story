"""A module for testing the ipyvizzustory.storylib.story.Story class."""

import unittest
import unittest.mock
from abc import ABC, abstractmethod
from ipyvizzu import Data, Style

from ipyvizzustory.storylib.story import Story, Slide, Step
from ipyvizzustory.storylib.template import VIZZU_STORY, DISPLAY_TEMPLATE


class TestHtml(ABC):
    """An abstract class for testing Story's html."""

    hex = "123456789"

    @abstractmethod
    def story(self, *args, **kwargs):
        """An abstract method for returning Chart()."""

    def get_story(self):
        """A method for returning a test Story."""
        story = self.story(data=Data.filter(None))
        story.add_slide(Slide(Step(Data.filter(None))))
        story.add_slide(Slide(Step(Data.filter('record.Function !== "Defense"'))))
        return story

    def get_vpd(self):
        """A method for returning a test Vizzu-Player data."""
        return (
            "{"
            + '"data": {"filter": null}, '
            + '"slides": ['
            + '[{"filter": null}], '
            + '[{"filter": record => { return (record.Function !== "Defense") }}]'
            + "]}"
        )


class TestStory(TestHtml, unittest.TestCase):
    """A class for testing Story() class."""

    def story(self, *args, **kwargs):
        """A method for returning Chart()."""
        return Story(*args, **kwargs)

    def test_init_if_no_data_was_passed(self) -> None:
        """A method for testing Story().__init__() if no data was passed."""

        with self.assertRaises(TypeError):
            Story()  # pylint: disable=no-value-for-parameter

    def test_init_if_no_data_was_set(self) -> None:
        """A method for testing Story().__init__() if no data was set."""

        with self.assertRaises(TypeError):
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

    def test_to_html(self) -> None:
        """A method for testing Story().to_html()."""

        with unittest.mock.patch(
            "ipyvizzustory.storylib.story.uuid.uuid4", return_value=self
        ):
            self.assertEqual(
                self.get_story().to_html(),
                DISPLAY_TEMPLATE.format(
                    id="1234567",
                    vizzu_story=VIZZU_STORY,
                    vizzu_player_data=self.get_vpd(),
                ),
            )
