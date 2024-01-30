__all__ = [
    "router_moder",
]

from aiogram.enums import ChatType
from aiogram import (
    Router,
    F,
)

from source.utils import CallbackButton
from source.routers.moder.accept_moder_status import accept_moder_status
from source.routers.moder.reject_moder_status import reject_moder_status
from source.routers.moder.demote_moder_list import demote_moderator_list
from source.routers.moder.demote_moder_status import demote_moderator_status
from source.routers.moder.show_moderators import show_moderators
from source.routers.moder.request_moder_status import request_moder_status
from source.routers.moder.moder_action_kb import moder_action_kb_menu

router_moder = Router(name="moder")

router_moder.message.register(
    request_moder_status,
    (F.text == "/add_moder") &
    (F.chat.type == ChatType.PRIVATE)
)

router_moder.callback_query.register(
    accept_moder_status,
    F.data.startswith(CallbackButton.request_moder_accept)
)

router_moder.callback_query.register(
    reject_moder_status,
    F.data.startswith(CallbackButton.request_moder_reject)
)

router_moder.callback_query.register(
    demote_moderator_list,
    F.data == CallbackButton.demote_moder_list
)

router_moder.callback_query.register(
    demote_moderator_status,
    F.data.startswith(CallbackButton.demote_moder)
)

router_moder.callback_query.register(
    show_moderators,
    F.data == CallbackButton.show_moders
)

router_moder.callback_query.register(
    moder_action_kb_menu,
    F.data == CallbackButton.moder_kb
)
