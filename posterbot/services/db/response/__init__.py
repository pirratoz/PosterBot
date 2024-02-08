__all__ = [
    "ModerManyResponse",
    "ModerResponse",
    "ChatManyResponse",
    "ChatResponse",
    "PublicationManyResponse",
    "PublicationResponse",
    "TemplateManyResponse",
    "TemplateResponse",
]

from posterbot.services.db.response.chat import (
    ChatManyResponse,
    ChatResponse,
)
from posterbot.services.db.response.moder import (
    ModerManyResponse,
    ModerResponse,
)
from posterbot.services.db.response.publication import (
    PublicationManyResponse,
    PublicationResponse,
)
from posterbot.services.db.response.template import (
    TemplateManyResponse,
    TemplateResponse,
)