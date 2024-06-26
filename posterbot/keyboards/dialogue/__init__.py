__all__ = [
    "kb_confirm_delete_template",
    "kb_request_status_moderator",
    "kb_remove_media_template",
    "kb_demote_moderator",
    "kb_select_template",
    "kb_remove_any_media_template",
]

from posterbot.keyboards.dialogue.request_status_moderator import kb_request_status_moderator
from posterbot.keyboards.dialogue.confirm_delete_template import kb_confirm_delete_template
from posterbot.keyboards.dialogue.remove_media_template import kb_remove_media_template
from posterbot.keyboards.dialogue.remove_any_media import kb_remove_any_media_template
from posterbot.keyboards.dialogue.demote_moderator import kb_demote_moderator
from posterbot.keyboards.dialogue.select_template import kb_select_template
