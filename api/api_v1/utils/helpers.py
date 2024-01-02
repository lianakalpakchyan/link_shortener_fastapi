"""
URL Utilities Module

This module provides utility functions for handling URLs.

Functions:
    - generate_short_url: Generates a short URL based on the SHA-256 hash of the original URL.
"""

import base64
import hashlib

from core import settings


def generate_short_url(original_url: str) -> str:
    """
    Generate a short URL based on the SHA-256 hash of the original URL.

    Args:
        original_url (str): The original URL for which a short URL is generated.

    Returns:
        str: The generated short URL.
    """
    hash_object = hashlib.sha256(original_url.encode())
    hash_bytes = hash_object.digest()
    base64_encoded = base64.b64encode(hash_bytes)
    short_url = base64_encoded.decode("utf-8").rstrip("=")[:8]
    return f"{settings.short_url_domain}{short_url}"
