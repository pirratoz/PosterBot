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
    STATUS_REQUEST_REJECTED = "Запрос на повышение отклонён"
    STATUS_UPGRADED = "Статус повышен"
    STATUS_DOWNGRADED = "Статус понижен"


class TextModeratorRegexp:
    @staticmethod
    def get_name(text: str) -> Name:
        return Name(
            fullname=search("(?<=fullname: )[\S ]+", text)[0],
            username=search("(?<=username: )[\S ]+", text)[0]
        )
