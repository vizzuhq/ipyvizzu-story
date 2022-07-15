"""A module for testing the ipyvizzustory.storylib.story.Story class."""

import unittest
import unittest.mock
from abc import ABC, abstractmethod
from ipyvizzu import Data, Style

from ipyvizzustory.storylib.story import Story, Slide, Step
from ipyvizzustory.storylib.template import (
    VIZZU_STORY,
    DISPLAY_TEMPLATE,
    DISPLAY_INDENT,
)


class TestHtml(ABC):
    """An abstract class for testing Story's html."""

    hex: str = "123456789"

    @abstractmethod
    def story(self, *args, **kwargs):  # -> Story
        """An abstract method for returning Chart()."""

    def get_story(self):  # -> Story
        """A method for returning a test Story."""

        story = self.story(data=Data.filter(None))
        story.add_slide(Slide(Step(Data.filter(None))))
        story.add_slide(Slide(Step(Data.filter('record.Function !== "Defense"'))))
        return story

    def get_vpd(self) -> str:
        """A method for returning a test Vizzu-Player data."""

        return (
            "{"
            + '"data": {"filter": null}, '
            + '"slides": ['
            + '[{"filter": null}], '
            + '[{"filter": record => { return (record.Function !== "Defense") }}]'
            + "]}"
        )

    def get_html(self) -> str:
        """A method for returning a test Story html output."""

        return DISPLAY_TEMPLATE.format(
            id="1234567",
            vizzu_story=VIZZU_STORY,
            vizzu_player_data=self.get_vpd(),
            chart_size="",
            chart_features="",
            chart_events="",
        )


