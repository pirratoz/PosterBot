from typing import Any

from pydantic import BaseModel


class MediaIds(BaseModel):
    photo: list[int] | None = []
    video: list[int] | None = []


class Media(BaseModel):
    text_message_id: int
    media_ids: MediaIds
    keyboard: list[list[dict[str, Any]]] | None = []


class TemplateResponse(BaseModel):
    id: int
    title: str
    from_chat_id: int
    media: Media


class TemplateManyResponse(BaseModel):
    templates: list[TemplateResponse]
