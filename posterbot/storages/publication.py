from datetime import datetime

from posterbot.models import Publication


class PublicationStorage:
    def __init__(self) -> None:
        self.storage: dict[int, Publication] = {}

    def get_by_id(self, user_id: int) -> Publication:
        publication = self.storage.get(user_id)
        if publication is None:
            publication = Publication(
                template_id = None,
                publish=None,
                finish=None,
                chat_id=None,
                message_id=None,
                pin=False,
                delete=False,
                published=False,
                deleted=False,
                pinned=False,
                archived=False
            )
            self.storage[user_id] = publication
        return publication

    def clear(self, user_id: int) -> bool:
        try:
            del self.storage[user_id]
        except KeyError:
            return False
        return True


class PublicationAction:
    def __init__(self, storage: PublicationStorage, user_id: int) -> None:
        self.publication = storage.get_by_id(user_id)

    def set_template_id(self, template_id: int) -> None:
        self.publication["template_id"] = template_id

    def set_chat_id(self, chat_id: int) -> None:
        self.publication["chat_id"] = chat_id

    def update_pin_message(self) -> None:
        self.publication["pin"] = not self.publication["pin"]

    def update_delete_message(self) -> None:
        self.publication["delete"] = not self.publication["delete"]

    def publish_date(self, date: datetime) -> None:
        self.publication["publish"] = date
    
    def finish_date(self, date: datetime) -> None:
        self.publication["finish"] = date
