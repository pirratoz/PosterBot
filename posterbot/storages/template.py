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
        if template:
            return template
        return Template(
            title="",
            text="",
            media=[],
            entities=[],
            keyboard=[]
        )

    def clear(self, user_id: int) -> None:
        if not self.storage.get(user_id):
            return None
        try:
            del self.storage[user_id]
        except KeyError:
            ...


class TemplateAction:
    def __init__(self, storage: TemplateStorage, user_id: int) -> None:
        self.template = storage.get_by_id(user_id)
        self.user_id: int

    def set_title(self, title: str) -> None:
        self.template["title"] = title
    
    def set_text(self, text: str) -> None:
        self.template["text"] = text
    
    def append_media(self, media: Media) -> str:
        media["uuid"] = str(uuid4())
        self.template["media"].append(media)
        return media["uuid"]
    
    def remove_media(self, uuid: str) -> bool:
        for media in self.template["media"]:
            if media["uuid"] == uuid:
                self.template["media"].remove(media)
                return True
        return False
