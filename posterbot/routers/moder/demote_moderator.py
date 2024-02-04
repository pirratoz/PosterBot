from aiogram.types import CallbackQuery

from posterbot.utils.commands import ModeratorCallbackRegexp
from posterbot.utils.answers import (
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


async def delete_moder(callback: CallbackQuery, api: ServiceApiSession) -> int:
    user_id = ModeratorCallbackRegexp.get_user(callback.data).id
    request_data = await api.send(ModerRequestBuilder().delete_moder(user_id))
    return request_data.status


async def send_messages(callback: CallbackQuery, status_code: int) -> None:
    await callback.message.answer(
        TextModerator.STATUS_DOWNGRADED if status_code == 200 else TextAnswer.OOPS
    )


async def demote_status_moderator(
    callback: CallbackQuery,
    api: ServiceApiSession
) -> None:
    
    user_id = ModeratorCallbackRegexp.get_user(callback.data).id
    
    if await is_moder(user_id, api):
        status_code = await delete_moder(callback, api)
        await send_messages(callback, status_code)
    else:
        await callback.message.answer(TextModerator.USER_IS_NOT_MODERATOR)

    await callback.message.delete()
