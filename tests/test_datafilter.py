# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring

import unittest

from ipyvizzu import Data

from ipyvizzustory.storylib.animation import DataFilter


class TestDataFilter(unittest.TestCase):
    def test_build_if_not_filter_was_set(self) -> None:
        data = Data()
        data.add_dimension("Genres", ["Pop", "Rock"])
        data.add_dimension("Kinds", ["Hard"])
        data.add_measure("Popularity", [[114, 96]])
        with self.assertRaises(KeyError):
            DataFilter(data).build()

    def test_build_if_not_only_filter_was_set(self) -> None:
        data = Data.filter(None)
        data.add_dimension("Genres", ["Pop", "Rock"])
        data.add_dimension("Kinds", ["Hard"])
        data.add_measure("Popularity", [[114, 96]])
        with self.assertRaises(KeyError):
            DataFilter(data).build()

    def test_build_if_filter_was_set(self) -> None:
        data = Data.filter(None)
        self.assertEqual(DataFilter(data).build(), {"filter": None})
