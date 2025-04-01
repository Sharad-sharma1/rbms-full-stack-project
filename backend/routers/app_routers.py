import logging
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.request_response_model.mortgage_models import *
from backend.controller import mortgage_controller
from fastapi.security import OAuth2PasswordRequestForm
from backend.request_response_model.auth_model import *
from backend.controller import auth_controller
from backend.db_con import get_mysql_db_con

router = APIRouter()
logger = logging.getLogger(__name__)

@router.post("/login", response_model=LoginResponse)
async def login(user_cred: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_mysql_db_con)):
    """
    API to login with registered Email-id and password.
    """
    logger.debug("Login attempt for user: %s", user_cred.username)  # DEBUG level for login attempts
    return auth_controller.authenticate_user(db, user_cred)


@router.post("/insert-mortgage-record")
def insert_mortgage_record(
    request_body: MortgageCreateRequestModel,
    db: Session = Depends(get_mysql_db_con)
):
    """
    API to insert a record into the target table.
    """
    logger.info("Received request to insert mortgage record: %s", request_body)  # INFO for received requests
    try:
        response = mortgage_controller.mortgage_insert_controller(request_body, db)
        logger.info("Successfully inserted mortgage record.")  # INFO for successful insertions
        return response
    except Exception as e:
        logger.error("Error inserting mortgage record: %s", str(e))  # ERROR for errors
        raise

@router.get("/get-mortgage-record")
def get_mortgage_record(
    request_body: MortgageGetRequestModel = Depends(),
    db: Session = Depends(get_mysql_db_con)
):
    """
    API to get a record into the target table.
    """
    logger.info("Received request to get mortgage record: %s", request_body)  # INFO for received requests
    try:
        response = mortgage_controller.mortgage_get_controller(request_body, db)
        logger.info("Successfully fetched mortgage record.")  # INFO for successful fetch
        return response
    except Exception as e:
        logger.error("Error getting mortgage record: %s", str(e))  # ERROR for errors
        raise

@router.put("/update-mortgage-record/{mortgage_id}")
def update_mortgage_record(
    mortgage_id: int,
    request_body: MortgageCreateRequestModel,
    db: Session = Depends(get_mysql_db_con)
):
    """
    API to update a mortgage record by ID.
    """
    logger.info("Received request to update mortgage record with ID %s: %s", mortgage_id, request_body)  # INFO for received requests
    try:
        response = mortgage_controller.mortgage_update_controller(mortgage_id, request_body, db)
        logger.info("Successfully updated mortgage record with ID %s.", mortgage_id)  # INFO for successful updates
        return response
    except Exception as e:
        logger.error("Error updating mortgage record with ID %s: %s", mortgage_id, str(e))  # ERROR for errors
        raise

@router.delete("/delete-mortgage-record/{mortgage_id}")
def delete_mortgage_record(
    mortgage_id: int,
    db: Session = Depends(get_mysql_db_con)
):
    """
    API to delete a mortgage record by ID.
    """
    logger.info("Received request to delete mortgage record with ID %s", mortgage_id)  # INFO for received requests
    try:
        response = mortgage_controller.mortgage_delete_controller(mortgage_id, db)
        logger.info("Successfully deleted mortgage record with ID %s.", mortgage_id)  # INFO for successful deletion
        return response
    except Exception as e:
        logger.error("Error deleting mortgage record with ID %s: %s", mortgage_id, str(e))  # ERROR for errors
        raise e
