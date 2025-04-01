from pydantic import BaseModel, Field, condecimal, conint
from enum import Enum
from typing import Optional
# Enum for Loan Type
class LoanTypeEnum(str, Enum):
    fixed = "fixed"
    adjustable = "adjustable"

# Enum for Property Type
class PropertyTypeEnum(str, Enum):
    single_family = "single_family"
    condo = "condo"

# Pydantic Model for Mortgage Request
class MortgageCreateRequestModel(BaseModel):
    credit_score: conint(ge=300, le=850) 
    loan_amount: condecimal(gt=0, decimal_places=2) 
    property_value: condecimal(gt=0, decimal_places=2) 
    annual_income: condecimal(gt=0, decimal_places=2) 
    debt_amount: condecimal(ge=0, decimal_places=2) 
    loan_type: LoanTypeEnum 
    property_type: PropertyTypeEnum 

class MortgageGetRequestModel(BaseModel):
    id: Optional[conint(ge=1)] = None
    page: Optional[conint(ge=1)] = 1
    page_size: Optional[conint(ge=50, le=500)] = 50


