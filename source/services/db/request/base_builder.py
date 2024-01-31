from typing import (
    Literal,
    Any,
)


class BaseRequestBuilder:
    def __init__(self) -> None:
        self.method: Literal["GET","POST","DELETE"] = "GET"
        self.params: dict[str, Any] | None = None
        self.json: dict[str, Any] | None = None
        self.base_url: str = ""
        self.path: str = ""

    def __clear(self) -> None:
        self.method = "GET"
        self.params = None
        self.json = None
        self.path = ""

    def dump(self) -> dict[str, Any]:
        request_data = {
            "method": self.method,
            "params": self.params,
            "json": self.json,
            "url": f"{self.base_url}{self.path}",
        }
        self.__clear()
        return request_data
