# file: ./app_setup/middlewares.py
# =============================================
# Support for regular expressions (RE)
import re

from fastapi import FastAPI
from starlette.datastructures import MutableHeaders
from starlette.middleware.cors import CORSMiddleware

from app.types.types import RequestHandler
from starlette.requests import Request
from starlette.responses import Response
# =============================================
"""
With these changes, your FastAPI application will now
use the content_type_middleware to set the Content-Type
header to application/json by default if it's not present
in the incoming request headers.
"""
async def middleware_config(request: Request, request_handler: RequestHandler) -> Response:
    if request.method in ["POST", "PUT"]:
        # Define the URL pattern for POST and PUT requests
        # regex explained: /posts/any-string-with-word-chars-and-hyphens
        post_url_pattern = re.compile(r"^/posts(?:/[\w-]+)?$")

        # Check if the URL path matches the post_url_pattern
        if post_url_pattern.match(request.url.path):
            # If the URL path matches, set the default Content-Type header
            new_headers = MutableHeaders(request.headers)
            new_headers.setdefault(key="Content-Type", value="application/json")
            request.scope['headers'] = new_headers.items()

    response: Response = await request_handler(request)
    return response


# =============================================

def add_cors(app_setup:  FastAPI):
    app_setup.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
# =============================================

















