from typing import (
    TypeVar,
    Any,
)

from pydantic import BaseModel


T_entities = TypeVar("T_entities", bound=list[dict[str, Any]])


class Media(BaseModel):
    file_id: str
    type: str
    message_id: int


class Button(BaseModel):
    text: str
    url: str


class TemplateResponse(BaseModel):
    id: int
    title: str
    text: str
    entities: T_entities
    media: list[Media]
    keyboard: list[list[Button]]


class TemplateManyResponse(BaseModel):
    templates: list[TemplateResponse]
