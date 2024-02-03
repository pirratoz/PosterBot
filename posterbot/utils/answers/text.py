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


class TextModeratorRegexp:
    def get_name(text: str) -> Name:
        return Name(
            fullname=search("(?<=fullname: )[\S ]+", text)[0],
            username=search("(?<=username: )[\S ]+", text)[0]
        )
