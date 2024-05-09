from datetime import date

from pydantic import BaseModel, ConfigDict

from backend.models.process import ProcessPerformance


class GetLink(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    url: str
    event_id: int | None = None


class GetAttachment(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    filename: str
    event_id: int | None = None


class GetEvent(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    type: str
    explanation: str
    attachements: list[GetAttachment]
    links: list[GetLink]
    process_id: int | None


class GetProcess(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    business_date: date
    working_date: date
    service: str
    performance: ProcessPerformance
    events: list[GetEvent]
