# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring

import unittest
import unittest.mock

from ddt import ddt, data  # type: ignore

from tests.test_storylib import TestHtml

from ipyvizzustory.env.py.story import Story as PythonStory
from ipyvizzustory.env.ipy.story import Story as JupyterStory
from ipyvizzustory.env.st.story import Story as StreamlitStory
from ipyvizzustory.env.pn.story import Story as PanelStory


class TestPythonStory(TestHtml, unittest.TestCase):
    def story(self, *args, **kwargs) -> PythonStory:
        return PythonStory(*args, **kwargs)

    def test_play(self) -> None:
        with unittest.mock.patch(
            "ipyvizzustory.storylib.story.uuid.uuid4", return_value=self
        ):
            self.assertEqual(
                self.get_story().play(),
                self.get_html(),
            )


class TestJupyterStory(TestHtml, unittest.TestCase):
    def story(self, *args, **kwargs) -> JupyterStory:
        return JupyterStory(*args, **kwargs)

    def test_play(self) -> None:
        with unittest.mock.patch(
            "ipyvizzustory.storylib.story.uuid.uuid4",
            return_value=self,
        ):
            with unittest.mock.patch(
                "ipyvizzustory.env.ipy.story.display_html"
            ) as output:
                self.get_story().play()
                self.assertEqual(
                    output.call_args_list[0].args[0].data,
                    self.get_html(),
                )


@ddt
class TestStreamlitStory(TestHtml, unittest.TestCase):
    def story(self, *args, **kwargs) -> StreamlitStory:
        return StreamlitStory(*args, **kwargs)

    @data(
        {"width": "800", "height": 480},
        {"width": 800, "height": "480"},
        {"width": "800", "height": "480"},
    )
    def test_set_size_if_width_or_height_is_not_int(self, value: dict) -> None:
        story = self.get_story()
        with self.assertRaises(ValueError):
            story.set_size(**value)

    def test_play(self) -> None:
        with unittest.mock.patch(
            "ipyvizzustory.storylib.story.uuid.uuid4", return_value=self
        ):
            with unittest.mock.patch("ipyvizzustory.env.st.story.html") as output:
                story = self.get_story()
                story.set_size(width=800, height=480)
                story.play()
                self.assertEqual(
                    output.call_args_list[0].args[0],
                    self.get_html_with_size(),
                )


@ddt
class TestPanelStory(TestHtml, unittest.TestCase):
    def story(self, *args, **kwargs) -> PanelStory:
        return PanelStory(*args, **kwargs)

    @data({"width": "800"}, {"height": "480"}, {"width": "800", "height": "480"})
    def test_play_if_width_or_height_is_not_int(self, value: dict) -> None:
        with unittest.mock.patch(
            "ipyvizzustory.storylib.story.uuid.uuid4", return_value=self
        ):
            story = self.get_story()
            story.set_size(**value)
            with self.assertRaises(ValueError):
                story.play()

    def test_play_if_style_was_not_set(self) -> None:
        with unittest.mock.patch(
            "ipyvizzustory.storylib.story.uuid.uuid4", return_value=self
        ):
            story = self.get_story()
            with self.assertRaises(ValueError):
                story.play()

    def test_play(self) -> None:
        with unittest.mock.patch(
            "ipyvizzustory.storylib.story.uuid.uuid4", return_value=self
        ):
            with unittest.mock.patch("ipyvizzustory.env.pn.story.HTML") as output:
                story = self.get_story()
                story.set_size(width="800px", height="480px")
                story.play()
                self.assertEqual(
                    output.call_args_list[0].args[0],
                    self.get_html_with_size(),
                )
