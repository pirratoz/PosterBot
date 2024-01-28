from uvloop import run as uvloop_run

from aiogram import (
    Dispatcher,
    Bot,
)

from source.configs import BotConfig
from source.services import ServiceApiSession


def include_routers(dp: Dispatcher) -> None:
    ...


async def main() -> None:
    config = BotConfig()
    api = ServiceApiSession()
    
    bot = Bot()
    dp = Dispatcher()

    include_routers(dp)

    await dp.start_polling(
        bot,
        api=api,
        config=config,
    )

    await api.session.close()


if __name__ == "__main__":
    uvloop_run(main())
