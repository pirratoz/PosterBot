from asyncio import sleep

from aiogram.types import Message

from posterbot.services.db.request import ChatRequestBuilder
from posterbot.services import ServiceApiSession
from posterbot.utils.functions import get_role
from posterbot.utils.answers import (
    TextAnswer,
    TextChat,
)


async def delete_chat(chat_id: int, api: ServiceApiSession) -> bool:
    return (await api.send(
        ChatRequestBuilder().delete_chat(chat_id)
    )).status == 200


async def create_chat(chat_id: int, title: str, api: ServiceApiSession) -> bool:
    return (await api.send(
        ChatRequestBuilder().create_chat(chat_id, title)
    )).status == 201


async def handle_chat(
    message: Message,
    api: ServiceApiSession,
) -> None:
    
    role = await get_role(message.from_user.id, api)

    if not role.owner_or_moder:
        return None

    await message.delete()

    text = TextAnswer.OOPS
    chat_id = message.chat.id
    title = message.chat.title

    status = (await api.send(
        ChatRequestBuilder().get_chat(chat_id)
    )).status

    if status == 200 and (await delete_chat(chat_id, api)):
        text = TextChat.CHAT_REMOVED
    elif status == 404 and (await create_chat(chat_id, title, api)):
        text = TextChat.CHAT_APPEND

    message_answer = await message.answer(text)

    await sleep(15)

    await message_answer.delete()
