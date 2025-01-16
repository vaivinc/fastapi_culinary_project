
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import func, select
from sqlalchemy.orm import aliased
from starlette import status

from models.receipes import (Ingredient,  # , recipe_ingredient_association
                             Recipe, recipe_ingredient_association)
from routes.auth import get_current_user
from schemas.receipes import *
from settings import get_session

route = APIRouter()


@route.post("/create/")
async def create_receipe(receipe: InputReceipe,
                         user=Depends(get_current_user),
                         session=Depends(get_session)):
    new_receipe = Recipe(**receipe.model_dump(), author=user)
    session.add(new_receipe)
    try:
        await session.commit()
        await session.refresh(new_receipe)
        return SchReceipe.model_validate(new_receipe)

    except Exception as e:
        await session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="Помилка при створенні статті")


@route.get("/read/all")
async def all_recipes(session=Depends(get_session)):
    total_count = await session.scalar(select(func.count()).select_from(Recipe))
    stmt = (select(Recipe))
    recipes = await session.scalars(stmt)
    recipes = recipes.all()
    if not recipes:
        raise HTTPException(status_code=404, detail="Not exists any recipe")
    return recipes, total_count


@route.get("/read/{recipe_id}")
async def recipe_by_id(recipe_id: int, session=Depends(get_session)):

    recipe = await session.get(Recipe, recipe_id)
    if not recipe:
        raise HTTPException(status_code=404, detail=f"Рецепт с ID {recipe_id} не найден.")

    ingredients_data = []
    for ingredient in recipe.ingredients:
        stmt = select(recipe_ingredient_association).where(
                recipe_ingredient_association.c.recipe_id == recipe.id,
                recipe_ingredient_association.c.ingredient_id == ingredient.id
            )
        link = await session.execute(stmt)
        link = link.first()

        ingredients_data.append({
            "name": ingredient.name,
            "quantity": link.quantity
        })

    result = {
        "id": recipe.id,
        "title": recipe.title,
        # "description": recipe.description,
        # "cooking_time": recipe.cooking_time,
        "ingredients": ingredients_data
    }
    return result
