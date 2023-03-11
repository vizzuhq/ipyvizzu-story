"""A module for working with chart animations."""

from ipyvizzu import Data


class DataFilter(Data):
    """A class for representing a data filter."""

    def build(self) -> dict:
        """
        A method for overwriting [Data.build][ipyvizzu.animation.Data.build] method.
        Data initialized with a `DataFilter` must contain only a filter.

        Returns:
            A dictionary contains the filter key with the filter expression.

        Raises:
            ValueError: If `DataFilter` does not contain a filter or contains anything else.
        """

        if len(self.keys()) != 1 or "filter" not in self:
            raise KeyError("Data must contain filter and only that.")
        return {"filter": self["filter"]}
