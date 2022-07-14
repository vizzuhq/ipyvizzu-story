"""Python integration of Vizzu-Story."""


from .storylib.story import Step, Slide

from .env.py.story import Story as PythonStory

try:
    from .env.ipy.story import Story as JupyterStory
except ImportError:  # pragma: no cover
    JupyterStory = None  # type: ignore

try:
    from .env.st.story import Story as StreamlitStory
except ImportError:  # pragma: no cover
    StreamlitStory = None  # type: ignore


def get_story():
    """A method for returning the appropriate Story for the environment."""

    return JupyterStory or StreamlitStory or PythonStory


Story = get_story()
