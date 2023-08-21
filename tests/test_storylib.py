# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring

import unittest
import unittest.mock
import os
import shutil
from abc import ABC, abstractmethod

from ipyvizzu import Data, Style

from ipyvizzustory.storylib.story import Story, Slide, Step
from ipyvizzustory.storylib.template import (
    VIZZU_STORY,
    DISPLAY_TEMPLATE,
    DISPLAY_INDENT,
)


class TestHtml(ABC):
    hex: str = "123456789"

    @abstractmethod
    def story(self, *args, **kwargs):  # -> Story
        """An abstract method for returning a story instance."""

    def get_story(self):  # -> Story
        story = self.story(data=Data.filter(None))
        story.add_slide(Slide(Step(Data.filter(None))))
        story.add_slide(Slide(Step(Data.filter('record.Function !== "Defense"'))))
        return story

    def get_vpd(self) -> str:
        return (
            "{"
            + '"data": {"filter": null}, '
            + '"slides": ['
            + '[{"filter": null}], '
            + '[{"filter": record => { return (record.Function !== "Defense") }}]'
            + "]}"
        )

    def get_html(self) -> str:
        return DISPLAY_TEMPLATE.format(
            id="1234567",
            vizzu_attribute="",
            start_slide="",
            vizzu_story=VIZZU_STORY,
            vizzu_player_data=self.get_vpd(),
            chart_size="",
            chart_features="",
            chart_events="",
        )

    def get_html_with_size(self) -> str:
        return DISPLAY_TEMPLATE.format(
            id="1234567",
            vizzu_attribute="",
            start_slide="",
            vizzu_story=VIZZU_STORY,
            vizzu_player_data=self.get_vpd(),
            chart_size="vp.style.cssText = 'width: 800px;height: 480px;'",
            chart_features="",
            chart_events="",
        )


class TestStoryInit(unittest.TestCase):
    def test_init_if_no_data_was_passed(self) -> None:
        with self.assertRaises(TypeError):
            Story()  # type: ignore  # pylint: disable=no-value-for-parameter

    def test_init_if_no_data_was_set(self) -> None:
        with self.assertRaises(TypeError):
            Story(data={})  # type: ignore

    def test_init_if_not_valid_data_was_set(self) -> None:
        with self.assertRaises(TypeError):
            Story(data={"filter": None})  # type: ignore

    def test_init_if_data_was_set(self) -> None:
        self.assertEqual(
            Story(data=Data.filter(None)), {"data": {"filter": None}, "slides": []}
        )

    def test_init_if_no_style_was_set(self) -> None:
        self.assertEqual(
            Story(data=Data.filter(None), style={}),  # type: ignore
            {"data": {"filter": None}, "slides": []},
        )

    def test_init_if_not_valid_style_was_set(self) -> None:
        with self.assertRaises(TypeError):
            Story(data=Data.filter(None), style={"style": None})  # type: ignore

    def test_init_if_style_was_set(self) -> None:
        self.assertEqual(
            Story(data=Data.filter(None), style=Style(None)),
            {"data": {"filter": None}, "style": None, "slides": []},
        )


class TestStoryAddSlide(unittest.TestCase):
    def test_add_slide_if_no_slide_was_set(self) -> None:
        story = Story(data=Data.filter(None))
        with self.assertRaises(TypeError):
            story.add_slide({})  # type: ignore

    def test_add_slide_if_not_valid_slide_was_set(self) -> None:
        story = Story(data=Data.filter(None))
        with self.assertRaises(TypeError):
            story.add_slide({"filter": None})  # type: ignore

    def test_add_slide_if_slides_were_set(self) -> None:
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


class TestStoryUrlProperties(TestHtml, unittest.TestCase):
    def story(self, *args, **kwargs):
        return Story(*args, **kwargs)

    def test_vizzu_default(self) -> None:
        story = self.get_story()
        self.assertEqual(story.vizzu, None)

    def test_vizzu(self) -> None:
        vizzu = "127.0.0.1:5500/vizzu.min.js"
        with unittest.mock.patch(
            "ipyvizzustory.storylib.story.uuid.uuid4", return_value=self
        ):
            story = self.get_story()
            story.vizzu = vizzu
            self.assertEqual(
                story.to_html(),
                DISPLAY_TEMPLATE.format(
                    id="1234567",
                    vizzu_attribute=f'vizzu-url="{vizzu}"',
                    start_slide="",
                    vizzu_story=VIZZU_STORY,
                    vizzu_player_data=self.get_vpd(),
                    chart_size="",
                    chart_features="",
                    chart_events="",
                ),
            )

    def test_vizzu_story_default(self) -> None:
        story = self.get_story()
        self.assertEqual(story.vizzu_story, VIZZU_STORY)

    def test_vizzu_story(self) -> None:
        vizzu_story = "127.0.0.1:5500/vizzu-story.min.js"
        with unittest.mock.patch(
            "ipyvizzustory.storylib.story.uuid.uuid4", return_value=self
        ):
            story = self.get_story()
            story.vizzu_story = vizzu_story
            self.assertEqual(
                story.to_html(),
                DISPLAY_TEMPLATE.format(
                    id="1234567",
                    vizzu_attribute="",
                    start_slide="",
                    vizzu_story=vizzu_story,
                    vizzu_player_data=self.get_vpd(),
                    chart_size="",
                    chart_features="",
                    chart_events="",
                ),
            )

    def test_start_slide_default(self) -> None:
        story = self.get_story()
        self.assertEqual(story.start_slide, None)

    def test_start_slide(self) -> None:
        start_slide = 3
        with unittest.mock.patch(
            "ipyvizzustory.storylib.story.uuid.uuid4", return_value=self
        ):
            story = self.get_story()
            story.start_slide = start_slide
            self.assertEqual(
                story.to_html(),
                DISPLAY_TEMPLATE.format(
                    id="1234567",
                    vizzu_attribute="",
                    start_slide=f'start-slide="{start_slide}"',
                    vizzu_story=VIZZU_STORY,
                    vizzu_player_data=self.get_vpd(),
                    chart_size="",
                    chart_features="",
                    chart_events="",
                ),
            )


