import jwt
from jwt.error import InvalidTokenError
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends
from datetime import datetime, timezone, timedelta

from app.core.token_config import SECRET_KEY, ALGORITHM

oauth2_scheme = OAuthPasswordBearer(tokenUrl="auth/login")

async def get_current_id(token: Annotated[str, Depends(oauth2_scheme)]):
    CredentialError = HTTPException(
        status_code=401,
        detail="Could not verify credentials",
        header={"Authenticate":"Bearer"}
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("sub")
        if not user_id:
            raise CredentialError
        #Ill also check when user exists in the database
    
    except InvalidTokenError:
        raise CredentialError
    else: 
        return user_id

async def create_token(claim: dict, expiry_delta:timedelta| None = None):
    to_encode = claim.copy()
    if expiry_delta:
        exp = datetime.now(timezone.utc) + timedelta(minutes=expiry_delta)
    else:
        exp = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp":exp})
    encoded = jwt.encode(to_encode, SECRET_KEY, ALGORITHM)

async def get_current_admin(user_id: Annotated[str, Depends(get_current_id)]):
    # this will get the admin
    pass

async def get_current_user(user_id: Annotated[str, Depends(get_current_id)]):
    #Will get the admin
    pass