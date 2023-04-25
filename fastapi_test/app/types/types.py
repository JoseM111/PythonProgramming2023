# file: app/types/types.py
# =============================================

from typing import TypeVar, Union
# =============================================

Void = None
# =============================================

# Custom ResultType class
Type = TypeVar("Type")
TypeNone = TypeVar("TypeNone")
ResultType = Union[Type, TypeNone]
# =============================================