class TestStoryHtml(TestHtml, unittest.TestCase):
    def setUp(self):
        self.test_dir = os.path.dirname(os.path.realpath(__file__))
        self.test_tmp_dir = os.path.join(self.test_dir, "..", ".tests")
        os.makedirs(self.test_tmp_dir)

    def tearDown(self):
        shutil.rmtree(self.test_tmp_dir)

    def story(self, *args, **kwargs):
        return Story(*args, **kwargs)

    def test_export_to_html(self) -> None:
        with unittest.mock.patch(
            "ipyvizzustory.storylib.story.uuid.uuid4", return_value=self
        ):
            test_html = self.test_tmp_dir + "/test_export_to_html.html"
            story = self.get_story()
            story.export_to_html(test_html)
            with open(test_html, "r", encoding="utf8") as file_desc:
                test_html_content = file_desc.read()
            self.assertEqual(
                test_html_content,
                self.get_html(),
            )

    def test_repr_html(self) -> None:
        with unittest.mock.patch(
            "ipyvizzustory.storylib.story.uuid.uuid4", return_value=self
        ):
            self.assertEqual(
                self.get_story()._repr_html_(),  # pylint: disable=protected-access
                self.get_html(),
            )

    def test_to_html(self) -> None:
        with unittest.mock.patch(
            "ipyvizzustory.storylib.story.uuid.uuid4", return_value=self
        ):
            self.assertEqual(
                self.get_story().to_html(),
                self.get_html(),
            )

    def test_to_html_with_size(self) -> None:
        with unittest.mock.patch(
            "ipyvizzustory.storylib.story.uuid.uuid4", return_value=self
        ):
            story = self.get_story()
            story.set_size(width=None, height=None)
            self.assertEqual(
                story.to_html(),
                DISPLAY_TEMPLATE.format(
                    id="1234567",
                    vizzu_attribute="",
                    start_slide="",
                    vizzu_story=VIZZU_STORY,
                    vizzu_player_data=self.get_vpd(),
                    chart_size="",
                    chart_features="",
                    chart_events="",
                ),
            )

    def test_to_html_with_size_width(self) -> None:
        with unittest.mock.patch(
            "ipyvizzustory.storylib.story.uuid.uuid4", return_value=self
        ):
            story = self.get_story()
            story.set_size(width="800px", height=None)
            self.assertEqual(
                story.to_html(),
                DISPLAY_TEMPLATE.format(
                    id="1234567",
                    vizzu_attribute="",
                    start_slide="",
                    vizzu_story=VIZZU_STORY,
                    vizzu_player_data=self.get_vpd(),
                    chart_size="vp.style.cssText = 'width: 800px;'",
                    chart_features="",
                    chart_events="",
                ),
            )

    def test_to_html_with_size_height(self) -> None:
        with unittest.mock.patch(
            "ipyvizzustory.storylib.story.uuid.uuid4", return_value=self
        ):
            story = self.get_story()
            story.set_size(width=None, height="480px")
            self.assertEqual(
                story.to_html(),
                DISPLAY_TEMPLATE.format(
                    id="1234567",
                    vizzu_attribute="",
                    start_slide="",
                    vizzu_story=VIZZU_STORY,
                    vizzu_player_data=self.get_vpd(),
                    chart_size="vp.style.cssText = 'height: 480px;'",
                    chart_features="",
                    chart_events="",
                ),
            )

    def test_to_html_with_size_width_and_height(self) -> None:
        with unittest.mock.patch(
            "ipyvizzustory.storylib.story.uuid.uuid4", return_value=self
        ):
            story = self.get_story()
            story.set_size(width="800px", height="480px")
            self.assertEqual(
                story.to_html(),
                self.get_html_with_size(),
            )

    def test_to_html_with_feature(self) -> None:
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
                    vizzu_attribute="",
                    start_slide="",
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
            story.add_event("plot-axis-label-draw", handler)
            story.add_event("plot-axis-label-draw", handler)
            self.assertEqual(
                story.to_html(),
                DISPLAY_TEMPLATE.format(
                    id="1234567",
                    vizzu_attribute="",
                    start_slide="",
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
