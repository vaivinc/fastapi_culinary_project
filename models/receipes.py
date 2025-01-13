from sqlalchemy.orm import Mapped, mapped_column

from settings import Base


class Receipes(Base):
    __tablename__ = "receipes"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False)
    ingredients: Mapped[str] = mapped_column(nullable=False)



