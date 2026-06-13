from fastapi import FastAPI

from app.routers.auth_router import auth_router
from app.routers.expense_router import expense_router


app = FastAPI()
app.include_router(auth_router)
app.include_router(expense_router)