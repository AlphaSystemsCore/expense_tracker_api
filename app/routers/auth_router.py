from fastapi import APIRouter, Depends
from fastapi.security import OAuthPasswordRequestForm

auth_router = APIRouter()

auth_router.post("/auth/register")
async def register(email: str = Form(), password:str = Form(), confirm: str = Form()):
    if password != confirm:
        return {"message":"passwords didn't match"}
    pass

async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    pass

auth_router.get("/auth/logout/{user_id}")
async def logout(user_id):
    pass

auth_router.get("/auth/verify/email/{token}")
async def verify_email(token):
    pass

auth_router.get("/auth/reset_password/{token}")
async def reset_password():
    pass

auth_router.post("/auth/reset_password/")
async def set_new_password(new_password:str = Form(), confirm_password:str = Form()):
    if 