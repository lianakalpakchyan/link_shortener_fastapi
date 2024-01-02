"""
CRUD Operations Module

This module provides CRUD operations for the URL model.

Classes:
    - CRUD: Class containing methods for CRUD operations on the URL model.
"""

from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete

from core import URL


class CRUD:
    """
    Class containing methods for CRUD operations on the URL model.

    Methods:
        - get_full_url: Retrieve the full URL by short URL.
        - add_url: Add a new URL entry to the database.
        - delete_url: Delete a URL entry from the database.
    """

    @staticmethod
    async def get_full_url(session: AsyncSession, short_url: str) -> URL | None:
        """
        Retrieve the full URL by short URL.

        Parameters:
            - session (AsyncSession): The database session.
            - short_url (str): The short URL to retrieve the full URL for.

        Returns:
            - URL | None: The URL entry if found, None otherwise.
        """
        statement = select(URL).filter(URL.short_url == short_url)
        result = await session.execute(statement)
        return result.scalars().one_or_none()

    @staticmethod
    async def add_url(session: AsyncSession, new_url: URL) -> URL:
        """
        Add a new URL entry to the database.

        Parameters:
            - session (AsyncSession): The database session.
            - new_url (URL): The URL entry to be added.

        Returns:
            - URL: The added URL entry.
        """
        session.add(new_url)
        await session.commit()
        return new_url

    @staticmethod
    async def delete_url(session: AsyncSession, short_url: str):
        """
        Delete a URL entry from the database.

        Parameters:
            - session (AsyncSession): The database session.
            - short_url (str): The short URL of the entry to be deleted.

        Raises:
            - NoResultFound: If the entry with the specified short URL is not found.
        """
        delete_statement = delete(URL).where(URL.short_url == short_url)
        result = await session.execute(delete_statement)
        await session.commit()

        if result.rowcount == 0:
            raise NoResultFound()

        return {}


crud = CRUD()
