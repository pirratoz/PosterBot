from pydantic_settings import SettingsConfigDict

from posterbot.configs.base_config import BaseConfig


class BotConfig(BaseConfig):
    model_config = SettingsConfigDict(
        env_prefix="TG_"
    )

    TOKEN: str
    OWNERS: list[int]
