from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from backend.routers.processes.router import router as processes_router

DIST_PATH = Path(__file__).parent.parent.parent / "frontend" / "dist"

origins = [
    "http://localhost:5173",  # Vue frontend
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://0.0.0.0:8000",
]


def app_maker() -> FastAPI:
    app = FastAPI()
    # https://fastapi.tiangolo.com/tutorial/cors/
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(processes_router)
    app.mount("/", StaticFiles(directory=DIST_PATH, html=True), name="static")
    return app
