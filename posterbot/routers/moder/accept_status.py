from aiogram.types import CallbackQuery
from aiogram import Bot

from posterbot.utils.commands import ModeratorCallbackRegexp
from posterbot.utils.answers import (
    TextModeratorRegexp,
    TextModerator,
    TextAnswer,
)
from posterbot.services import (
    ModerRequestBuilder,
    ServiceApiSession,
)


async def is_moder(user_id: int, api: ServiceApiSession) -> bool:
    request_data = await api.send(ModerRequestBuilder().get_moder(user_id))
    return request_data.status == 200


async def create_moder(callback: CallbackQuery, api: ServiceApiSession) -> int:
    user_id = ModeratorCallbackRegexp.get_user(callback.data).id
    user_data = TextModeratorRegexp.get_name(callback.message.text)

    request_data = await api.send(ModerRequestBuilder().create_moder(
        user_id=user_id,
        fullname=user_data.fullname,
        username=user_data.username
    ))

    return request_data.status


async def send_messages(
    callback: CallbackQuery, 
    status_code: int,
    bot: Bot
) -> None:
    user_id = ModeratorCallbackRegexp.get_user(callback.data).id
    text = TextModerator.STATUS_UPGRADED
    
    if status_code == 201:
        await callback.message.answer(text)
        await bot.send_message(user_id, text)
    else:
        await callback.message.answer(TextAnswer.OOPS)


async def accept_status_moderator(
    callback: CallbackQuery,
    api: ServiceApiSession,
    bot: Bot
) -> None:
    
    user_id = ModeratorCallbackRegexp.get_user(callback.data).id
    
    if await is_moder(user_id, api):
        await callback.message.answer(TextModerator.USER_ALREADY_MODERATOR)
    else:
        status_code = await create_moder(callback, api)
        await send_messages(callback, status_code, bot)
    
    await callback.message.delete()
