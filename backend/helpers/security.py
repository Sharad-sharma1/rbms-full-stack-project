"""
Module containing abstraction layer for security libraries.
"""
from datetime import datetime, timedelta
from passlib.context import CryptContext
from jose import jwt, JWTError
from backend.controller.app_config import app_config
from . import constant as sc

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password):
    """
    Function to hash plain-text password using bcrypt algorithm.
    """
    # Hash the password with a random salt.
    return bcrypt_context.hash(password)


def compare_passwords(text_pwd, hash_pwd) -> bool:
    """
    Function to compare plain-text password and hashed password.
    """
    return bcrypt_context.verify(text_pwd, hash_pwd)


def create_access_token(unq_id: int, data: dict = None):
    """
    Function to create and return JWT access token encapsulating input data.
    """
    now = datetime.utcnow()

    # Initialize JWT payload.
    payload = {
        "sub": str(unq_id),  # Add unique subject id.
        "exp": now + timedelta(minutes=app_config.ACCESS_TOKEN_EXPIRE_MINUTES),  # Add expiration time.
        "iat": now,  # Add JWT issued time.
    }

    # Add data to JWT payload.
    if data:
        payload.update(data)

    # Encode payload and return JWT.
    return jwt.encode(payload, app_config.JWT_SECRET_KEY, algorithm=sc.ACT_ALG)


def verify_access_token(token: str):
    """
    Function to verify JWT access token.
    """
    try:
        # Validate JWT header.
        hdr = jwt.get_unverified_header(token)

        if hdr["alg"] != sc.ACT_ALG:
            raise JWTError(f'Invalid algorithm-string - {hdr["alg"]} - in header.')

        if hdr["typ"] != sc.ACT_TYPE:
            raise JWTError(f'Invalid access token type - {hdr["typ"]} - in header.')

        # TODO: Validate `jwt.get_unverified_claims(token)`.

        return jwt.decode(token, app_config.JWT_SECRET_KEY, algorithms=[sc.ACT_ALG])

    except JWTError as err:
        print("JWT ERROR:", err)
        raise err
