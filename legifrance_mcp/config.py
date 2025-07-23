"""Configuration de l'application."""

from __future__ import annotations

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Paramètres principaux."""

    client_id: str
    client_secret: str
    port: int = 7777
    log_level: str = "info"

    class Config:
        env_prefix = ""
        env_file = ".env"


def get_settings() -> Settings:
    """Retourne une instance de :class:`Settings`."""
    return Settings()  # type: ignore[call-arg]
