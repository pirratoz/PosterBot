from aiogram.types import CallbackQuery

from posterbot.keyboards.menu import kb_template_menu
from posterbot.utils.answers.button import MenuButtonText
from posterbot.configs import BotConfig
from posterbot.services import (
    ModerRequestBuilder,
    ServiceApiSession,
)


async def is_moder(user_id: int, api: ServiceApiSession) -> bool:
    request_data = await api.send(ModerRequestBuilder().get_moder(user_id))
    return request_data.status == 200


async def send_menu_template(
    callback: CallbackQuery,
    api: ServiceApiSession,
    config: BotConfig
) -> None:
    
    user_id = callback.message.chat.id

    if user_id in config.OWNERS or await is_moder(user_id, api):
        await callback.message.delete()
        await callback.message.answer(
            text=MenuButtonText.TEMPLATE_MENU,
            reply_markup=kb_template_menu()
        )
