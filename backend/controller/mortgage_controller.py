from sqlalchemy.orm import Session
from backend.helpers.mortgage_credit_calculator import CreditRatingCalculator  # Import your class
from backend.request_response_model.mortgage_models import MortgageCreateRequestModel
from backend.manager import mortgage_manager
import logging

# Set up the logger for this module
logger = logging.getLogger(__name__)

def mortgage_insert_controller(request_body: MortgageCreateRequestModel, db_session: Session):
    try:
        logger.info("Received request to insert mortgage: %s", request_body)
        
        # Convert Pydantic model to a dictionary before unpacking
        calculator = CreditRatingCalculator(**request_body.model_dump())
        
        # Calculate the credit rating
        credit_rating = calculator.calculate_credit_rating()
        logger.debug("Calculated credit rating: %s", credit_rating)

        # Insert mortgage details into the database
        insert_response = mortgage_manager.mortgage_detail_insert(request_body, db_session)
        logger.info("Mortgage record inserted successfully. Mortgage ID: %s", insert_response.get("id"))
        
        # Return structured JSON response
        return {
            "status": "success",
            "message": "Mortgage Inserted successfully",
            "data": {
                "mortgage_id": insert_response.get("id"),
                "credit_rating": credit_rating,
            },
        }
    except Exception as e:
        # Rollback transaction in case of an error
        db_session.rollback()
        logger.error("An error occurred while inserting the mortgage record: %s", str(e), exc_info=True)
        raise e

def mortgage_get_controller(request_body: dict, db_session: Session):
    try:
        logger.info("Received request to get mortgage records with params: %s", request_body)

        id = request_body.id
        page = request_body.page
        page_size = request_body.page_size

        # Get mortgage details from the database
        get_response = mortgage_manager.mortgage_detail_get(db_session, id, page, page_size)
        data = get_response.get('data', [])
        total_count = get_response.get('total_count')
        total_pages = get_response.get('total_pages')

        # Process each mortgage record to calculate and add credit_rating
        for mortgage in data:
            calculator = CreditRatingCalculator(
                mortgage.credit_score,
                mortgage.loan_amount,
                mortgage.property_value,
                mortgage.annual_income,
                mortgage.debt_amount,
                mortgage.loan_type,
                mortgage.property_type
            )
            credit_rating = calculator.calculate_credit_rating()
            mortgage.credit_rating = credit_rating 
            logger.debug("Calculated credit rating for mortgage ID %s: %s", mortgage.id, credit_rating)

        # Structure the JSON response
        response = {
            "status": "success",
            "message": "Mortgage details retrieved successfully",
            "total_count": total_count,
            "total_pages": total_pages,
            "data": data
        }

        return response
    except Exception as e:
        # Rollback transaction in case of an error
        db_session.rollback()
        logger.error("An error occurred while processing the mortgage records: %s", str(e), exc_info=True)
        raise e

def mortgage_update_controller(id: int, request_body: MortgageCreateRequestModel, db_session: Session):
    try:
        logger.info("Received request to update mortgage record with ID: %s", id)

        # Convert Pydantic model to a dictionary before unpacking
        request_body_dict = request_body.model_dump()
        
        get_single_mortgage = mortgage_manager.mortgage_detail_get(db_session, id, for_update=True)
        
        # Update mortgage record
        insert_response = mortgage_manager.mortgage_detail_update(get_single_mortgage, request_body_dict, db_session)
        logger.info("Mortgage record updated successfully with ID: %s", id)

        # Return structured JSON response
        return {
            "status": "success",
            "message": "Mortgage record updated successfully",
            "data": insert_response
        }
    
    except Exception as e:
        # Rollback transaction in case of an error
        db_session.rollback()
        logger.error("An error occurred while updating the mortgage record with ID %s: %s", id, str(e), exc_info=True)
        raise e

def mortgage_delete_controller(id: int, db_session: Session):
    try:
        logger.info("Received request to delete mortgage record with ID: %s", id)

        get_single_mortgage = mortgage_manager.mortgage_detail_get(db_session, id, for_update=True)

        # Delete mortgage record
        insert_response = mortgage_manager.mortgage_detail_delete(get_single_mortgage, db_session)
        logger.info("Mortgage record deleted successfully with ID: %s", id)

        # Return structured JSON response
        return {
            "status": "success",
            "data": insert_response
        }
    
    except Exception as e:
        # Rollback transaction in case of an error
        db_session.rollback()
        logger.error("An error occurred while deleting the mortgage record with ID %s: %s", id, str(e), exc_info=True)
        raise e
