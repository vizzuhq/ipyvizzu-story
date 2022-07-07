"""A module for working with ipyvizzu-story animations."""

from ipyvizzu import Data


class DataFilter(Data):
    """A class for representing a data filter."""

    def build(self) -> dict:
        """A method for overwriting Data().build()."""

        if len(self.keys()) != 1:
            raise KeyError("Data can only contain a filter.")
        return {"filter": self["filter"]}
