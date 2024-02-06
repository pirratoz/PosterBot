from dataclasses import dataclass
from re import search


@dataclass
class Name:
    fullname: str
    username: str


class TextAnswer:
    OOPS = "Что-то пошло не так!"


class TextModerator:
    REQUEST_SENDED = "Заявка на получение статуса модератора отправлена!"
    NEW_REQUEST_FOR_MODERATOR_STATUS = "Статус модератора запрашивает:\n" \
                                       "fullname: {fullname}\n" \
                                       "username: @{username}"
    USER_ALREADY_MODERATOR = "Пользователь уже имеет статус модератора"
    USER_IS_NOT_MODERATOR = "Пользователь не имеет статуса модератора"
    STATUS_REQUEST_REJECTED = "Запрос на повышение отклонён"
    STATUS_UPGRADED = "Статус повышен"
    STATUS_DOWNGRADED = "Статус понижен"
    WHO_TO_DEMOTE = "Кого понижать"    
    MODERATOR_LIST = "Список модераторов:\n"


class TextModeratorRegexp:
    @staticmethod
    def get_name(text: str) -> Name:
        return Name(
            fullname=search("(?<=fullname: )[\S ]+", text)[0],
            username=search("(?<=username: )[\S ]+", text)[0]
        )


class TextTemplate:
    AWAIT_TITLE_TEMPLATE = "Введите название для шаблона"
    TITLE_TEMPLATE_NOT_BE_NONE = "Название шаблона должно состоять из символов"
    TITLE_SETTED = "Название шаблона установлено: {title}"
    TEMPLATE_CLEARED = "Шаблон очищен"
    TEMPLATE_IS_EMPTY = "Шаблон пуст"
    TEMPLATE_FILL_MODE_ENABLED = "Включен режим заполнения шаблона"
    TEMPLATE_FILL_MODE_DISABLED = "Выключен режим заполнения шаблона"

    TEXT_UPDATED = "Текст обновлён"
    VIDEO_APPEND = "Видео добавлено"
    PHOTO_APPEND = "Фото добавлено"
    VIDEO_REMOVED = "Видео удалено"
    PHOTO_REMOVED = "Фото удалено"
