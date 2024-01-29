from asyncio import gather as asyncio_gather

from aiogram.types import Message
from aiogram import Bot

from source.configs import BotConfig
from source.utils import AnswerText
from source.keyboards import get_kb_moder_menu


async def request_moder_status(
    message: Message,
    bot: Bot,
    config: BotConfig
) -> None:
    await message.answer(
        text=AnswerText.request_get_moderator
    )
    
    keyboard = get_kb_moder_menu(message.from_user.id)
    text = AnswerText.user_send_request_get_moderator.format(
        fullname=message.from_user.full_name,
        username=message.from_user.username
    )

    tasks = [
        bot.send_message(owner_chat_id, text, reply_markup=keyboard)
        for owner_chat_id in config.OWNERS
    ]

    await asyncio_gather(*tasks)
