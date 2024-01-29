from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

from source.utils import (
    CallbackButton,
    AnswerButton,
)


def get_kb_moder_menu(user_id: int | str) -> InlineKeyboardMarkup:
    btn_accept = InlineKeyboardButton(
        text=AnswerButton.request_moder_accept,
        callback_data=CallbackButton.request_moder_accept + str(user_id)
    )
    btn_reject = InlineKeyboardButton(
        text=AnswerButton.request_moder_reject,
        callback_data=CallbackButton.request_moder_reject + str(user_id)
    )
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [btn_accept, btn_reject]
        ]
    )
