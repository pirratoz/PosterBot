from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

from source.utils import (
    AnswerButton,
    CallbackButton,
)


def get_kb_main_menu() -> InlineKeyboardMarkup:
    btn_moder_kb = InlineKeyboardButton(
        text=AnswerButton.moder_kb,
        callback_data=CallbackButton.moder_kb
    )
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [btn_moder_kb]
        ]
    )
