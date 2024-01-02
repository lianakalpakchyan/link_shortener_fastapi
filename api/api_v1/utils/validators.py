"""
URL Validation Utilities Module

This module provides utility functions for validating URLs.

Functions:
    - is_valid_url: Checks if the given URL is valid by sending a HEAD request.
"""

import requests


def is_valid_url(url: str) -> bool:
    """
    Check if the given URL is valid by sending a HEAD request and
    checking if the response status code falls within the 2xx range.

    Parameters:
        - url (str): The URL to be checked.

    Returns:
        - bool: True if the URL is valid and returns a successful response (2xx),
          False otherwise or if an exception occurs during the request.
    """
    try:
        response = requests.head(url)
        return response.status_code // 100 == 2
    except requests.RequestException:
        return False
