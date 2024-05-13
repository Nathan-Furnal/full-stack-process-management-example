from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.routers.processes.router import router as processes_router


def app_maker() -> FastAPI:
    app = FastAPI()
    # https://fastapi.tiangolo.com/tutorial/cors/
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:5173"],  # Vue frontend
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(processes_router)
    return app
