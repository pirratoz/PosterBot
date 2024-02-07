from typing import Any
from uuid import uuid4

from posterbot.models import (
    Template,
    Media,
)


class TemplateStorage:
    def __init__(self) -> None:
        self.storage: dict[int, Template] = {}

    def get_by_id(self, user_id: int) -> Template:
        template = self.storage.get(user_id)
        if template is None:
            template = Template(
                id=None,
                title="",
                text="",
                media=[],
                entities=[],
                keyboard=[]
            )
            self.storage[user_id] = template
        return template

    def clear(self, user_id: int) -> bool:
        try:
            del self.storage[user_id]
        except KeyError:
            return False
        return True


class TemplateAction:
    def __init__(self, storage: TemplateStorage, user_id: int) -> None:
        self.template = storage.get_by_id(user_id)
    
    def get_media(self) -> list[Media]:
        return sorted(self.template["media"], key=lambda v: v["message_id"])

    def set_title(self, title: str) -> None:
        self.template["title"] = title
    
    def set_text(self, text: str) -> None:
        self.template["text"] = text
    
    def set_entities(self, entities: list[dict[str, Any]]) -> None:
        self.template["entities"] = entities
    
    def append_media(self, media: Media) -> str:
        media["uuid"] = str(uuid4())
        self.template["media"].append(media)
        return media["uuid"]
    
    def remove_media(self, uuid: str) -> tuple[bool, Media | None]:
        for media in self.template["media"]:
            if media["uuid"] == uuid:
                self.template["media"].remove(media)
                return (True, media)
        return (False, None)
