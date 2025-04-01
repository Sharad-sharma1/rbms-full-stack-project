from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..request_response_model.mortgage_models import *
from ..controller import mortgage_controller
from ..db_con import get_mysql_db_con
router = APIRouter()
import logging
logger = logging.getLogger(__name__)


@router.post("/insert-mortgage-record")
def insert_mortgage_record(
    request_body: MortgageCreateRequestModel,
    db: Session = Depends(get_mysql_db_con)
):
    """
    API to insert a record into the target table.
    """
    logger.info("Received request to insert mortgage record: %s", request_body)
    try:
        response = mortgage_controller.mortgage_insert_controller(request_body, db)
        logger.info("Successfully inserted mortgage record.")
        return response
    except Exception as e:
        logger.error("Error inserting mortgage record: %s", str(e))
        raise

@router.get("/get-mortgage-record")
def get_mortgage_record(
    request_body: MortgageGetRequestModel = Depends(),
    db: Session = Depends(get_mysql_db_con)
):
    """
    API to get a record into the target table.
    """
    logger.info("Received request to get mortgage record: %s", request_body)
    try:
        response = mortgage_controller.mortgage_get_controller(request_body, db)
        logger.info("Successfully geted mortgage record.")
        return response
    except Exception as e:
        logger.error("Error geting mortgage record: %s", str(e))
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
    logger.info("Received request to update mortgage record with ID %s: %s", mortgage_id, request_body)
    try:
        response = mortgage_controller.mortgage_update_controller(mortgage_id, request_body, db)
        logger.info("Successfully updated mortgage record with ID %s.", mortgage_id)
        return response
    except Exception as e:
        logger.error("Error updating mortgage record with ID %s: %s", mortgage_id, str(e))
        raise 

@router.delete("/delete-mortgage-record/{mortgage_id}")
def delete_mortgage_record(
    mortgage_id: int,
    db: Session = Depends(get_mysql_db_con)
):
    """
    API to delete a mortgage record by ID.
    """
    logger.info("Received request to delete mortgage record with ID %s", mortgage_id)
    try:
        response = mortgage_controller.mortgage_delete_controller(mortgage_id, db)
        logger.info("Successfully deleted mortgage record with ID %s.", mortgage_id)
        return response
    except Exception as e:
        logger.error("Error deleting mortgage record with ID %s: %s", mortgage_id, str(e))
        raise e
