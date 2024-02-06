from aiogram.types import CallbackQuery
from aiogram.enums import InputMediaType

from posterbot.utils.commands import TemplateCallbackRegexp
from posterbot.utils.answers import TextTemplate
from posterbot.storages import (
    TemplateStorage,
    TemplateAction,
)


async def remove_media(
    callback: CallbackQuery,
    storage_tmp: TemplateStorage
) -> None:
    
    storage = TemplateAction(storage_tmp, callback.message.chat.id)

    uuid = TemplateCallbackRegexp.get_media_info(callback.data).uuid

    result, media = storage.remove_media(uuid)

    text_mapper = {
        InputMediaType.PHOTO.value: TextTemplate.PHOTO_REMOVED,
        InputMediaType.VIDEO.value: TextTemplate.VIDEO_REMOVED,
    }

    await callback.message.delete()

    if result:
        await callback.message.answer(
            text=text_mapper[media["type"]]
        )
