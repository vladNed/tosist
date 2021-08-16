from typing import List
from pydantic import BaseModel

import schemas.notes


class NotebookBase(BaseModel):
    title: str


class NotebookCreate(NotebookBase):
    reference: int
    subtitle: str


class NotebookDelete(NotebookBase):
    reference: int


class NotebookInDB(NotebookBase):
    reference: int
    subtitle: str
    notes: List[schemas.notes.Note]

    class Config:
        orm_mode = True
