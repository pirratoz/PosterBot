from uvloop import run as uvloop_run

from aiogram import (
    Dispatcher,
    Bot,
)

from posterbot.configs import BotConfig
from posterbot.services import ServiceApiSession
from posterbot.routers import router_moder


def include_routers(dp: Dispatcher) -> None:
    dp.include_routers(
        router_moder,
    )


async def main() -> None:   
    config = BotConfig()
    api = ServiceApiSession()

    bot = Bot(token=config.TOKEN)
    dp = Dispatcher()

    include_routers(dp)

    await dp.start_polling(
        bot,
        api=api,
        config=config,
    )

    await api.close_session()


if __name__ == "__main__":
    uvloop_run(main())
