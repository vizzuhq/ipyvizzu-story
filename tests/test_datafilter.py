"""A module for testing the ipyvizzustory.storylib.animation.DataFilter class."""

import unittest

from ipyvizzu import Data

from ipyvizzustory.storylib.animation import DataFilter


class TestDataFilter(unittest.TestCase):
    """A class for testing DataFilter() class."""

    def test_build_if_not_filter_was_set(self) -> None:
        """A method for testing DataFilter().build() if no filter was set."""

        data = Data()
        data.add_dimension("Genres", ["Pop", "Rock"])
        data.add_dimension("Kinds", ["Hard"])
        data.add_measure("Popularity", [[114, 96]])
        with self.assertRaises(KeyError):
            DataFilter(data).build()

    def test_build_if_not_only_filter_was_set(self) -> None:
        """A method for testing DataFilter().build() if not only filter was set."""

        data = Data.filter(None)
        data.add_dimension("Genres", ["Pop", "Rock"])
        data.add_dimension("Kinds", ["Hard"])
        data.add_measure("Popularity", [[114, 96]])
        with self.assertRaises(KeyError):
            DataFilter(data).build()

    def test_build_if_filter_was_set(self) -> None:
        """A method for testing DataFilter().build() if filter was set."""

        data = Data.filter(None)
        self.assertEqual(DataFilter(data).build(), {"filter": None})
