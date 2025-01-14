from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship

from settings import Base


class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)

    recipes: Mapped[list["Recipe"]] = relationship("Recipe", back_populates="category")


# Association table for Recipe-Ingredient many-to-many relationship
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

    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    author: Mapped["User"] = relationship("User", back_populates="recipes")

    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))
    category: Mapped["Category"] = relationship("Category", back_populates="recipes")

    ingredients: Mapped[list["Ingredient"]] = relationship(
        "Ingredient", secondary=recipe_ingredient_association, back_populates="recipes"
    )


class Ingredient(Base):
    __tablename__ = "ingredients"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)

    recipes: Mapped[list["Recipe"]] = relationship(
        "Recipe", secondary=recipe_ingredient_association, back_populates="ingredients"
    )
