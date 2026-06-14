from fastapi import APIRouter,Depends
from typing import Annotated

from app.auths.auth_dependecies import get_current_user
from app.services.expense_service import create_expense_service
from app.schemas.expense_schema import Expense_In
from app.exceptions.expense_exceptions import DateTimeExtractionError

expense_router = APIRouter(tags=['expense'])

@expense_router.post("/expenses")
async def create_expense(user_id:Annotated[str, Depends(get_current_user)], expense_in:Expense_In):
    try:
        create_expense_service(user_id, expense_in.amount,expense_in.categories, expense_in.Date, expense_in.Time)
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail = str(e)
        )
    except DateTimeExtractionError:
        raise HTTPException(
            status_code = 500,
            detail = "Date extraction Failed"
        )
    except Exception as e:
        raise HTPPException(
            status_code = 500,
            detail = "Failed to create expense"
        )
    return {
        "message":"Created successfull"
    }

@expense_router.patch("/expenses/{expense_id}")
async def update_expense():
    pass