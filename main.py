import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager

from api import router as router_v1
from core import settings
from core import Base
from db import db_helper


# Async context manager for setting up the database during the application's lifespan
@asynccontextmanager
async def lifespan(lifespan_app: FastAPI):
    """
    Async context manager to handle the application's lifespan.

    Parameters:
    - lifespan_app (FastAPI): The FastAPI application.

    Yields:
    - None

    Usage:
    ```
    async with lifespan(app):
        # Code to be executed during the lifespan of the application
    ```
    """
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield


# Create a FastAPI application
app = FastAPI(
    title="Short Link Service",
    description="A service for generating short links",
    docs_url="/",
    lifespan=lifespan,
)

# Include API routers
app.include_router(router_v1, prefix=settings.api_v1_prefix)


# Run the FastAPI application using Uvicorn when executed as the main module
if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
