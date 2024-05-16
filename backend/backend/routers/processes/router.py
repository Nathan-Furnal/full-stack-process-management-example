from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.db import get_session
from backend.models import Attachment, Event, Link, Process
from backend.routers.processes import GetProcess, PostProcess

SessionDep = Annotated[Session, Depends(get_session)]

router = APIRouter(prefix="/processes")


def create_process_from_payload(session: Session, payload: PostProcess):
    events = []
    for event in payload.events:
        links = [Link(url=link.url) for link in event.links]
        attachments = [Attachment(filename=a.filename) for a in event.attachments]
        db_event = Event(
            type=event.type,
            explanation=event.explanation,
            links=links,
            attachments=attachments,
        )
        events.append(db_event)
    session.add_all(events)

    db_process = Process(
        business_date=payload.business_date,
        working_date=payload.working_date,
        service=payload.service,
        performance=payload.performance,
        events=events,
    )
    session.add(db_process)
    session.commit()
    return GetProcess.model_validate(db_process)


@router.get("/", response_model=list[GetProcess])
async def get_all_processes(session: SessionDep):
    processes = session.query(Process).all()
    return [GetProcess.model_validate(p) for p in processes]


@router.get("/{pid}", response_model=GetProcess)
async def get_process(pid: int, session: SessionDep):
    process = session.get(Process, pid)
    return GetProcess.model_validate(process)


@router.post("/", response_model=GetProcess)
async def create_process(payload: PostProcess, session: SessionDep):
    return create_process_from_payload(session=session, payload=payload)
