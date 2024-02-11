from aiogram.types import CallbackQuery
from aiogram import Bot

from posterbot.utils.commands import ModeratorCallbackRegexp
from posterbot.utils.functions import get_role
from posterbot.utils.answers import (
    TextModerator,
    TextAnswer,
)
from posterbot.services import (
    ModerRequestBuilder,
    ServiceApiSession,
)


async def delete_moder(callback: CallbackQuery, api: ServiceApiSession) -> bool:
    user_id = ModeratorCallbackRegexp.get_user(callback.data).id
    request_data = await api.send(ModerRequestBuilder().delete_moder(user_id))
    return request_data.status == 200


async def send_messages(
    callback: CallbackQuery, 
    status_code: int,
    bot: Bot
) -> None:
    user_id = ModeratorCallbackRegexp.get_user(callback.data)
    text = TextModerator.STATUS_DOWNGRADED
    
    if status_code == 200:
        await callback.message.answer(text)
        await bot.send_message(user_id, text)
    else:
        await callback.message.answer(TextAnswer.OOPS)


async def reject_status_moderator(
    callback: CallbackQuery,
    api: ServiceApiSession,
    bot: Bot
) -> None:
    
    user_id = ModeratorCallbackRegexp.get_user(callback.data).id

    role = await get_role(user_id, api)
    
    if role.is_moder:
        status_code = await delete_moder(callback, api)
        await send_messages(callback, status_code, bot)
    else:
        await callback.message.answer(TextModerator.STATUS_REQUEST_REJECTED)

    await callback.message.delete()
