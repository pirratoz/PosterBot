__all__ = [
    "router_moder",
]

from aiogram import Router

from posterbot.routers.moder.show_moderators_for_demote import show_moderators_for_demote
from posterbot.routers.moder.demote_moderator import demote_status_moderator
from posterbot.routers.moder.request_status import request_status_moderator
from posterbot.routers.moder.accept_status import accept_status_moderator
from posterbot.routers.moder.reject_status import reject_status_moderator
from posterbot.routers.moder.show_moderators import show_moderators

from posterbot.utils.filters import ModeratorFilter


router_moder = Router(name="moder")


router_moder.message.register(
    request_status_moderator,
    *ModeratorFilter.REQUEST_STATUS_MODERATOR()
)

router_moder.callback_query.register(
    show_moderators,
    *ModeratorFilter.SHOW_MODERATORS()
)

router_moder.callback_query.register(
    accept_status_moderator,
    *ModeratorFilter.ACCEPT_STATUS_MODERATOR()
)

router_moder.callback_query.register(
    reject_status_moderator,
    *ModeratorFilter.REJECT_STATUS_MODERATOR()
)

router_moder.callback_query.register(
    show_moderators_for_demote,
    *ModeratorFilter.SHOW_MODERATORS_FOR_DEMOTE()
)

router_moder.callback_query.register(
    demote_status_moderator,
    *ModeratorFilter.DEMOTE_STATUS_MODERATOR()
)
