from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class AttachmentBase(BaseModel):
    file_name: str = Field(max_length=255)
    file_key: str = Field(max_length=500)
    content_type: str = Field(max_length=100)
    size: int = Field()

class AttachmentCreate(AttachmentBase):
    task_id: int
    bucket_name: str = Field(max_length=255)
    created_at: datetime
    pass

class AttachmentResponse(AttachmentBase):
    id: int
    task_id: int
    bucket_name: str = Field(max_length=255)
    created_at: datetime
    uploaded_by_user_id: int
    pass