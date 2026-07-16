from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class TaskBase(BaseModel):
    text: str
    project_id: int

class TaskCreate(TaskBase):
    is_done: bool = False

class TaskUpdate(BaseModel):
    text: Optional[str] = None
    is_done: Optional[bool] = None

class TaskResponse(TaskBase):
    id: int
    is_done: bool
    created_at: datetime