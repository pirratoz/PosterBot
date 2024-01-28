from pydantic_settings import SettingsConfigDict

from source.configs.base_config import BaseConfig


class BotConfig(BaseConfig):
    model_config = SettingsConfigDict(
        env_prefix="TG_"
    )

    TOKEN: str
    OWNER_IDS: list[int]
