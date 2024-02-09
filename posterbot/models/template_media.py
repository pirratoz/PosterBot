from typing import (
    TypedDict,
    Any,
)


class Media(TypedDict):
    message_id: int
    file_id: str
    type: str


class Button(TypedDict):
    text: str
    url: str


class Template(TypedDict):
    id: None | int
    title: str
    text: str
    media: list[Media]
    entities: list[dict[str, Any]]
    keyboard: list[list[Button]]


class Attachments(TypedDict):
    media: list[Media]
    entities: list[dict[str, Any]]
    keyboard: list[list[Button]]


class TemplateCreate(TypedDict):
    title: str
    text: str
    attachments: Attachments


def convert_to_template_create(template: Template) -> TemplateCreate:
    return TemplateCreate(
        title=template["title"],
        text=template["text"],
        attachments=Attachments(
            media=template["media"] or None,
            entities=template["entities"] or None,
            keyboard=template["keyboard"] or None
        )
    )
