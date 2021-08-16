from sqlalchemy import Column, ForeignKey
from sqlalchemy import String, Integer, DateTime
from sqlalchemy.orm import relationship

from db.database import Base


class Note(Base):
    """
    Table keeping all the notes in a notebook
    """
    __tablename__="notes"

    reference = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, nullable=False)
    created_at = Column(DateTime, nullable=False)
    content = Column(String, nullable=False, unique=True)
    notebook_id = Column(Integer, ForeignKey("notebooks.reference"))

    notebooks = relationship("Notebook", back_populates="notes")