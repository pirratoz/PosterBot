from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

from source.utils import CallbackButton
from source.services.db import ModerResponse


def get_kb_demote_moder_menu(moders: list[ModerResponse]) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
            InlineKeyboardButton(
                text=moder.fullname,
                callback_data=CallbackButton.demote_moder + str(moder.id)
            )
            ]
            for moder in moders
        ]
    )
