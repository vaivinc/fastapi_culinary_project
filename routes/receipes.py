from http.client import HTTPException

from fastapi import APIRouter, Depends
from starlette import status

from routes.auth import get_current_user

from main import app
from settings import get_session
from schemas.receipes import *
from models.receipes import Receipes


route = APIRouter()


@route.post("/create/receipe/")
async def create_receipe(receipe: InputReceipe,
                         user=Depends(get_current_user),
                         session=Depends(get_session)):
    new_receipe = Receipes(**receipe.model_dump(), author=user)
    session.add(new_receipe)
    try:
        await session.commit()
        await session.refresh(new_receipe)
        return SchReceipe.model_validate(new_receipe)

    except Exception as e:
        await session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="Помилка при створенні статті")
