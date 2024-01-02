"""
Base Model Module

This module defines a base SQLAlchemy DeclarativeBase class for models.

Classes:
    - Base: Abstract base class for SQLAlchemy models.
"""

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr


class Base(DeclarativeBase):
    """
    Abstract base class for SQLAlchemy models.

    Attributes:
        - __abstract__ (bool): Indicates that this is an abstract base class.
        - __tablename__ (str): Computed attribute for generating the table name.
        - id (Mapped[int]): Mapped column for the primary key.

    Methods:
        - None
    """

    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        """
        Computed attribute for generating the table name.

        Returns:
            str: Table name based on the lowercase name of the model class.
        """
        return f"{cls.__name__.lower()}s"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
