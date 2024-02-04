from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

from posterbot.services.db.response import ModerManyResponse
from posterbot.utils.commands import ModeratorCallbackBuilder


def kb_demote_moderator(moders: ModerManyResponse) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
            InlineKeyboardButton(
                text=moder.fullname,
                callback_data=ModeratorCallbackBuilder.demote_moderator(moder.id)
            )
            ]
            for moder in moders.moders
        ]
    )
