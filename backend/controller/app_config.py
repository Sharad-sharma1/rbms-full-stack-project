"""
Module containing all application configuration
functions that access environment variables.
"""
import os
from urllib.parse import quote
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_mysql_conn_string():
    """
    Function to build and return MySQL connection string.
    """
    username = os.getenv("MYSQL_USERNAME")
    password = os.getenv("MYSQL_PASSWORD")
    host = os.getenv("MYSQL_HOST")
    port = os.getenv("MYSQL_PORT", "3306")  # Default MySQL port
    database = os.getenv("MYSQL_DATABASE", "rbmd_db")

    encoded_password = quote(password) if password else ""
    return f"mysql+pymysql://{username}:{encoded_password}@{host}:{port}/{database}"

def get_act_secret_key():
    """
    Function to return Access token secret key stored in environment variable.
    """
    return os.getenv("JWT_SECRET_KEY", "default_secret_key")

def get_token_expiry():
    """
    Function to return JWT expiration time (in minutes) stored in environment variable.
    """
    return int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 1440))

class AppConfig(BaseSettings):
    """
    Define multiple config parameters whose values are taken from environment variables.
    """

    # CORS parameters.
    ALLOW_ORIGIN: list = ["*"]  # Allow any origin.

    # MySQL connection string
    MYSQL_CONNECTION_STRING: str = get_mysql_conn_string()
   
    # JWT constants.
    JWT_SECRET_KEY: str = get_act_secret_key()
    ACCESS_TOKEN_EXPIRE_MINUTES: int = get_token_expiry()

app_config = AppConfig()
