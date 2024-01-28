from source.services.db.request.base_builder import (
    BaseUrlBuilder,
    RequestData,
)


class ModerRequestBuilder(BaseUrlBuilder):
    def __init__(self) -> None:
        super().__init__()
        self.base_url = "http://localhost:8000"

    def get_moders(self) -> RequestData:
        self.type_request = "GET"
        self.path = "/moders"
        return self.dump()

    def get_moder(self, user_id: int) -> RequestData:
        self.type_request = "GET"
        self.path = f"/moders/{user_id}"
        return self.dump()

    def create_moder(self, user_id: int, fullname: str, username: str) -> RequestData:
        self.type_request = "POST"
        self.path = "/moders"
        self.data = {
            "id": user_id,
            "fullname": fullname,
            "username": username,
        }
        return self.dump()

    def delete_moder(self, user_id: int) -> RequestData:
        self.type_request = "DELETE"
        self.path = f"/moders/{user_id}"
        return self.dump()
