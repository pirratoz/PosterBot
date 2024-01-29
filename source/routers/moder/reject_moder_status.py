from aiogram.types import CallbackQuery
from aiogram import Bot

from source.utils import AnswerText


async def reject_moder_status(
    callback: CallbackQuery,
    bot: Bot,
) -> None:

    user_id_requesting_moderator: int = int(callback.data.split("_")[-1])
    text = AnswerText.owner_reject_request_get_moderator

    await bot.send_message(user_id_requesting_moderator, text, parse_mode="html")
    await callback.message.answer(text, parse_mode="html")
    await callback.message.delete()
