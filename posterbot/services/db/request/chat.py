from posterbot.services.db.request.base_builder import BaseRequestBuilder


class ChatRequestBuilder(BaseRequestBuilder):
    def __init__(self) -> None:
        super().__init__()
        self.base_url = "http://localhost:8000"
    
    def get_chats(self) -> "ChatRequestBuilder":
        self.method = "GET"
        self.path = "/chats"
        return self
    
    def get_chat(self, chat_id: int) -> "ChatRequestBuilder":
        self.method = "GET"
        self.path = f"/chats/{chat_id}"
        return self

    def create_chat(self, chat_id: int, title: str) -> "ChatRequestBuilder":
        self.method = "POST"
        self.path = "/chats"
        self.json = {
            "id": chat_id,
            "title": title,
        }
        return self

    def delete_chat(self, chat_id: int) -> "ChatRequestBuilder":
        self.method = "DELETE"
        self.path = f"/chats/{chat_id}"
        return self
