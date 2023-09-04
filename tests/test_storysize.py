# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring

import unittest

from ddt import ddt, data  # type: ignore

from ipyvizzustory.storylib.story import StorySize


@ddt
class TestStorySize(unittest.TestCase):
    @data(
        {"input": 800, "ref": True},
        {"input": 800.0, "ref": True},
        {"input": "800", "ref": True},
        {"input": "800.0", "ref": True},
        {"input": "800px", "ref": True},
        {"input": "800.0px", "ref": True},
        {"input": "80%", "ref": False},
        {"input": "pxpx", "ref": False},
    )
    def test_is_pixel(self, value: dict) -> None:
        self.assertEqual(StorySize.is_pixel(value["input"]), value["ref"])
