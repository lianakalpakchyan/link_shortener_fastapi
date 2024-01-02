"""
URL Router Module

This module defines FastAPI router for handling URL-related operations.
"""

from http import HTTPStatus
from typing import Dict

from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Path, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.exc import IntegrityError, NoResultFound

from . import crud
from db import db_helper
from core import URL
from . import URLCreateModel
from ..utils import generate_short_url
from ..utils import is_valid_url

router = APIRouter(tags=["URLs"])


@router.get("/{short_url:path}/", status_code=HTTPStatus.TEMPORARY_REDIRECT)
async def get_full_url_and_redirect(
    short_url: str = Path(...),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> RedirectResponse:
    """
    Redirect to the full URL corresponding to the given short URL.

    Parameters:
        - short_url (str): The short URL to redirect to.
        - session (AsyncSession): The database session.

    Returns:
        - RedirectResponse: Redirects to the full URL.

    Raises:
        - HTTPException: If the short URL doesn't exist (HTTP 404 Not Found).
    """
    url = await crud.get_full_url(session=session, short_url=short_url)
    if url:
        return RedirectResponse(url.full_url)
    else:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail="Short URL not found.",
        )


@router.post("/shorten/", status_code=HTTPStatus.CREATED)
async def create_short_url(
    url_data: URLCreateModel,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Dict[str, str]:
    """
    Create a short URL for the given full URL.

    Parameters:
        - url_data (URLCreateModel): The data to create a new URL.
        - session (AsyncSession): The database session.

    Returns:
        - dict: A dictionary containing the created short URL.

    Raises:
        - HTTPException: If the URL is invalid, unreachable, or short URL already exists.
    """
    if not is_valid_url(url_data.full_url):
        raise HTTPException(
            status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
            detail="Invalid or unreachable URL.",
        )

    new_url = URL(
        short_url=generate_short_url(url_data.full_url), full_url=url_data.full_url
    )

    try:
        url = await crud.add_url(session=session, new_url=new_url)
        return {"short_url": url.short_url}
    except IntegrityError:
        raise HTTPException(
            status_code=HTTPStatus.CONFLICT,
            detail="Short URL already exists.",
        )


@router.delete("/{short_url:path}/", status_code=HTTPStatus.NO_CONTENT)
async def delete_url(
    short_url: str = Path(...),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    """
    Delete the URL entry corresponding to the given short URL.

    Parameters:
        - short_url (str): The short URL to delete.
        - session (AsyncSession): The database session.

    Raises:
        - HTTPException: If the short URL doesn't exist (HTTP 404 Not Found).
    """
    try:
        await crud.delete_url(session=session, short_url=short_url)
    except NoResultFound:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail="Short URL not found.",
        )
