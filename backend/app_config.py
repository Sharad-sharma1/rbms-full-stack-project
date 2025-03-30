"""
Module containing all application configuration
functions that has accesses to environment variables.
"""
import os
from pydantic_settings import BaseSettings
from urllib.parse import quote

def get_postgres_conn_string():
    """
    Function to build and return Snowflake connection string.
    """
    username = "pharmmdm_dna"
    password = "D&^F&g$#65&gD@7D)h"
    port = 5432
    database = "pharmmdm"
    host = 'dna-dev-mdm-postgresql-rds.cbvtgpvvbmxq.ap-south-1.rds.amazonaws.com'
 

    encoded_password = quote(password)  # URL-encode the password
    return f"postgresql://{username}:{encoded_password}@{host}:{port}/{database}"


def get_act_secret_key():
    """
    Function to return Access token secret key stored in environment variable.
    """
    return "3bb638d962ca0a398d9aa1d6c348fda7e249edb22468d2a2d8db671bf1efefc4"


def get_token_expiry():
    """
    Function to return JWT expiration time (in hours) stored in environment variable.
    """
    return "1440"


class AppConfig(BaseSettings):
    """
    Define multiple config parameters whose values are taken from environment variables.
    """

    # CORS parameters.
    ALLOW_ORIGIN: list = ["*"]  # Allow any origin.

    #P postgres connection string
    POSTGRES_CONNECTION_STRING:str = get_postgres_conn_string()
   
    # JWT constants.
    JWT_SECRET_KEY: str = get_act_secret_key()
    ACCESS_TOKEN_EXPIRE_MINUTES: int = get_token_expiry()


app_config = AppConfig()
