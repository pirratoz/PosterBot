from posterbot.services.db.request.base_builder import BaseRequestBuilder
from posterbot.models import Publication


class PublicationRequestBuilder(BaseRequestBuilder):
    def __init__(self) -> None:
        super().__init__()
        self.base_url = "http://localhost:8000"
    
    def get_publication_active(self) -> "PublicationRequestBuilder":
        self.method = "GET"
        self.path = "/publications"
        return self

    def get_publication_for_chat(self, chat_id: int) -> "PublicationRequestBuilder":
        self.method = "GET"
        self.path = f"/publications/{chat_id}"
        return self

    def get_publication(self, publication_id: int) -> "PublicationRequestBuilder":
        self.method = "GET"
        self.path = f"/publications/{publication_id}"
        return self

    def create_publication(self, publication: Publication) -> "PublicationRequestBuilder":
        self.method = "POST"
        self.path = "/publications"
        self.json = publication
        return self

    def delete_publication(self, publication_id: int) -> "PublicationRequestBuilder":
        self.method = "DELETE"
        self.path = f"/publications/{publication_id}"
        return self
