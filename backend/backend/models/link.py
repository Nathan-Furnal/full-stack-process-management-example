from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.db import Base

if TYPE_CHECKING:
    from backend.models.event import Event


class Link(Base):
    __tablename__ = "link"

    id: Mapped[int] = mapped_column(primary_key=True)
    url: Mapped[str]
    event_id: Mapped[int] = mapped_column(ForeignKey("event.id"), nullable=True)
    event: Mapped[Event] = relationship(back_populates="links")

    def __repr__(self) -> str:
        return f"Link(id={self.id!r}, url={self.url!r})"