class TestStory(TestHtml, unittest.TestCase):
    """A class for testing Story() class."""

    def story(self, *args, **kwargs):
        """A method for returning Chart()."""

        return Story(*args, **kwargs)

    def test_init_if_no_data_was_passed(self) -> None:
        """A method for testing Story().__init__() if no data was passed."""

        with self.assertRaises(TypeError):
            Story()  # type: ignore  # pylint: disable=no-value-for-parameter

    def test_init_if_no_data_was_set(self) -> None:
        """A method for testing Story().__init__() if no data was set."""

        with self.assertRaises(TypeError):
            Story(data={})  # type: ignore

    def test_init_if_not_valid_data_was_set(self) -> None:
        """A method for testing Story().__init__() if not valid data was set."""

        with self.assertRaises(TypeError):
            Story(data={"filter": None})  # type: ignore

    def test_init_if_data_was_set(self) -> None:
        """A method for testing Story().__init__() if data was set."""

        self.assertEqual(
            Story(data=Data.filter(None)), {"data": {"filter": None}, "slides": []}
        )

    def test_init_if_no_style_was_set(self) -> None:
        """A method for testing Story().__init__() if no style was set."""

        self.assertEqual(
            Story(data=Data.filter(None), style={}),  # type: ignore
            {"data": {"filter": None}, "slides": []},
        )

    def test_init_if_not_valid_style_was_set(self) -> None:
        """A method for testing Story().__init__() if not valid style was set."""

        with self.assertRaises(TypeError):
            Story(data=Data.filter(None), style={"style": None})  # type: ignore

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
            story.add_slide({})  # type: ignore

    def test_add_slide_if_not_valid_slide_was_set(self) -> None:
        """A method for testing Story().add_slide() if not valid slide was set."""

        story = Story(data=Data.filter(None))
        with self.assertRaises(TypeError):
            story.add_slide({"filter": None})  # type: ignore

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
                self.get_html(),
            )

    def test_to_html_with_size(self) -> None:
        """A method for testing Story().to_html() with size."""

        with unittest.mock.patch(
            "ipyvizzustory.storylib.story.uuid.uuid4", return_value=self
        ):
            story = self.get_story()
            story.set_size(width=None, height=None)
            self.assertEqual(
                story.to_html(),
                DISPLAY_TEMPLATE.format(
                    id="1234567",
                    vizzu_story=VIZZU_STORY,
                    vizzu_player_data=self.get_vpd(),
                    chart_size="",
                    chart_features="",
                    chart_events="",
                ),
            )

    def test_to_html_with_size_width(self) -> None:
        """A method for testing Story().to_html() with size/width."""

        with unittest.mock.patch(
            "ipyvizzustory.storylib.story.uuid.uuid4", return_value=self
        ):
            story = self.get_story()
            story.set_size(width="800px", height=None)
            self.assertEqual(
                story.to_html(),
                DISPLAY_TEMPLATE.format(
                    id="1234567",
                    vizzu_story=VIZZU_STORY,
                    vizzu_player_data=self.get_vpd(),
                    chart_size="vizzuPlayer.style.cssText = 'width: 800px;'",
                    chart_features="",
                    chart_events="",
                ),
            )

    def test_to_html_with_size_height(self) -> None:
        """A method for testing Story().to_html() with size/height."""

        with unittest.mock.patch(
            "ipyvizzustory.storylib.story.uuid.uuid4", return_value=self
        ):
            story = self.get_story()
            story.set_size(width=None, height="480px")
            self.assertEqual(
                story.to_html(),
                DISPLAY_TEMPLATE.format(
                    id="1234567",
                    vizzu_story=VIZZU_STORY,
                    vizzu_player_data=self.get_vpd(),
                    chart_size="vizzuPlayer.style.cssText = 'height: 480px;'",
                    chart_features="",
                    chart_events="",
                ),
            )

    def test_to_html_with_size_width_and_height(self) -> None:
        """A method for testing Story().to_html() with size/width and height."""

        with unittest.mock.patch(
            "ipyvizzustory.storylib.story.uuid.uuid4", return_value=self
        ):
            story = self.get_story()
            story.set_size(width="800px", height="480px")
            self.assertEqual(
                story.to_html(),
                DISPLAY_TEMPLATE.format(
                    id="1234567",
                    vizzu_story=VIZZU_STORY,
                    vizzu_player_data=self.get_vpd(),
                    chart_size="vizzuPlayer.style.cssText = 'width: 800px;height: 480px;'",
                    chart_features="",
                    chart_events="",
                ),
            )

    def test_to_html_with_feature(self) -> None:
        """A method for testing Story().to_html() with feature."""

        with unittest.mock.patch(
            "ipyvizzustory.storylib.story.uuid.uuid4", return_value=self
        ):
            story = self.get_story()
            story.set_feature("tooltip", True)
            story.set_feature("tooltip", True)
            self.assertEqual(
                story.to_html(),
                DISPLAY_TEMPLATE.format(
                    id="1234567",
                    vizzu_story=VIZZU_STORY,
                    vizzu_player_data=self.get_vpd(),
                    chart_size="",
                    chart_features=(
                        "chart.feature('tooltip', true);"
                        + f"\n{DISPLAY_INDENT * 3}"
                        + "chart.feature('tooltip', true);"
                    ),
                    chart_events="",
                ),
            )

    def test_to_html_with_event(self) -> None:
        """A method for testing Story().to_html() with event."""

        with unittest.mock.patch(
            "ipyvizzustory.storylib.story.uuid.uuid4", return_value=self
        ):
            story = self.get_story()
            handler = """
                let Year = parseFloat(event.data.text);
                if (!isNaN(Year) && Year > 1950 && Year < 2020 && Year % 5 !== 0) {
                    event.preventDefault();
                }
                """
            story.event("plot-axis-label-draw", handler)
            story.event("plot-axis-label-draw", handler)
            self.assertEqual(
                story.to_html(),
                DISPLAY_TEMPLATE.format(
                    id="1234567",
                    vizzu_story=VIZZU_STORY,
                    vizzu_player_data=self.get_vpd(),
                    chart_size="",
                    chart_features="",
                    chart_events=(
                        "chart.on('plot-axis-label-draw', "
                        + f"event => {{{' '.join(handler.split())}}});"
                        + f"\n{DISPLAY_INDENT * 3}"
                        + "chart.on('plot-axis-label-draw', "
                        + f"event => {{{' '.join(handler.split())}}});"
                    ),
                ),
            )
