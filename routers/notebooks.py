from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session

from db.database import SessionLocal

import starlette.status
import models.notebooks
import schemas.notebooks

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/notebooks/", tags=['notebooks'], status_code=starlette.status.HTTP_200_OK)
async def read_notebooks(db_session: Session = Depends(get_db)):
    return models.notebooks.CRUDNotebook(db_session).get_notebooks()


@router.get("/notebooks/{notebook_reference}", tags=['notebooks'], status_code=starlette.status.HTTP_200_OK)
async def read_notebook(notebook_reference: int, db_session: Session = Depends(get_db)):
    notebook = models.notebooks.CRUDNotebook(db_session).get_notebook(notebook_reference)
    if notebook is None:
        return HTTPException(status_code=404, detail="This notebook does not exist")

    return schemas.notebooks.NotebookInDB(
        reference=notebook.reference,
        title=notebook.title,
        subtitle=notebook.subtitle,
        notes=notebook.notes
    )


@router.post("/notebooks/", tags=['notebooks'], status_code=starlette.status.HTTP_201_CREATED)
async def create_notebook(request: schemas.notebooks.NotebookCreate, db_session: Session = Depends(get_db)):
    db_notebook = models.notebooks.CRUDNotebook(db_session).get_notebook(request.reference)
    if db_notebook is not None:
        return HTTPException(status_code=400, detail="This notebook already exists")

    new_notebook = models.notebooks.CRUDNotebook(db_session).create_notebook(request)
    return schemas.notebooks.NotebookInDB(
        reference=new_notebook.reference,
        title=new_notebook.title,
        subtitle=new_notebook.subtitle,
        notes=new_notebook.notes
    )


@router.delete("/notebooks/{notebook_reference}", tags=['notebooks'], status_code=starlette.status.HTTP_204_NO_CONTENT)
async def delete_notebook(notebook_reference: int, db_session: Session = Depends(get_db)):
    db_notebook = models.notebooks.CRUDNotebook(db_session).get_notebook(notebook_reference)
    if db_notebook is None:
        return HTTPException(status_code=404, detail="Could not find notebook")

    db_session.delete(db_notebook)
    db_session.commit()
