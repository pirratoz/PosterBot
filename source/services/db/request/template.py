from typing import Any

from source.services.db.request.base_builder import BaseRequestBuilder


class TemplateRequestBuilder(BaseRequestBuilder):
    def __init__(self) -> None:
        super().__init__()
        self.base_url = "http://localhost:8000"
    
    def get_templates(self) -> "TemplateRequestBuilder":
        self.method = "GET"
        self.path = "/templates"
        return self

    def get_template(self, template_id: int) -> "TemplateRequestBuilder":
        self.method = "GET"
        self.path = f"/templates/{template_id}"
        return self

    def create_template(
        self,
        title: str,
        from_chat_id: int,
        text_message_id: int,
        photo_ids: list[int] | None = None,
        video_ids: list[int] | None = None,
        keyboard: list[list[dict[str, Any]]] | None = None
    ) -> "TemplateRequestBuilder":
        self.method = "POST"
        self.data = {
            "title": title,
            "from_chat_id": from_chat_id,
            "media": {
                "text_message_id": text_message_id,
                "media_ids": {
                    "photo": photo_ids or [],
                    "video": video_ids or [],
                },
                "keyboard": keyboard or [],
            },
        }
        return self

    def delete_template(self, template_id: int) -> "TemplateRequestBuilder":
        self.method = "DELETE"
        self.path = f"/templates/{template_id}"
        return self
