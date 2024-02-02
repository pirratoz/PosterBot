from posterbot.services.db.request.base_builder import BaseRequestBuilder
from posterbot.models import Template

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

    def create_template(self, template: Template) -> "TemplateRequestBuilder":
        self.method = "POST"
        self.json = template
        return self

    def delete_template(self, template_id: int) -> "TemplateRequestBuilder":
        self.method = "DELETE"
        self.path = f"/templates/{template_id}"
        return self
