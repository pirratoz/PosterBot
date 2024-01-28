from datetime import datetime

from source.services.db.request.base_builder import (
    BaseUrlBuilder,
    RequestData,
)


class PublicationRequestBuilder(BaseUrlBuilder):
    def __init__(self) -> None:
        super().__init__()
        self.base_url = "http://localhost:8000"
    
    async def get_publication_active(self) -> RequestData:
        self.type_request = "GET"
        self.path = "/publications"
        return self.dump()

    async def get_publication_for_chat(self, chat_id: int) -> RequestData:
        self.type_request = "GET"
        self.path = f"/publications/{chat_id}"
        return self.dump()

    async def get_publication(self, publication_id: int) -> RequestData:
        self.type_request = "GET"
        self.path = f"/publications/{publication_id}"
        return self.dump()

    async def create_publication(
        self,
        template_id: int,
        publish: datetime,
        finish: datetime,
        chat_id: int,
        pin: bool | None = None,
        delete: bool | None = None
    ) -> RequestData:
        self.type_request = "POST"
        self.path = "/publications"
        self.data = {
            "template_id": template_id,
            "publish": publish,
            "finish": finish,
            "chat_id": chat_id,
            "message_id": None,
            "pin": pin or False,
            "delete": delete or False,
            "published": False,
            "deleted": False,
            "pinned": False,
            "archived": False,
        }
        return self.dump()

    async def delete_publication(self, publication_id: int) -> RequestData:
        self.type_request = "DELETE"
        self.path = f"/publications/{publication_id}"
        return self.dump()
