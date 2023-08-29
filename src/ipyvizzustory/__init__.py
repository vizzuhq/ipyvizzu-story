"""
Build, present and share animated data stories in `Jupyter Notebook` and similar environments.

`ipyvizzu-story` package consists of two main parts:

* [Storylib][ipyvizzustory.storylib]: environment independent modules
* [Env][ipyvizzustory.env]: environment dependent modules

`ipyvizzu-story` package tries to figure out the environment and import the correct type of `Story`,
however `Story` could be imported with full path.

`ipyvizzu-story` package imports the following objects in `__init__.py`:


* `Story` from [Env.py.story][ipyvizzustory.env.py.story] or
    [Env.ipy.story][ipyvizzustory.env.ipy.story] or
    [Env.st.story][ipyvizzustory.env.st.story]
* [Step][ipyvizzustory.storylib.story.Step]
* [Slide][ipyvizzustory.storylib.story.Slide]
"""

import warnings

from .__version__ import __version__, PYENV

from .storylib.story import Step, Slide

from .env.py.story import Story as PythonStory

try:
    from .env.ipy.story import Story as JupyterStory
    import IPython

    if not IPython.get_ipython():
        raise ImportError("JupyterStory")
except ImportError:
    JupyterStory = None  # type: ignore

try:
    from .env.st.story import Story as StreamlitStory
    import streamlit as st

    if hasattr(st, "runtime"):
        ctx = st.runtime.scriptrunner.get_script_run_ctx()
    else:
        ctx = st.scriptrunner.script_run_context.get_script_run_ctx()  # type: ignore  # pylint: disable=no-member

    if not ctx:
        raise ImportError("StreamlitStory")
except ImportError:
    StreamlitStory = None  # type: ignore


def get_story():
    """
    A method for returning the appropriate Story for the environment.

    Returns:
        (Union[ipyvizzustory.env.py.story.Story, ipyvizzustory.env.ipy.story.Story, ipyvizzustory.env.st.story.Story]):
            The appropriate `Story` for the environment.
    """  # pylint: disable=line-too-long

    return JupyterStory or StreamlitStory or PythonStory  # type: ignore


Story = get_story()
"""
Available types:

* [Jupyter/IPython Story][ipyvizzustory.env.ipy.story.Story]
* [Streamlit Story][ipyvizzustory.env.st.story.Story]
* [Panel Story][ipyvizzustory.env.pn.story.Story]
* [Python Story][ipyvizzustory.env.py.story.Story]
"""

__all__ = ["get_story", "Story", "Slide", "Step"]

# TODO: remove once support for Python 3.6 is dropped
if PYENV < (3, 7):
    warnings.warn(
        "Python 3.6 support will be dropped in future versions.",
        FutureWarning,
        stacklevel=2,
    )
