"""Python integration of Vizzu-Story."""


from .storylib.story import Step, Slide


class Environment:
    """A class for selecting the runtime environment."""

    # pylint: disable=import-outside-toplevel
    # pylint: disable=unused-import

    @staticmethod
    def get_story() -> None:
        """A static method for importing the appropriate chart for the environment."""

        if Environment.is_ipython():  # pragma: no cover
            from .ipython_env.story import Story as JupyterStory

            return JupyterStory

        if Environment.is_streamlit():  # pragma: no cover
            from .streamlit_env.story import Story as StreamlitStory

            return StreamlitStory

        from .python_env.story import Story as PythonStory

        return PythonStory

    @staticmethod
    def is_ipython():
        """A static method for detecting Jupyter environment."""
        try:
            from IPython import get_ipython

            return get_ipython()
        except ImportError:  # pragma: no cover
            return None

    @staticmethod
    def is_streamlit():
        """A static method for detecting Streamlit environment."""
        try:
            from streamlit.scriptrunner.script_run_context import get_script_run_ctx

            return get_script_run_ctx()
        except ImportError:  # pragma: no cover
            return None


Story = Environment.get_story()
