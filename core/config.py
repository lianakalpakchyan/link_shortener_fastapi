"""
Configuration Module

This module defines a Pydantic BaseSettings class for application configuration.

Classes:
    - Setting: Configuration class derived from BaseSettings.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Configuration class derived from BaseSettings.

    Attributes:
        - model_config (SettingsConfigDict): Configuration for loading settings from environment variables and an
            optional .env file.
        - db_echo (bool): Flag to enable or disable echoing SQL statements.
        - api_v1_prefix (str): Prefix for API version 1.
        - short_url_domain (str): Domain for short URLs.
        - POSTGRES_DB (str): PostgreSQL database name.
        - POSTGRES_USER (str): PostgreSQL database user.
        - POSTGRES_PASSWORD (str): PostgreSQL database password.
        - POSTGRES_HOST (str): PostgreSQL database host.
        - POSTGRES_PORT (str): PostgreSQL database port.

    Properties:
        - db_url (str): Computed property for generating the PostgreSQL database URL.

    Methods:
        - None
    """

    model_config = SettingsConfigDict(env_file=".env")
    db_echo: bool = False
    api_v1_prefix: str = "/api/v1"
    short_url_domain: str

    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: str

    @property
    def db_url(self) -> str:
        """
        Computed property for generating the PostgreSQL database URL.

        Returns:
            str: PostgreSQL database URL.
        """
        return (
            f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@"
            f"{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )


settings = Settings()
