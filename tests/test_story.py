"""A module for testing the ipyvizzustory environment specific Story classes."""

import unittest
import unittest.mock

from ipyvizzustory.storylib.template import VIZZU_STORY, DISPLAY_TEMPLATE

from ipyvizzustory.python.story import Story as PythonStory
from ipyvizzustory.jupyter.story import Story as JupyterStory
from ipyvizzustory.streamlit.story import Story as StreamlitStory

from tests.test_storylib import TestHtml


class TestPythonStory(TestHtml, unittest.TestCase):
    """A class for testing Story() class in Python environment."""

    def story(self, *args, **kwargs):
        """A method for returning Chart()."""
        return PythonStory(*args, **kwargs)

    def test_play(self) -> None:
        """A method for testing Story().play()."""

        with unittest.mock.patch(
            "ipyvizzustory.storylib.story.uuid.uuid4", return_value=self
        ):
            self.assertEqual(
                self.get_story().play(),
                DISPLAY_TEMPLATE.format(
                    id="1234567",
                    vizzu_story=VIZZU_STORY,
                    vizzu_player_data=self.get_vpd(),
                ),
            )


class TestJupyterStory(TestHtml, unittest.TestCase):
    """A class for testing Story() class in Jupyter environment."""

    def story(self, *args, **kwargs):
        """A method for returning Chart()."""
        return JupyterStory(*args, **kwargs)

    def test_play(self) -> None:
        """A method for testing Story().play()."""

        with unittest.mock.patch(
            "ipyvizzustory.storylib.story.uuid.uuid4", return_value=self
        ):
            with unittest.mock.patch("ipyvizzustory.jupyter.story.display"):
                with unittest.mock.patch("ipyvizzustory.jupyter.story.HTML") as output:
                    self.get_story().play()
                    self.assertEqual(
                        output.call_args_list[0].args[0],
                        DISPLAY_TEMPLATE.format(
                            id="1234567",
                            vizzu_story=VIZZU_STORY,
                            vizzu_player_data=self.get_vpd(),
                        ),
                    )

    def test_repr_html_(self) -> None:
        """A method for testing Story()._repr_html_()."""

        with unittest.mock.patch(
            "ipyvizzustory.storylib.story.uuid.uuid4", return_value=self
        ):
            self.assertEqual(
                self.get_story()._repr_html_(),  # pylint: disable=protected-access
                DISPLAY_TEMPLATE.format(
                    id="1234567",
                    vizzu_story=VIZZU_STORY,
                    vizzu_player_data=self.get_vpd(),
                ),
            )


class TestStreamlitStory(TestHtml, unittest.TestCase):
    """A class for testing Story() class in Streamlit environment."""

    def story(self, *args, **kwargs):
        """A method for returning Chart()."""
        return StreamlitStory(*args, **kwargs)

    def test_play(self) -> None:
        """A method for testing Story().play()."""

        with unittest.mock.patch(
            "ipyvizzustory.storylib.story.uuid.uuid4", return_value=self
        ):
            with unittest.mock.patch("ipyvizzustory.streamlit.story.html") as output:
                self.get_story().play()
                self.assertEqual(
                    output.call_args_list[0].args[0],
                    DISPLAY_TEMPLATE.format(
                        id="1234567",
                        vizzu_story=VIZZU_STORY,
                        vizzu_player_data=self.get_vpd(),
                    ),
                )
