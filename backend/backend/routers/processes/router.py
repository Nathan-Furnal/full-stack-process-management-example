from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.db import get_session
from backend.models import Process
from backend.routers.processes import GetProcess

SessionDep = Annotated[Session, Depends(get_session)]

router = APIRouter(prefix="/processes")


@router.get("/", response_model=list[GetProcess])
async def get_all_processes(session: SessionDep):
    processes = session.query(Process).all()
    return [GetProcess.model_validate(p) for p in processes]


@router.get("/{pid}", response_model=GetProcess)
async def get_process(pid: int, session: SessionDep):
    process = session.get(Process, pid)
    return GetProcess.model_validate(process)
