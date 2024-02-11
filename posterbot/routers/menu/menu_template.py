from aiogram.types import CallbackQuery

from posterbot.keyboards.menu import kb_template_menu
from posterbot.utils.functions import get_role
from posterbot.utils.answers.button import MenuButtonText
from posterbot.services import ServiceApiSession


async def send_menu_template(
    callback: CallbackQuery,
    api: ServiceApiSession
) -> None:

    role = await get_role(callback.message.chat.id, api)

    if role.owner_or_moder:
        await callback.message.delete()
        await callback.message.answer(
            text=MenuButtonText.TEMPLATE_MENU,
            reply_markup=kb_template_menu()
        )
