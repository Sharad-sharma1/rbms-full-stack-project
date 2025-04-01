from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from backend.db_models.mortgage_model import Mortgage
from backend.request_response_model.mortgage_models import MortgageCreateRequestModel
import logging

logger = logging.getLogger(__name__)

def mortgage_detail_insert(request_body: MortgageCreateRequestModel, db_session: Session):
    try:
        # Convert Pydantic model to dictionary
        mortgage_data = request_body.model_dump()
        # Create an instance of the Mortgage model
        new_mortgage = Mortgage(**mortgage_data)
        # Add to the session
        db_session.add(new_mortgage)
        # Commit the transaction
        db_session.commit()
        # Refresh the instance to get updated values (like auto-generated IDs)
        db_session.refresh(new_mortgage)

        return {"message": "Mortgage record inserted successfully", "id": new_mortgage.id}
    except Exception as e:
        db_session.rollback()  # Rollback in case of error
        logger.error("An error occurred while inserting the mortgage: %s", str(e), exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error inserting mortgage")

def mortgage_detail_get(db_session: Session, id: int, page: int = 1, page_size: int = 100, for_update: bool = False):
    try:
        # Initialize the query
        query = db_session.query(Mortgage)
        # Apply filters based on provided parameters
        if id is not None:
            query = query.filter(Mortgage.id == id)
        query = query.filter(Mortgage.is_active == True)
        
        if for_update:
            data = query.first()
            if not data:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="No records found for the given filters."
                )
            return data
        
        # Calculate total count before pagination
        total_count = query.count()
        # Calculate total pages
        total_pages = (total_count + page_size - 1) // page_size if page_size else 1
        # Validate page number

        # Apply pagination
        offset_value = (page - 1) * page_size
        data = query.limit(page_size).offset(offset_value).all()

        if not data:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No records found for the given filters."
            )
        
        return {
            "message": "Mortgage records fetched successfully.",
            "total_count": total_count,
            "total_pages": total_pages,
            "data": data
        }

    except Exception as e:
        db_session.rollback()  # Rollback in case of error
        logger.error("An error occurred while fetching the mortgage data: %s", str(e), exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error fetching mortgage data")

def mortgage_detail_update(existing_mortgage: Mortgage, updated_data: dict, db_session: Session):
    try:
        # Update the attributes of the existing mortgage instance
        for key, value in updated_data.items():
            setattr(existing_mortgage, key, value)

        # Add the updated instance to the session and commit the changes
        db_session.add(existing_mortgage)
        db_session.commit()
        return {"id": existing_mortgage.id}
    
    except Exception as e:
        db_session.rollback()
        logger.error("An error occurred while updating the mortgage: %s", str(e), exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error updating mortgage")

def mortgage_detail_delete(get_single_mortgage: Mortgage, db_session: Session):
    try:
        # Soft delete the mortgage by marking it as inactive
        get_single_mortgage.is_active = False
        # Add the updated instance to the session and commit the changes
        db_session.add(get_single_mortgage)
        db_session.commit()
        return {"message": "Mortgage record deleted successfully", "id": get_single_mortgage.id}
    
    except Exception as e:
        db_session.rollback()
        logger.error("An error occurred while deleting the mortgage: %s", str(e), exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error deleting mortgage")
