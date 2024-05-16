from datetime import date

from pydantic import BaseModel, ConfigDict, Field

from backend.models.process import ProcessPerformance


class GetLink(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    url: str
    event_id: int | None = None


class PostLink(BaseModel):
    url: str
    event_id: int | None = None


class GetAttachment(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    filename: str
    event_id: int | None = None


class PostAttachment(BaseModel):
    filename: str
    event_id: int | None = None


class GetEvent(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    type: str
    explanation: str
    attachments: list[GetAttachment] = Field(default_factory=list)
    links: list[GetLink] = Field(default_factory=list)
    process_id: int | None


class PostEvent(BaseModel):
    type: str
    explanation: str
    attachments: list[PostAttachment] = Field(default_factory=list)
    links: list[PostLink] = Field(default_factory=list)
    process_id: int | None = None


class GetProcess(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    business_date: date
    working_date: date
    service: str
    performance: ProcessPerformance
    events: list[GetEvent] = Field(default_factory=list)


class PostProcess(BaseModel):
    business_date: date
    working_date: date
    service: str
    performance: ProcessPerformance
    events: list[PostEvent] = Field(default_factory=list)
