"""
Database Helper Module

This module provides a DatabaseHelper class for handling asynchronous database operations using SQLAlchemy.

Classes:
    - DatabaseHelper: Helper class for managing the database connection and sessions.
"""

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession,
    async_scoped_session,
    async_sessionmaker,
)
from asyncio import current_task

from core import settings


class DatabaseHelper:
    """
    Helper class for managing the database connection and sessions.

    Attributes:
        - engine: SQLAlchemy asynchronous database engine.
        - session_factory: Factory for creating asynchronous database sessions.

    Methods:
        - __init__: Initializes the DatabaseHelper instance.
        - get_scoped_session: Returns a scoped asynchronous database session.
        - scoped_session_dependency: Asynchronous context manager for obtaining a scoped database session.
    """

    def __init__(self, url: str, echo: bool = False):
        """
        Initializes the DatabaseHelper instance.

        Parameters:
            - url (str): The database URL.
            - echo (bool): If True, the engine will log all SQL statements.

        Returns:
            None
        """
        self.engine = create_async_engine(
            url=url,
            echo=echo,
        )
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )

    def get_scoped_session(self):
        """
        Returns a scoped asynchronous database session.

        Returns:
            Session: Scoped asynchronous database session.
        """
        session = async_scoped_session(
            session_factory=self.session_factory,
            scopefunc=current_task,
        )
        return session

    async def scoped_session_dependency(self) -> AsyncSession:
        """
        Asynchronous context manager for obtaining a scoped database session.

        Yields:
            AsyncSession: Scoped asynchronous database session.
        """
        async with self.session_factory() as session:
            yield session


# Database Helper instance for global use
db_helper = DatabaseHelper(
    url=settings.db_url,
    echo=settings.db_echo,
)
