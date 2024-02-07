from dataclasses import dataclass

from aiogram.enums import InputMediaType
from aiogram.types import Message

from posterbot.keyboards.dialogue import kb_remove_media_template
from posterbot.utils.answers import TextTemplate
from posterbot.models import Media
from posterbot.storages import (
    TemplateStorage,
    TemplateAction,
)


@dataclass
class MediaInfo:
    message_id: int
    file_id: str
    type: str
    text: str

    def dump(self) -> Media:
        return Media(message_id=self.message_id, file_id=self.file_id, type=self.type)


def find_media(message: Message) -> MediaInfo:
    media = MediaInfo(message.message_id, "", "", "")

    if message.photo:
        media.file_id = message.photo[-1].file_id
        media.type = InputMediaType.PHOTO.value
        media.text = TextTemplate.PHOTO_APPEND
    elif message.video:
        media.file_id = message.video.file_id
        media.type = InputMediaType.VIDEO.value
        media.text = TextTemplate.VIDEO_APPEND
    
    return media


async def fill_template(
    message: Message,
    storage_tmp: TemplateStorage
) -> None:
    
    storage = TemplateAction(storage_tmp, message.from_user.id)
    markup = kb_remove_media_template

    text = message.text or message.caption

    if text:
        storage.set_text(text)
        storage.set_entities(message.entities)
        await message.reply(
            text=TextTemplate.TEXT_UPDATED,
            reply_markup=markup(None)
        )

    media = find_media(message)
    
    if media.file_id:
        uuid=storage.append_media(media.dump())

        await message.reply(
            text=media.text,
            reply_markup=markup(uuid)
        )
