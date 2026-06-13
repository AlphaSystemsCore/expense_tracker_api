from fastapi import APIRouter,Depends
from typing import Annotated

from app.auths.auth_dependecies import get_current_user

expense_router = APIRouter(prefix="/expenses", tags=['expense'])

@expense_router.post("/")
async def create_expense(user_id:Annotated[str, Depends(get_current_user)]):
    return {"user_id":user_id}
