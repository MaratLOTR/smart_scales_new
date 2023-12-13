import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from web.containers.Container import UserControllerContainer
from web.views import routers
from uvicorn import run


def create_app() -> FastAPI:
    container = UserControllerContainer()
    db = container.database()
    app = FastAPI()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.container = container
    for router in routers:
        app.include_router(router)
    return app

app = create_app()
