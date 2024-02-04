from asyncio import gather as asyncio_gather

from aiogram.types import Message
from aiogram import Bot

from posterbot.keyboards.dialogue import kb_request_status_moderator
from posterbot.utils.answers import TextModerator
from posterbot.configs import BotConfig
from posterbot.services import (
    ModerRequestBuilder,
    ServiceApiSession,
)


async def is_moder(user_id: int, api: ServiceApiSession) -> bool:
    request_data = await api.send(ModerRequestBuilder().get_moder(user_id))
    return request_data.status == 200


async def send_request(
    message: Message,
    config: BotConfig,
    bot: Bot
) -> None:
    text = TextModerator.NEW_REQUEST_FOR_MODERATOR_STATUS.format(
        fullname=message.from_user.full_name,
        username=message.from_user.username
    )
    markup = kb_request_status_moderator(message.from_user.id)
    
    await asyncio_gather(*[
        bot.send_message(chat_id=owner_id, text=text, reply_markup=markup)
        for owner_id in config.OWNERS
    ])

    await message.answer(TextModerator.REQUEST_SENDED)


async def request_status_moderator(
    message: Message,
    config: BotConfig,
    api: ServiceApiSession,
    bot: Bot
) -> None:
    
    if await is_moder(message.from_user.id, api):
        return None

    await send_request(message, config, bot)
