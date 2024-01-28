from aiohttp import ClientSession
from aiohttp.client import ClientResponse

from source.services.db.request.base_builder import RequestData


class ServiceApiSession:
    def __init__(self) -> None:
        self.session: ClientSession | None = None

    async def __init_session(self) -> None:
        if self.session is None or self.session.closed:
            self.session = ClientSession()

    async def send(self, data: RequestData) -> ClientResponse:
        await self.__init_session()
        kwargs = {
            "url": data.url,
            "params": data.params,
        }

        if data.type == "GET":
            return await self.session.get(**kwargs)
        
        kwargs["data"] = data.data
        if data.type == "POST":
            return await self.session.post(**kwargs)
        elif data.type == "DELETE":
            return await self.session.delete(**kwargs)
