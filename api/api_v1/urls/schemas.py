"""
URL Schemas Module

This module defines Pydantic models for handling URLs.

Classes:
    - URLModel: Base Pydantic model for URLs.
    - URLCreateModel: Pydantic model for creating a new URL entry.
"""

from pydantic import BaseModel, ConfigDict


class URLModel(BaseModel):
    pass


class URLCreateModel(URLModel):
    """
    Model for creating a new URL.

    Attributes:
        full_url (str): The full URL to be stored.

    Configurations:
        model_config (ConfigDict): Additional configuration for the model.
            - from_attributes: Set to True for automatic conversion from class attributes.
            - json_schema_extra: Additional JSON schema information, including an example.
    """

    full_url: str

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {"full_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"}
        },
    )
