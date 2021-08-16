from fastapi import FastAPI

from db.database import engine

import models.notebooks
import models.notes
import routers.heart
import routers.notebooks

models.notes.Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(routers.heart.router, prefix="/api")
app.include_router(routers.notebooks.router, prefix="/api")
