from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

from posterbot.utils.answers import TemplateButtonText
from posterbot.utils.commands import (
    TemplateCallbackData,
    TemplateCallbackBuilder,
)


def kb_remove_media_template(media_message_id: str | None = None) -> InlineKeyboardMarkup:
    btn_remove_media = InlineKeyboardButton(
        text=TemplateButtonText.REMOVE_MEDIA,
        callback_data=TemplateCallbackBuilder.remove_media(media_message_id)
    )
    btn_stop_fill_tmp = InlineKeyboardButton(
        text=TemplateButtonText.STOP_FILL_TEMPLATE,
        callback_data=TemplateCallbackData.FILL_TEMPLATE_END
    )
    if media_message_id is None:
        inline_keyboard=[
            [btn_stop_fill_tmp]
        ]
    else:
        inline_keyboard=[
            [btn_remove_media, btn_stop_fill_tmp]
        ]
    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
