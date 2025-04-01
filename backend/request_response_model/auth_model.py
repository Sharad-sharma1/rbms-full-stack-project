"""
Module to define login response model.
"""
from pydantic import BaseModel
from ..helpers import constant as sc


class UserCreateRequestBody(BaseModel):
    """
    User Created request body schema
    """

    username: str
    password: str
    email: str
    role: str


class LoginResponse(BaseModel):
    """
    Login response schema
    """

    status: bool = True
    message: str = sc.LOGIN_SUCCESSFUL
    access_token: str
    token_type: str
    role: str

class UserCreatedResponse(BaseModel):
    """
    User Created response schema
    """

    status: bool = True
    message: str = sc.USER_CREATED_SUCCESSFULLY
    username: str