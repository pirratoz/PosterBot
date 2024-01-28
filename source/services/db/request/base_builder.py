from dataclasses import dataclass
from typing import (
    Literal,
    Any,
)


@dataclass
class RequestData:
    type: Literal["GET","POST","DELETE"]
    params: dict[str, Any]
    data: dict[str, Any]
    url: str


class BaseUrlBuilder:
    def __init__(self) -> None:
        self.type_request: Literal["GET","POST","DELETE"] = "GET"
        self.params: dict[str, Any] = {}
        self.data: dict[str, Any] = {}
        self.base_url: str = ""
        self.path: str = ""

    def __clear(self) -> None:
        self.type_request = "GET"
        self.params = {}
        self.data = {}
        self.path = ""

    def dump(self) -> RequestData:
        data = RequestData(
            type=self.type_request,
            params=self.params,
            data=self.data,
            url=f"{self.base_url}{self.path}"
        )
        self.__clear()
        return data
