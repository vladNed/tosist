import starlette.status

from typing import Optional
from fastapi import APIRouter
from fastapi.param_functions import Query

router = APIRouter()

ALIVE_DATA = {
    "ALL": {
        "app_name": "Tosist",
        "status": "ALIVE",
        "description": {
            "author": "Vlad Nedelcu",
            "email": "nedelcuvd@gmail.com",
            "description": "A minimalist notepad for programmers"
        }
    },
    "DSC": {
        "author": "Vlad Nedelcu",
        "email": "nedelcuvd@gmail.com",
        "description": "A minimalist notepad for programmers"
    }
}


@router.get('/heartbeat', status_code=starlette.status.HTTP_200_OK)
async def root(cht: Optional[str] = Query(None, max_length=3)):
    """
    The heartbeat of the tosist app
    """
    if cht is not None and cht in ALIVE_DATA.keys():
        return ALIVE_DATA[cht]

    return ALIVE_DATA.get("ALL")
