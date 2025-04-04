"""
Module containing all reusable logics as utility functions.
"""

from . import constant as sc

def success_response(message: str = sc.SUCCESS_MESSAGE, data: dict = None):
    """
    Returns a standardized success response.
    """
    return {"status": True, "message": message, "data": data or {}}

def failure_response(message: str = sc.INTERNAL_SERVER_ERROR, errors: list = None):
    """
    Returns a standardized failure response.
    """
    return {"status": False, "message": message, "errors": errors or []}
