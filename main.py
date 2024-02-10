from uvloop import run as uvloop_run

from aiogram import (
    Dispatcher,
    Bot,
)

from posterbot.configs import BotConfig
from posterbot.services import ServiceApiSession
from posterbot.storages import TemplateStorage
from posterbot.routers import (
    router_menu,
    router_moder,
    router_template,
    router_publication,
)


def include_routers(dp: Dispatcher) -> None:
    dp.include_routers(
        router_menu,
        router_moder,
        router_template,
        router_publication,
    )


async def main() -> None:   
    config = BotConfig()
    api = ServiceApiSession()
    storage_tmp = TemplateStorage()

    bot = Bot(token=config.TOKEN)
    dp = Dispatcher()

    include_routers(dp)

    await dp.start_polling(
        bot,
        api=api,
        config=config,
        storage_tmp=storage_tmp
    )

    await api.close_session()


if __name__ == "__main__":
    uvloop_run(main())
