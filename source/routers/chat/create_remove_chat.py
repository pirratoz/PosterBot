from asyncio import sleep

from aiogram.types import Message

from source.configs import BotConfig
from source.utils import AnswerText
from source.services import ServiceApiSession
from source.services.db import ChatRequestBuilder


async def __create_chat(api: ServiceApiSession, chat_id: int, title: str) -> str:
    response_request = await api.send(
        ChatRequestBuilder().create_chat(chat_id, title)
    )

    if response_request.status == 201:
        return AnswerText.chat_created
    return AnswerText.something_went_wrong


async def __remove_chat(api: ServiceApiSession, chat_id: int) -> str:
    response_request = await api.send(
        ChatRequestBuilder().delete_chat(chat_id)
    )

    if response_request.status == 200:
        return AnswerText.chat_removed
    return AnswerText.something_went_wrong


async def create_remove_chat(
    message: Message,
    config: BotConfig,
    api: ServiceApiSession
) -> None:
    
    await message.delete()
    
    chat_id = message.chat.id
    chat_title = message.chat.title
    
    if message.from_user.id not in config.OWNERS:
        return None
    
    if chat_title is None:
        return None
    
    response_request = await api.send(
        ChatRequestBuilder().get_chat(chat_id)
    )

    if response_request.status == 404:
        text = await __create_chat(api, chat_id, chat_title)
    else:
        text = await __remove_chat(api, chat_id)

    answer = await message.answer(text=text)
    await sleep(10)
    await answer.delete()
