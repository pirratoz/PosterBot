from typing import TypedDict
from datetime import datetime


class Publication(TypedDict):
    template_id: int
    publish: datetime
    finish: datetime
    chat_id: int
    message_id: int | None
    pin: bool
    delete: bool
    published: bool
    deleted: bool
    pinned: bool
    archived: bool
