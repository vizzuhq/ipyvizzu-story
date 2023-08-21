# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring

import sys
from typing import Any, List, Optional
from unittest.mock import MagicMock


class Normalizer:
    # pylint: disable=too-few-public-methods

    @staticmethod
    def normalize_output(
        output: MagicMock, start_index: int = 0, end_index: Optional[int] = None
    ) -> List[Any]:
        output_items = []
        if not end_index:
            end_index = len(output.call_args_list)
        for block in output.call_args_list[start_index:end_index]:
            if sys.version_info >= (3, 8):
                args = block.args
            else:
                # TODO: remove once support for Python 3.7 is dropped
                args, _ = block
            output_items.append(args[0])
        return output_items
