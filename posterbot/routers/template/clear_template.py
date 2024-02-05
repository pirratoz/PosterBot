from aiogram.types import CallbackQuery

from posterbot.utils.answers import TextTemplate
from posterbot.storages import TemplateStorage


async def clear_template(
    callback: CallbackQuery,
    storage_tmp: TemplateStorage
) -> None:

    storage_tmp.clear(callback.message.chat.id)

    await callback.message.answer(TextTemplate.TEMPLATE_CLEARED)
    await callback.answer()
