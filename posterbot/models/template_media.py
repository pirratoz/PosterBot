from typing import (
    TypedDict,
    Any,
)


class Media(TypedDict):
    file_id: str
    type: str
    uuid: str


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
