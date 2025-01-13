from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, ConfigDict


class InputReceipe(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    title: str = Field(min_length=3)
    content: str


class OutUserName(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    username: str


class SchReceipe(InputReceipe):
    model_config = ConfigDict(from_attributes=True)

    published_at: datetime
    author: OutUserName
