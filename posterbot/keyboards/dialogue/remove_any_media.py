from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

from posterbot.utils.answers import TemplateButtonText
from posterbot.utils.commands import TemplateCallbackBuilder


def kb_remove_any_media_template(media_message_id: str) -> InlineKeyboardMarkup:
    btn_remove_media = InlineKeyboardButton(
        text=TemplateButtonText.REMOVE_MEDIA,
        callback_data=TemplateCallbackBuilder.remove_media(media_message_id)
    )
    return InlineKeyboardMarkup(inline_keyboard=[
        [btn_remove_media]
    ])
