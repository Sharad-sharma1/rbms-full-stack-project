"""
Module containing code for user Authentication.
"""
from fastapi import HTTPException, status
from backend.manager import user_manger
from backend.helpers import utils, security, constant as sc


def authenticate_user(db, user_cred):
    """
    API to authenticate user using user's user-id and password.
    After a successfully authentication, API returns JWT as access token.
    """

    """
    STEP 1: Get user details from database using user-id.
    """
    user = user_manger.get_user_by_email(db, user_cred.username)

    """
    STEP 2: Validate user credentials.
    """
    if utils.is_empty(user):
        # Raise unauthorized request error if the user is not registered in the database.
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail=sc.INVALID_CREDENTIALS
        )

    # Compare between plain-text-password (entered by user) and hashed-password (from database).
    is_matching = security.compare_passwords(
        text_pwd=user_cred.password, hash_pwd=user.password
    )

    if not is_matching:
        # Raise unauthorized request error if the passwords are not matching.
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail=sc.INVALID_CREDENTIALS
        )

    """
    STEP 3: Generate and send new JWT token as API response
            after all the user credentials are authenticated.
    """
    access_token = security.create_access_token(
        uniq_id=user.email_id,
    )
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "role": user.role,
    }
