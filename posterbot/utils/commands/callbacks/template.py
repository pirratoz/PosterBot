from dataclasses import dataclass
from re import search


@dataclass
class MediaInfo:
    message_id: int


class TemplateCallbackData:
    SET_TITLE = "tmp_set_title"
    FILL_TEMPLATE_START = "tmp_fill_s"
    FILL_TEMPLATE_END = "tmp_fill_e"
    CLEAR_TEMPLATE = "tmp_clr"
    CREATE_TEMPLATE = "tmp_crt"
    SHOW_TEMPLATE = "tmp_show"
    REMOVE_MEDIA = "tmp_rm_media"
    REMOVE_MEDIA_LIST = "tmp_rm_media_l"


class TemplateCallbackRegexp:
    @staticmethod
    def get_media_info(callback_data: str) -> MediaInfo:
        pattern = TemplateCallbackData.REMOVE_MEDIA
        return MediaInfo(
            uuid=int(search(f"(?<={pattern}_)[0-9a-z-]+", callback_data)[0])
        )


class TemplateCallbackBuilder:
    @staticmethod
    def remove_media(media_message_id: str) -> str:
        return f"{TemplateCallbackData.REMOVE_MEDIA}_{media_message_id}"
