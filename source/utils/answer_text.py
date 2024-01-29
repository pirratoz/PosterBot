from html import escape


class AnswerText:
    request_get_moderator = "Запрос на получение статуса модератора отправлен"
    user_send_request_get_moderator = "Запрос на получение статуса 'МОДЕРАТОР'\nfullname: {fullname}\nusername: @{username}\n"
    
    __request_get_moder = "Запрос на получение статуса 'МОДЕРАТОР'\n<b> {status} </b>"
    owner_accept_request_get_moderator = __request_get_moder.format(
        status=escape('==> ПРИНЯТ <==')
    )
    owner_reject_request_get_moderator = __request_get_moder.format(
        status=escape('==> ОТКЛОНЁН <==')
    )

    moder_already_created = "Пользователь и так модератор!"
    something_went_wrong = "Что-то пошло не так"