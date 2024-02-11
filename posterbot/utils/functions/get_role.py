from dataclasses import dataclass

from posterbot.services.db.request import ModerRequestBuilder
from posterbot.services import ServiceApiSession
from posterbot.configs import BotConfig


@dataclass
class UserRole:
    is_moder: bool
    is_owner: bool
    other: bool

    def set_moder(self) -> None:
        self.is_moder = True
        self.other = False
    
    def set_owner(self) -> None:
        self.is_owner = True
        self.other = False

    @property
    def owner_or_moder(self) -> bool:
        return self.is_owner or self.is_moder


async def get_role(
    user_id: int,
    api: ServiceApiSession,
    config: BotConfig = BotConfig()
) -> UserRole:
    role = UserRole(False, False, True)

    if user_id in config.OWNERS:
        role.set_owner()
    
    response_data = await api.send(
        ModerRequestBuilder().get_moder(user_id)
    )

    if response_data.status == 200:
        role.set_moder()

    return role
