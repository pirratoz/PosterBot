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


class Attachments(BaseModel):
    entities: T_entities | None = []
    media: list[Media] | None = []
    keyboard: list[list[Button]] | None = []


class TemplateResponse(BaseModel):
    id: int
    title: str
    text: str
    attachments: Attachments


class TemplateManyResponse(BaseModel):
    templates: list[TemplateResponse]
