from source.services.db.request.base_builder import (
    BaseUrlBuilder,
    RequestData,
)


class ChatRequestBuilder(BaseUrlBuilder):
    def __init__(self) -> None:
        super().__init__()
        self.base_url = "http://localhost:8000"
    
    async def get_chats(self) -> RequestData:
        self.type_request = "GET"
        self.path = "/chats"
        return self.dump()
    
    async def get_chat(self, chat_id: int) -> RequestData:
        self.type_request = "GET"
        self.path = f"/chats/{chat_id}"
        return self.dump()

    async def create_chat(self, chat_id: int, title: str) -> RequestData:
        self.type_request = "POST"
        self.path = "/chats"
        self.data = {
            "id": chat_id,
            "title": title,
        }
        return self.dump()

    async def delete_chat(self, chat_id: int) -> RequestData:
        self.type_request = "DELETE"
        self.path = f"/chats/{chat_id}"
        return self.dump()
