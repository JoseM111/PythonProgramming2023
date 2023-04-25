# file: app/app_setup/app_config.py
# =============================================

from fastapi import FastAPI
from app.routes import post_handlers
import uvicorn

from app.types.types import Void
# =============================================

# Create a global instance of the FastAPI app
app = FastAPI()
# =============================================

def create_app() -> FastAPI:
    # Include the router from book_handlers
    app.include_router(post_handlers.router)

    return app
# =============================================

def uvi_run(local_host: str = "127.0.0.1", port: int = 8000, log_level: str = "info") -> Void:
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
