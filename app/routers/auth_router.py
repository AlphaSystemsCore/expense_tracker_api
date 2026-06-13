from fastapi import APIRouter, Depends, Form,HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import RedirectResponse

from app.services.auth_services import create_user_service, verify_email_token_service
from app.schemas.auth_schema import User_In

auth_router = APIRouter()
    
@auth_router.post("/auth/register")
async def register(user_in: User_In = Form(...)):
    if user_in.password != user_in.confirm_password:
        return {"message":"passwords didn't match"}
    try:
        token_infor = create_user_service(user_in.email, user_in.password)
        message = f"http://127.0.0.1:8000/auth/verify/email/{token_infor.get("credential_id")}/{token_infor.get("token")}"

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
    else:
        return RedirectResponse(url=message)
        
    
@auth_router.post("/auth/verify/email/{credential_id}/{token}")
async def verify_email(credential_id, token):
    try:
        verify_email_token_service(credential_id, token)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
    else:
        return RedirectResponse(url="http://127.0.0.1:8000/auth/login")

 
@auth_router.post("/auth/login")
async def login():
    return {
        "message": "logged in successful"
    }

# @auth_router.get("/auth/logout/{user_id}")
# async def logout(user_id):
#     pass



# @auth_router.get("/auth/reset_password/{token}")
# async def reset_password():
#     pass

# @auth_router.post("/auth/reset_password/")
# async def set_new_password(new_password:str = Form(), confirm_password:str = Form()):
#     pass