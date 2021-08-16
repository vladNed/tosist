from typing import List, Optional
from datetime import datetime
from sqlalchemy import Column
from sqlalchemy import Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.orm.session import Session

import db.database
import schemas.notebooks


class Notebook(db.database.Base):
    """
    Model keeping all the notbooks
    """
    __tablename__ = "notebooks"

    reference = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True, nullable=False)
    subtitle = Column(String, unique=True, nullable=False)
    created_at = Column(DateTime, nullable=False)

    notes = relationship("Note", back_populates="notebooks")


class CRUDNotebook:
    """
    CRUD operations for Notebook table
    """

    def __init__(self, session: Session):
        self.db_session = session

    def get_notebooks(self) -> List[Notebook]:
        return self.db_session.query(Notebook).all()

    def get_notebook(self, reference: int) -> Optional[Notebook]:
        return self.db_session.query(Notebook).filter(Notebook.reference == reference).one_or_none()

    def create_notebook(self, request_object: schemas.notebooks.NotebookCreate) -> Notebook:
        notebook = Notebook(
            reference=request_object.reference,
            title=request_object.title,
            subtitle=request_object.subtitle,
            created_at=datetime.now(),
            notes=[]
        )

        self.db_session.add(notebook)
        self.db_session.commit()

        return notebook
