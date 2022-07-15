"""Python integration of Vizzu-Story."""


from .storylib.story import Step, Slide

from .env.py.story import Story as PythonStory

try:
    from .env.ipy.story import Story as JupyterStory
    import IPython  # type: ignore

    if not IPython.get_ipython():  # pragma: no cover
        raise ImportError("JupyterStory")
except ImportError as e:  # pragma: no cover
    JupyterStory = None  # type: ignore

try:
    from .env.st.story import Story as StreamlitStory
    import streamlit as st

    if not st.scriptrunner.script_run_context.get_script_run_ctx():  # pragma: no cover
        raise ImportError("StreamlitStory")
except ImportError:  # pragma: no cover
    StreamlitStory = None  # type: ignore


def get_story():
    """A method for returning the appropriate Story for the environment."""

    return JupyterStory or StreamlitStory or PythonStory


Story = get_story()
