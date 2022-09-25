"""
ipyvizzu-story package consists of two main parts:

* ipyvizzustory.storylib: environment independent modules
* ipyvizzustory.env: environment dependent modules

ipyvizzustory package tries to figure out the environment and import the correct type of `Story`,
however `Story` could be imported with full path.

ipyvizzustory package imports the following objects in `__init__.py`:

* `Step` and `Slide` from `ipyvizzustory.storylib.story`
* `Story` from `ipyvizzustory.env.py.story` or
    `ipyvizzustory.env.ipy.story` or
    `ipyvizzustory.env.st.story`
"""


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

    if hasattr(st, "runtime"):  # pragma: no cover
        ctx = st.runtime.scriptrunner.get_script_run_ctx()  # type: ignore
    else:  # pragma: no cover
        ctx = st.scriptrunner.script_run_context.get_script_run_ctx()  # type: ignore

    if not ctx:  # pragma: no cover
        raise ImportError("StreamlitStory")
except ImportError:  # pragma: no cover
    StreamlitStory = None  # type: ignore


def get_story():
    """
    A method for returning the appropriate Story for the environment.

    Returns:
        (Union[ipyvizzustory.env.py.story.Story, ipyvizzustory.env.ipy.story.Story, ipyvizzustory.env.st.story.Story]):
            The appropriate `Story` for the environment.
    """  # pylint: disable=line-too-long

    return JupyterStory or StreamlitStory or PythonStory


Story = get_story()
