# file: app/app_setup/app_config.py
# =============================================

from fastapi import FastAPI
from starlette.responses import JSONResponse

from app.app_setup.middlewares import middleware_config, add_cors
from app.routes import post_handlers
import uvicorn
# =============================================

"""
By setting the default_response_class to JSONResponse,
FastAPI will use the JSONResponse class for all responses
by default, which sets the Content-Type header to application/json.
This way, we don't need to worry about setting the header manually
for each route.
"""
app = FastAPI(default_response_class=JSONResponse)
# =============================================

def create_app() -> FastAPI:
    # Include the router from book_handlers
    app.include_router(post_handlers.router)
    # CORS Middleware
    add_cors(app)
    # Include middleware for headers
    app.middleware('http')(middleware_config)

    return app
# =============================================

def uvi_run(local_host: str = "127.0.0.1", port: int = 8000, log_level: str = "info") -> None:
    # Pass the app import string to the uvicorn.run function
    config_app_str = "app.app_setup.app_config:app"

    uvicorn.run(
        app=config_app_str,
        host=local_host,
        port=port,
        log_level=log_level,
        reload=True
    )
# =============================================
