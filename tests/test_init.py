# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring

import unittest

import IPython  # pylint: disable=unused-import
import streamlit  # pylint: disable=unused-import

from tests.utils.import_modifiers import RaiseImportError, ReImport
from tests.mocks import ipython
from tests.mocks.streamlit import streamlit_runtime, streamlit_scriptrunner


class TestInitPy(unittest.TestCase):
    def test_import_story_in_ipython(self):
        with ReImport("IPython", ipython):
            with ReImport("ipyvizzustory"):
                import ipyvizzustory  # pylint: disable=import-outside-toplevel

                self.assertEqual(
                    ipyvizzustory.Story.__module__, "ipyvizzustory.env.ipy.story"
                )

    def test_import_story_in_streamlit_scriptrunner(self):
        with ReImport("streamlit", streamlit_scriptrunner):
            with ReImport("ipyvizzustory"):
                import ipyvizzustory  # pylint: disable=import-outside-toplevel

                self.assertEqual(
                    ipyvizzustory.Story.__module__, "ipyvizzustory.env.st.story"
                )

    def test_import_story_in_streamlit_runtime(self):
        with ReImport("streamlit", streamlit_runtime):
            with ReImport("ipyvizzustory"):
                import ipyvizzustory  # pylint: disable=import-outside-toplevel

                self.assertEqual(
                    ipyvizzustory.Story.__module__, "ipyvizzustory.env.st.story"
                )

    def test_import_story_in_python(self):
        with ReImport("ipyvizzustory"):
            import ipyvizzustory  # pylint: disable=import-outside-toplevel

            self.assertEqual(
                ipyvizzustory.Story.__module__, "ipyvizzustory.env.py.story"
            )

    def test_import_story_in_python_with_import_errors(self):
        with RaiseImportError.module_name("IPython"):
            with RaiseImportError.module_name("streamlit"):
                with ReImport("ipyvizzustory"):
                    import ipyvizzustory  # pylint: disable=import-outside-toplevel

                    self.assertEqual(
                        ipyvizzustory.Story.__module__, "ipyvizzustory.env.py.story"
                    )
