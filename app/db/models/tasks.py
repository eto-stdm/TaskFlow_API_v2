from datetime import datetime

from sqlalchemy import String, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    text: Mapped[str] = mapped_column(String(100), index=True, nullable=False)
    is_done: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    project_id: Mapped[int] = mapped_column(ForeignKey("projects.id"), nullable=False)

    project = relationship("Project", back_populates="tasks", cascade="all, delete-orphan")
    attachments = relationship("Attachment", back_populates="tasks", cascade="all, delete-orphan")