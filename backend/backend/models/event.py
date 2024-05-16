from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.db import Base
from backend.models.attachment import Attachment
from backend.models.link import Link

if TYPE_CHECKING:
    from backend.models.process import Process


class Event(Base):
    __tablename__ = "event"

    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str]
    explanation: Mapped[str]
    attachments: Mapped[list[Attachment]] = relationship(
        back_populates="event", cascade="all, delete-orphan"
    )
    links: Mapped[list[Link]] = relationship(
        back_populates="event", cascade="all, delete-orphan"
    )
    process_id: Mapped[int] = mapped_column(ForeignKey("process.id"), nullable=True)
    process: Mapped[Process] = relationship(back_populates="events")

    def __repr__(self) -> str:
        return (
            f"Event(id={self.id!r}, "
            f"type={self.type!r}, "
            f"explanation={self.explanation!r}, "
            f"attachments={self.attachments!r}, "
            f"links={self.links!r})"
        )
