__all__ = [
    "router_menu",
]

from aiogram import Router

from posterbot.routers.menu.menu_moderator import send_menu_moderator
from posterbot.routers.menu.menu_main import send_menu_main

from posterbot.utils.filters import MenuFilter


router_menu = Router(name="menu")


router_menu.callback_query.register(
    send_menu_moderator,
    *MenuFilter.MODERATOR_MENU()
)

router_menu.callback_query.register(
    send_menu_main,
    *MenuFilter.MAIN_MENU()
)

router_menu.message.register(
    send_menu_main,
    *MenuFilter.MAIN_MENU()
)
