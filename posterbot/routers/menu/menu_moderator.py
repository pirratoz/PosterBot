from aiogram.types import CallbackQuery

from posterbot.keyboards.menu import kb_moderator_menu
from posterbot.utils.answers.button import MenuButtonText


async def send_menu_moderator(callback: CallbackQuery) -> None:
    await callback.message.delete()
    await callback.message.answer(
        text=MenuButtonText.MODERATOR_MENU,
        reply_markup=kb_moderator_menu()
    )
