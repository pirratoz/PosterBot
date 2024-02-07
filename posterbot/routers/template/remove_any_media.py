from aiogram.types import CallbackQuery

from posterbot.keyboards.dialogue import kb_remove_any_media_template
from posterbot.utils.answers import TextTemplate
from posterbot.storages import (
    TemplateStorage,
    TemplateAction,
)


async def remove_any_media(
    callback: CallbackQuery,
    storage_tmp: TemplateStorage
) -> None:
    
    storage = TemplateAction(storage_tmp, callback.message.chat.id)

    if not storage.template["media"]:
        await callback.message.answer(TextTemplate.MEDIA_IS_EMPTY)
        return None
    
    await callback.message.delete()

    await callback.message.answer(TextTemplate.START_LIST_MEDIA)

    for media in storage.template["media"]:
        await callback.message.answer(
            text=TextTemplate.REMOVE_MEDIA,
            reply_markup=kb_remove_any_media_template(media["uuid"])
        )
    
    await callback.message.answer(TextTemplate.END_LIST_MEDIA)
