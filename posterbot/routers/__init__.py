__all__ = [
    "router_template",
    "router_moder",
    "router_menu",
    "router_chat",
    "router_publication",
]

from posterbot.routers.publication import router_publication
from posterbot.routers.template import router_template
from posterbot.routers.moder import router_moder
from posterbot.routers.menu import router_menu
from posterbot.routers.chat import router_chat
