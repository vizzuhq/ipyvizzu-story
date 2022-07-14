"""A module for testing the ipyvizzustory environment specific Story classes."""

import unittest
import unittest.mock

from ipyvizzustory.env.py.story import Story as PythonStory
from ipyvizzustory.env.ipy.story import Story as JupyterStory
from ipyvizzustory.env.st.story import Story as StreamlitStory

from tests.test_storylib import TestHtml


class TestPythonStory(TestHtml, unittest.TestCase):
    """A class for testing Story() class in Python environment."""

    def story(self, *args, **kwargs) -> PythonStory:
        """A method for returning Chart()."""
        return PythonStory(*args, **kwargs)

    def test_play(self) -> None:
        """A method for testing Story().play()."""

        with unittest.mock.patch(
            "ipyvizzustory.storylib.story.uuid.uuid4", return_value=self
        ):
            self.assertEqual(
                self.get_story().play(),
                self.get_html(),
            )


class TestJupyterStory(TestHtml, unittest.TestCase):
    """A class for testing Story() class in Jupyter environment."""

    def story(self, *args, **kwargs) -> JupyterStory:
        """A method for returning Chart()."""
        return JupyterStory(*args, **kwargs)

    def test_play(self) -> None:
        """A method for testing Story().play()."""

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

    def test_repr_html_(self) -> None:
        """A method for testing Story()._repr_html_()."""

        with unittest.mock.patch(
            "ipyvizzustory.storylib.story.uuid.uuid4", return_value=self
        ):
            self.assertEqual(
                self.get_story()._repr_html_(),  # pylint: disable=protected-access
                self.get_html(),
            )


class TestStreamlitStory(TestHtml, unittest.TestCase):
    """A class for testing Story() class in Streamlit environment."""

    def story(self, *args, **kwargs) -> StreamlitStory:
        """A method for returning Chart()."""
        return StreamlitStory(*args, **kwargs)

    def test_play(self) -> None:
        """A method for testing Story().play()."""

        with unittest.mock.patch(
            "ipyvizzustory.storylib.story.uuid.uuid4", return_value=self
        ):
            with unittest.mock.patch("ipyvizzustory.env.st.story.html") as output:
                self.get_story().play()
                self.assertEqual(
                    output.call_args_list[0].args[0],
                    self.get_html(),
                )
