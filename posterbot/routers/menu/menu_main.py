from aiogram.types import (
    CallbackQuery,
    Message,
)

from posterbot.keyboards.menu import kb_main_menu
from posterbot.utils.answers.button import MenuButtonText


async def send_menu_main(query: CallbackQuery | Message) -> None:

    if isinstance(query, Message):
        function_answer = query.answer
        function_delete_message = query.delete
    else:
        function_answer = query.message.answer
        function_delete_message = query.message.delete

    await function_delete_message()
    
    await function_answer(
        text=MenuButtonText.MAIN_MENU,
        reply_markup=kb_main_menu()
    )
