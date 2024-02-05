from aiogram.fsm.state import (
    StatesGroup,
    State,
)


class TemplateStates(StatesGroup):
    set_title = State()
    fill_tmp = State()
