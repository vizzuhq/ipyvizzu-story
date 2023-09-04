# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring

from abc import abstractmethod
import unittest
import unittest.mock

from ddt import ddt, data  # type: ignore

from tests.test_storylib import TestHtml
from tests.utils.normalizer import Normalizer

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
                    Normalizer.normalize_output(output)[0].data,
                    self.get_html(),
                )


@ddt
class TestStoryWithLimitedPlay(TestHtml):
    @abstractmethod
    def get_mock(self) -> str:
        """An abstract method for returning the mocking value."""

    @abstractmethod
    def assert_raises(self, error):
        """An abstract method for assertRaises."""

    @abstractmethod
    def assert_equal(self, value, ref):
        """An abstract method for assertEqual."""

    def test_play_without_size(self) -> None:
        with unittest.mock.patch(
            "ipyvizzustory.storylib.story.uuid.uuid4", return_value=self
        ):
            story = self.get_story()
            with self.assert_raises(ValueError):
                story.play()

    @data(
        {"width": "800"},
        {"height": "480"},
        {"aspect_ratio": 16 / 9},
        {"width": "100%", "aspect_ratio": 16 / 9},
        {"width": 800, "aspect_ratio": "16/9"},
    )
    def test_play_with_wrong_size(self, value: dict) -> None:
        with unittest.mock.patch(
            "ipyvizzustory.storylib.story.uuid.uuid4", return_value=self
        ):
            story = self.get_story()
            story.set_size(**value)
            with self.assert_raises(ValueError):
                story.play()

    @data(
        {
            "input": {"width": "800.0px", "height": "480.0px"},
            "ref_style": "vp.style.cssText = 'width: 800.0px;height: 480.0px;'",
            "ref_size": (800, 480),
        },
        {
            "input": {"width": "800.0", "height": "480.0"},
            "ref_style": "vp.style.cssText = 'width: 800.0px;height: 480.0px;'",
            "ref_size": (800, 480),
        },
        {
            "input": {"width": 800.0, "height": 480.0},
            "ref_style": "vp.style.cssText = 'width: 800.0px;height: 480.0px;'",
            "ref_size": (800, 480),
        },
        {
            "input": {"width": "800px", "height": "480px"},
            "ref_style": "vp.style.cssText = 'width: 800px;height: 480px;'",
            "ref_size": (800, 480),
        },
        {
            "input": {"width": "800", "height": "480"},
            "ref_style": "vp.style.cssText = 'width: 800px;height: 480px;'",
            "ref_size": (800, 480),
        },
        {
            "input": {"width": "800", "height": 480},
            "ref_style": "vp.style.cssText = 'width: 800px;height: 480px;'",
            "ref_size": (800, 480),
        },
        {
            "input": {"width": 800, "height": "480"},
            "ref_style": "vp.style.cssText = 'width: 800px;height: 480px;'",
            "ref_size": (800, 480),
        },
        {
            "input": {"width": 800.5, "aspect_ratio": 17 / 9},
            "ref_style": (
                "vp.style.cssText = "
                "'aspect-ratio: 1.8888888888888888 !important;width: 800.5px;'"
            ),
            "ref_size": (800, 423),  # 800 / (17 / 9)
        },
        {
            "input": {"height": 480.5, "aspect_ratio": 17 / 9},
            "ref_style": (
                "vp.style.cssText = "
                "'aspect-ratio: 1.8888888888888888 !important;width: unset;height: 480.5px;'"
            ),
            "ref_size": (907, 480),  # 480 * (17 / 9)
        },
    )
    def test_play(self, value: dict) -> None:
        with unittest.mock.patch(
            "ipyvizzustory.storylib.story.uuid.uuid4", return_value=self
        ):
            with unittest.mock.patch(self.get_mock()) as output:
                story = self.get_story()
                story.set_size(**value["input"])
                story.play()
                self.assert_equal(
                    "\n".join(Normalizer.normalize_output(output)),
                    self.get_html(chart_size=value["ref_style"]),
                )
                self.assert_equal(
                    story._size.get_width_height_in_pixels(),  # pylint: disable=protected-access
                    value["ref_size"],
                )


class TestStreamlitStory(TestStoryWithLimitedPlay, unittest.TestCase):
    def story(self, *args, **kwargs) -> StreamlitStory:
        return StreamlitStory(*args, **kwargs)

    def get_mock(self) -> str:
        return "ipyvizzustory.env.st.story.html"

    def assert_raises(self, error):
        return self.assertRaises(error)

    def assert_equal(self, value, ref):
        return self.assertEqual(value, ref)


class TestPanelStory(TestStoryWithLimitedPlay, unittest.TestCase):
    def story(self, *args, **kwargs) -> PanelStory:
        return PanelStory(*args, **kwargs)

    def get_mock(self) -> str:
        return "ipyvizzustory.env.pn.story.HTML"

    def assert_raises(self, error):
        return self.assertRaises(error)

    def assert_equal(self, value, ref):
        return self.assertEqual(value, ref)
