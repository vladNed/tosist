from datetime import datetime

from pydantic import BaseModel


class NoteBase(BaseModel):
    title: str
    content: str


class NoteCreate(NoteBase):
    created_at: datetime


class Note(NoteBase):
    reference: int
    created_at: datetime
    notebook_id: int

    class Config:
        orm_mode = True