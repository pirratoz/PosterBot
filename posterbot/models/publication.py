from typing import TypedDict
from datetime import datetime


class Publication(TypedDict):
    template_id: int | None
    publish: datetime | None
    finish: datetime | None
    chat_id: int | None
    message_id: int | None
    pin: bool
    delete: bool
    published: bool
    deleted: bool
    pinned: bool
    archived: bool
