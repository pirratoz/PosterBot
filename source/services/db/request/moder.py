from source.services.db.request.base_builder import BaseRequestBuilder


class ModerRequestBuilder(BaseRequestBuilder):
    def __init__(self) -> None:
        super().__init__()
        self.base_url = "http://localhost:8000"

    def get_moders(self) -> "ModerRequestBuilder":
        self.method = "GET"
        self.path = "/moders"
        return self

    def get_moder(self, user_id: int) -> "ModerRequestBuilder":
        self.method = "GET"
        self.path = f"/moders/{user_id}"
        return self

    def create_moder(self, user_id: int, fullname: str, username: str) -> "ModerRequestBuilder":
        self.method = "POST"
        self.path = "/moders"
        self.json = {
            "id": user_id,
            "fullname": fullname,
            "username": username,
        }
        return self

    def delete_moder(self, user_id: int) -> "ModerRequestBuilder":
        self.method = "DELETE"
        self.path = f"/moders/{user_id}"
        return self
