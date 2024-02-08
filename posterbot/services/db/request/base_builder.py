from typing import (
    TypedDict,
    TypeVar,
    Literal,
    Any,
)


T_method = TypeVar("T_method", bound=Literal["GET", "POST", "DELETE", "PUT"])


class RequestData(TypedDict):
    method: T_method
    params: dict[str, Any] | None
    json: dict[str, Any] | None
    url: str


class BaseRequestBuilder:
    def __init__(self) -> None:
        self.method: T_method = "GET"
        self.params: dict[str, Any] | None = None
        self.json: dict[str, Any] | None = None
        self.base_url: str = ""
        self.path: str = ""

    def __clear(self) -> None:
        self.method = "GET"
        self.params = None
        self.json = None
        self.path: str = ""

    def dump(self) -> RequestData:
        request_data = RequestData(
            method=self.method,
            params=self.params,
            json=self.json,
            url=f"{self.base_url}{self.path}"
        )
        self.__clear()
        return request_data
