# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring

from contextlib import contextmanager
import importlib
import os
import sys
from types import ModuleType, TracebackType
from typing import Iterator, Optional


class ReImport:
    def __init__(
        self, module_name: str, mock_module: Optional[ModuleType] = None
    ) -> None:
        self.module_name = module_name
        self.mock_module = mock_module
        self.original_module: Optional[ModuleType] = None

    def __enter__(self) -> "ReImport":
        if self.module_name in sys.modules:
            self.original_module = sys.modules[self.module_name]
            del sys.modules[self.module_name]
        if self.mock_module:
            sys.modules[self.module_name] = self.mock_module
        return self

    def __exit__(
        self, exc_type: type, exc_value: BaseException, traceback: TracebackType
    ) -> None:
        if self.module_name in sys.modules:
            del sys.modules[self.module_name]
        if self.original_module:
            sys.modules[self.module_name] = self.original_module
        importlib.invalidate_caches()


class RaiseImportError:
    @classmethod
    @contextmanager
    def module_name(cls, *module_names: str) -> Iterator[None]:
        original_values = {name: os.environ.get(name, None) for name in module_names}
        for name in module_names:
            os.environ[name] = name

        try:
            yield
        finally:
            for name, original_value in original_values.items():
                if original_value is None:
                    os.environ.pop(name, None)
                else:
                    os.environ[name] = original_value

    @staticmethod
    def overwrite_imports() -> None:
        builtins = globals()["__builtins__"]

        def overwrite_import(original_import_builtin):
            def import_replacement(name, *args, **kwargs):
                module_names = os.environ.get("RAISE_IMPORT_ERROR", "").split(",")
                if name in module_names:
                    raise ImportError(f"{name} is not available")
                return original_import_builtin(name, *args, **kwargs)

            return import_replacement

        builtins["__import__"] = overwrite_import(builtins["__import__"])
