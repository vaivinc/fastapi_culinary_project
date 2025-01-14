from sqlalchemy.orm import Mapped, mapped_column, relationship

from schemas.user import UserType
from settings import Base

from .receipes import Recipe


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    password_hash: Mapped[str] = mapped_column()
    role: Mapped[UserType] = mapped_column(default=UserType.USER)

    recipes: Mapped[list["Recipe"]] = relationship("Recipe", back_populates="author")
