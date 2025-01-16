from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship

from settings import Base


class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)

    recipes: Mapped[list["Recipe"]] = relationship("Recipe",
                                                   back_populates="category",
                                                   lazy="selectin")


recipe_ingredient_association = Table(
    "recipe_ingredient_association",
    Base.metadata,
    Column("recipe_id", Integer, ForeignKey("recipes.id"), primary_key=True),
    Column("ingredient_id", Integer, ForeignKey("ingredients.id"), primary_key=True),
    Column("quantity", String, default="Yo taste")
)


class Recipe(Base):
    __tablename__ = "recipes"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False)

    # description
    # cooking_time

    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    author: Mapped["User"] = relationship("User", back_populates="recipes", lazy="selectin")

    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))
    category: Mapped["Category"] = relationship("Category", back_populates="recipes", lazy="selectin")

    ingredients: Mapped[list["Ingredient"]] = relationship(
        "Ingredient",
        secondary="recipe_ingredient_association",
        back_populates="recipes",
        lazy="selectin"
    )


class Ingredient(Base):
    __tablename__ = "ingredients"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)

    recipes: Mapped[list["Recipe"]] = relationship(
        "Recipe", secondary="recipe_ingredient_association", back_populates="ingredients",
        lazy="selectin"
    )
