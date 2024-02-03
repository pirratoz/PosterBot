from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

from posterbot.utils.commands import ModeratorCallbackBuilder
from posterbot.utils.answers import ModeratorButtonText


def kb_request_status_moderator(user_id: int | str) -> InlineKeyboardMarkup:
    btn_accept = InlineKeyboardButton(
        text=ModeratorButtonText.ACCEPT_STATUS_MODERATOR,
        callback_data=ModeratorCallbackBuilder.accept_moderator(user_id)
    )
    btn_reject = InlineKeyboardButton(
        text=ModeratorButtonText.REJECT_STATUS_MODERATOR,
        callback_data=ModeratorCallbackBuilder.reject_moderator(user_id)
    )
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [btn_accept, btn_reject]
        ]
    )
