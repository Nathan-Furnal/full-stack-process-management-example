from __future__ import annotations

import enum
from datetime import date
from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.db import Base

if TYPE_CHECKING:
    from backend.models.event import Event


class ProcessPerformance(enum.Enum):
    GREEN = "GREEN"
    ORANGE = "ORANGE"
    RED = "RED"
    GRAY = "GRAY"


class Process(Base):
    __tablename__ = "process"

    id: Mapped[int] = mapped_column(primary_key=True)
    business_date: Mapped[date]
    working_date: Mapped[date]
    service: Mapped[str]
    performance: Mapped[ProcessPerformance]
    events: Mapped[list[Event]] = relationship(
        back_populates="process", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        fmt = "%Y-%m-%d"
        return (
            f"Process(id={self.id!r}, "
            f"business_date={self.business_date.strftime(fmt)}, "
            f"working_date={self.working_date.strftime(fmt)}, "
            f"service={self.service!r}, "
            f"performance={self.performance.value}, "
            f"events={self.events!r})"
        )
