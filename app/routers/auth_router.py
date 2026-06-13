from fastapi import APIRouter, Depends, Form,HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import RedirectResponse
from datetime import timedelta

from app.services.auth_services import create_user_service, validate_credentials, verify_email_token_service
from app.schemas.auth_schema import User_In
from app.exceptions.auth_exceptions import *
from app.auths.auth_dependecies import create_token
from app.core.dotenv_config import TOKEN_EXPIRE_TIME

auth_router = APIRouter(tags=['auths'])
    
@auth_router.post("/auth/register")
async def register(user_in: User_In = Form(...)):
    if user_in.password != user_in.confirm_password:
        return {"message":"passwords didn't match"}
    try:
        token_infor = create_user_service(user_in.email, user_in.password)
        message = f"/auth/verify/email/{token_infor.get("credential_id")}/{token_infor.get("token")}"

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
    else:
        #send verification email
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
        return {
            "message": "Email verified successfully, proceed to login"
        }

 
@auth_router.post("/auth/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    try:
        user_claims = validate_credentials(form_data.username, form_data.password)
    except (EmailNotVerifiedError, AccessDeniedError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied, Email not verified or Access Revoked"
        )
    except (EmailNotFoundError, PasswordInvalidError):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Wrong email or password"
        )
    except(TokenExpiredError):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email not verified, token expired"
        )
    else:
        expire_delta = timedelta(minutes=TOKEN_EXPIRE_TIME)
        sub = user_claims.get("user_id")
        role = user_claims.get("role")
        payload = {
            "sub":sub,
            "role": role
        }
        access_token = create_token(payload, expire_delta)
        return {
            "access_token": access_token,
            "token_type": "Bearer",
        }
        


