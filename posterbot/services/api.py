from asyncio import sleep

from aiohttp import ClientSession
from aiohttp.client import ClientResponse

from posterbot.services.db.request.base_builder import BaseRequestBuilder


class ServiceApiSession:
    def __init__(self) -> None:
        self.session: ClientSession | None = None

    async def send(self, builder: BaseRequestBuilder) -> ClientResponse:
        if self.session is None or self.session.closed:
            self.session = ClientSession()
        return await self.session.request(**builder.dump())

    async def close_session(self):
        if self.session is not None and not self.session.closed:
            await self.session.close()
            await sleep(0.250)
