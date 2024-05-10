from fastapi import FastAPI

from backend.routers.processes.router import router as processes_router


def app_maker() -> FastAPI:
    app = FastAPI()
    app.include_router(processes_router)
    return app
