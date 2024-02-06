from aiogram.types import CallbackQuery

from posterbot.utils.answers import TextTemplate
from posterbot.storages import TemplateStorage


async def clear_template(
    callback: CallbackQuery,
    storage_tmp: TemplateStorage
) -> None:

    text = TextTemplate.TEMPLATE_IS_EMPTY
    if storage_tmp.clear(callback.message.chat.id):
        text = TextTemplate.TEMPLATE_CLEARED
    
    await callback.message.answer(text)

    await callback.answer()
