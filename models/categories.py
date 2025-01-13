from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column


from settings import Base


class Categories(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)