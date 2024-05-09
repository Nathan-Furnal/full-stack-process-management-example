from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy import Engine
from sqlalchemy.orm import Session

from backend.db import get_engine
from backend.models import Process
from backend.routers.processes import GetProcess

EngineDep = Annotated[Engine, Depends(get_engine)]

router = APIRouter(prefix="/processes")


@router.get("/", response_model=list[GetProcess])
async def get_all_processes(engine: EngineDep):
    with Session(engine) as session:
        processes = session.query(Process).all()
        return [GetProcess.model_validate(p) for p in processes]


@router.get("/{pid}", response_model=GetProcess)
async def get_process(pid: int, engine: EngineDep):
    with Session(engine) as session:
        process = session.get(Process, pid)
        return GetProcess.model_validate(process)
