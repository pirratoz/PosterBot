from uvloop import run as uvloop_run

from aiogram import (
    Dispatcher,
    Bot,
)

from source.configs import BotConfig
from source.services import ServiceApiSession

from source.routers import (
    router_start,
    router_moder,
)


def include_routers(dp: Dispatcher) -> None:
    dp.include_routers(
        router_start,
        router_moder,
    )


async def moke(*args, **kwargs):
    print(args[0].dump())


async def main() -> None:   
    config = BotConfig()
    api = ServiceApiSession()
    # api.send = moke

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
