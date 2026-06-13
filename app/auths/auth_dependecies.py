import jwt
from jwt.exceptions import InvalidTokenError
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from datetime import datetime, timezone, timedelta
from typing import Annotated

from app.core.dotenv_config import SECRET_KEY, ALG

ALGORITHM = ALG
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

async def create_token(claim: dict, expiry_delta:timedelta| None = None):
    to_encode = claim.copy()
    if expiry_delta:
        exp = datetime.now(timezone.utc) + expiry_delta
    else:
        exp = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp":exp})
    encoded = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded

async def get_current_user_id_role(token: Annotated[str, Depends(oauth2_scheme)]):
    CredentialError = HTTPException(
        status_code=401,
        detail="Could not verify credentials",
        header={"Authenticate":"Bearer"}
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("sub")
        role = payload.get("role")
        print(role)
        print(user_id)
        if not user_id:
            raise CredentialError
        #Ill also check when user exists in the database
    
    except InvalidTokenError:
        raise CredentialError
    else: 
        return {
            "user_id": user_id,
            "role": role
        }



async def get_current_admin(user: Annotated[dict, Depends(get_current_user_id_role)]):
    if user.get("role") == "admin":
        return user.get("user_id")
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Not Admin"
    )
        
    pass

async def get_current_user(user: Annotated[dict, Depends(get_current_user_id_role)]):
    if user.get("role") == "user" or  user.get("role") == "admin":
        return user.get("user_id")
    
    
