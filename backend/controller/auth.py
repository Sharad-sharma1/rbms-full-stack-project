# """
# Module to authenticate user using JWT token and
# return context after successful authentication.

# This module contains components that play the role
# of Authorization server as per OAuth 2.0 scheme.
# """
# from fastapi import Depends, HTTPException, status
# from fastapi.security import OAuth2PasswordBearer
# from sqlalchemy.orm import Session
# from src.db_sf import get_sf_db_con
# from context import Context
# from helpers.app_exceptions_validations import ValidationError
# from src.libs import security
# from helpers import utils
# import helpers.constant as sc


# oauth2_bearer = OAuth2PasswordBearer(tokenUrl="api/auth/login")
# async def get_context(token: str = Depends(oauth2_bearer), db: Session = Depends(get_sf_db_con)):
#     """
#     Function to verify JWT token and extract data from payload.
#     """
#     try:
#         """
#         STEP 1: Extract payload from JWT token after validating:
#                 1. Token expiry.
#                 2. Tampering.
#         """
#         payload = security.verify_access_token(token)

#         sub = payload.get("sub")  # JWT Subject or User id.
#         eid = payload.get("eid")  # Email id.
#         enm = payload.get("enm")  # Application id.

#         """
#         STEP 2: Additionally validate if all necessary fields are present.
#         """
#         if utils.is_empty(sub) or utils.is_empty(eid) or utils.is_empty(enm):
#             raise ValidationError(message="Invalid payload.")

#         """
#         STEP 4: Build and return Context object.
#         """
#         return Context(sub, eid, aid, enm)

#     except Exception as err:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=sc.TOKEN_VALIDATION_FAILED) from err
