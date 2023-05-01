# file: app/types/types.py
# =============================================

from typing import TypeAlias, Callable, Awaitable
from fastapi import Request, Response
# =============================================

RequestHandler: TypeAlias = Callable[[Request], Awaitable[Response]]
# =============================================
