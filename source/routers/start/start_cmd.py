from aiogram.types import Message

from source.utils import AnswerText
from source.keyboards import get_kb_main_menu


async def handle_start_cmd(message: Message) -> None:
    await message.answer(
        text=AnswerText.main_menu,
        reply_markup=get_kb_main_menu()
    )
