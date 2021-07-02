from typing import Callable, Union
from enum import Enum
from argparse import ArgumentTypeError as ArgumentError
import os

class ValType(Enum):
    ANY = 0
    FILE = 1
    DIR = 2

class PathType:
    def __init__(
        self,
        exists=True,
        val_type: Union[Callable[[str], bool], ValType] = ValType.FILE,
        stdio_ok=True,
    ):
        """Represent an argument of type path to a file, directory or symlink
        :param exists:
            True: a path that does exist
            False: a path that does not exist, in a valid parent directory
            None: don't care
        :param val_type: ValType.FILE, ValType.DIR, ValType.ANY, or a function returning True for valid paths
            None: don't care
        :param stdio_ok: whether to allow "-" as stdin/stdout"""

        assert exists in (True, False, None)
        assert isinstance(val_type, ValType) or callable(val_type)

        self.exists = exists
        self.val_type = val_type
        self.stdio_ok = stdio_ok

    def __call__(self, value):
        if value == "-":
            if self.val_type != ValType.FILE or not self.stdio_ok:
                raise ArgumentError("Standard input/output (-) not allowed")
            return value
        
        if self.exists is None:
            return value
        
        if self.exists is True:
            if not os.path.exists(value):
                raise ArgumentError(f"Path does not exist: {value}")
            if not self.valid_type(value):
                raise ArgumentError(f"Path has to of of type {self.val_type.name if not callable(self.val_type) else 'custom'}")
            return value
        
        if self.exists is False:
            if os.path.exists(value):
                raise ArgumentError(f"Path already exists: {value}")
            return value
        
    def valid_type(self, value) -> bool:
        if self.val_type == ValType.ANY: return True
        if self.val_type == ValType.FILE and os.path.isfile(value): return True
        if self.val_type == ValType.DIR and os.path.isdir(value): return True
        if callable(self.val_type) and self.val_type(value): return True
        return False
        
