from aiogram.types import CallbackQuery

from posterbot.services.db.response import ModerManyResponse
from posterbot.routers.menu.menu_main import send_menu_main
from posterbot.utils.answers import (
    TextModerator,
    TextAnswer,
)
from posterbot.services import (
    ModerRequestBuilder,
    ServiceApiSession,
)


async def get_moders(api: ServiceApiSession) -> ModerManyResponse | None:
    request_data = await api.send(ModerRequestBuilder().get_moders())
    if request_data.status == 200:
        return ModerManyResponse.model_validate(
            await request_data.json()
        )
    return None


def get_moders_text(moders: ModerManyResponse) -> str:
    text = TextModerator.MODERATOR_LIST
    for moder in moders.moders:
        text += f"id{moder.id} | {moder.username} | {moder.fullname}\n"
    return text


async def show_moderators(
    callback: CallbackQuery,
    api: ServiceApiSession
) -> None:
    
    moders = await get_moders(api)

    text = get_moders_text(moders) if moders else TextAnswer.OOPS
    
    await callback.message.answer(text)
    await send_menu_main(callback)
