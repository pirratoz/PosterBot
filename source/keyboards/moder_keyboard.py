from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

from source.utils import (
    AnswerButton,
    CallbackButton,
)


def get_kb_moder_menu_action() -> InlineKeyboardMarkup:
    btn_show_moders = InlineKeyboardButton(
        text=AnswerButton.show_moder_list,
        callback_data=CallbackButton.show_moders
    )
    btn_demote_moder = InlineKeyboardButton(
        text=AnswerButton.demote_moder,
        callback_data=CallbackButton.demote_moder_list
    )
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [btn_show_moders],
            [btn_demote_moder]
        ]
    )
