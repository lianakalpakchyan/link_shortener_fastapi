"""
URL Model Module

This module defines the SQLAlchemy model for URLs.

Classes:
    - URL: SQLAlchemy model for storing URL entries.
"""

from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from . import Base


class URL(Base):
    """
    SQLAlchemy model for storing URL entries.

    Attributes:
        - full_url (Mapped[str]): Full URL to be shortened (non-nullable, unique, indexed).
        - short_url (Mapped[str]): Shortened URL (non-nullable, indexed).
        - date_created (Mapped[datetime]): Date and time when the URL entry was created (default: current UTC time).

    Methods:
        - __repr__: String representation of the URL instance.
    """

    full_url: Mapped[str] = mapped_column(nullable=False, unique=True, index=True)
    short_url: Mapped[str] = mapped_column(nullable=False, index=True)
    date_created: Mapped[datetime] = mapped_column(default=datetime.utcnow)

    def __repr__(self) -> str:
        """
        String representation of the URL instance.

        Returns:
            str: A string representation of the URL instance.
        """
        return f"<URL: {self.short_url}>"
