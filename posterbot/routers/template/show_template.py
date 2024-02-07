from aiogram.utils.media_group import MediaGroupBuilder
from aiogram.types import CallbackQuery

from posterbot.storages import (
    TemplateStorage,
    TemplateAction,
)


async def show_template(
    callback: CallbackQuery,
    storage_tmp: TemplateStorage
) -> None:

    storage = TemplateAction(storage_tmp, callback.message.chat.id)

    album_builder = MediaGroupBuilder(
        caption=storage.template["text"],
        caption_entities=storage.template["entities"]
    )

    is_first_attachments = True
    for media in storage.template["media"]:
        album_builder.add(
            type=media["type"],
            media=media["file_id"],
            caption_entities=storage.template["entities"] if is_first_attachments else []
        )
        is_first_attachments = False

    if storage.template["media"]:
        await callback.message.answer_media_group(
            media=album_builder.build()
        )
    else:
        await callback.message.answer(
            text=storage.template["text"],
            entities=storage.template["entities"]
        )

    await callback.answer()
