from dataclasses import dataclass
from re import search


@dataclass
class User:
    id: int


class ModeratorCallbackData:
    SHOW_MODERATORS_FOR_DEMOTE = "show_moderators_for_demote"
    ACCEPT_STATUS_MODERATOR = "accept_status_moderator"
    REJECT_STATUS_MODERATOR = "reject_status_moderator"
    SHOW_MODERATORS = "show_moderators"
    DEMOTE_MODERATOR = "demote_moderator"


class ModeratorCallbackRegexp:
    @staticmethod
    def get_user(callback_data: str) -> User:
        patterns_id = (
            ModeratorCallbackData.ACCEPT_STATUS_MODERATOR,
            ModeratorCallbackData.REJECT_STATUS_MODERATOR,
            ModeratorCallbackData.DEMOTE_MODERATOR,
        )
        for pattern_id in patterns_id:
            if callback_data.startswith(pattern_id):
                break
        return User(
            id=int(search(f"(?<={pattern_id}_)\d+", callback_data)[0])
        )


class ModeratorCallbackBuilder:
    @staticmethod
    def accept_moderator(user_id: int | str) -> str:
        return f"{ModeratorCallbackData.ACCEPT_STATUS_MODERATOR}_{user_id}"
    
    @staticmethod
    def reject_moderator(user_id: int | str) -> str:
        return f"{ModeratorCallbackData.REJECT_STATUS_MODERATOR}_{user_id}"
    
    @staticmethod
    def demote_moderator(user_id: int | str) -> str:
        return f"{ModeratorCallbackData.DEMOTE_MODERATOR}_{user_id}"
