"""
Module to place all string constants used in the application.
"""

# General messages
SUCCESS_MESSAGE = "Success!"  # Used in health check
INTERNAL_SERVER_ERROR = "Internal server error."
INVALID_REQUEST = "Invalid request."
UNAUTHORIZED_REQUEST = "Unauthorized request."  # HTTP status 401
FORBIDDEN_REQUEST = "Forbidden request."  # HTTP status 403
RESOURCE_NOT_FOUND = "Resource not found."  # HTTP status 404
SERVICE_UNAVAILABLE = "Service is unavailable."
APPLICATION_NAME = "RBMS APIs Collection"
TOKEN_VALIDATION_FAILED = "Failed to authorize user."
LOGIN_SUCCESSFUL = "User login successful."
USER_CREATED_SUCCESSFULLY = "User created successfully."

# JWT constants.
ACT_TYPE = "JWT"  # Access Token Type.
ACT_ALG = "HS256"  # Access Token Algorithm.
