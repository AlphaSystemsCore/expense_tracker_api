from datetime import datetime, timezone, timedelta
import secrets


from ..auths.password_handler import (hash_password, verify_password, DUMMY_HASH)
from app.auths.token_handler import hash_token, verify_token
from app.core.dotenv_config import EMAIL_VERIFICATION_TOKEN_EXPIRY
from app.repositories.auth_repo import create_credential_user_token_repo,get_verify_email_token_repo, update_verify_email_token_repo



def create_email_verification_token_service():
    #creates the token using secrete lib
    token = secrets.token_urlsafe(32)
    token_expiry = datetime.now(timezone.utc) + timedelta(minutes=EMAIL_VERIFICATION_TOKEN_EXPIRY)
    return token, token_expiry


def create_user_service(email, password):
    # create credentials, returns token and credential_id
    hashed_password = hash_password(password)
    token_data = create_email_verification_token_service()
    try:
    
        credential_id = create_credential_user_token_repo(email, hashed_password, hash_token(token_data[0]), token_data[1])[0]
    except Exception as e:
        #log
        raise
    else:
        return token_data[0], credential_id


def verify_email_token_service(credential_id: str, token: str):
    try:
        row = get_verify_email_token_repo(credential_id)
        token_data = {
            "is_verified":row[0],
            "hashed_token":row[1],
            "expire_at":row[2],
            "is_used":row[3],
        }
        print(token_data)
        if verify_token(token, token_data.get("hashed_token")):
            raise ValueError("Could Not Validate token")
        if token_data.get("is_verified") == False and token_data.get("expire_at") < datetime.utcnow()  and token_data.get("is_used") == False:
            is_used = True
            is_verified = True
            update_verify_email_token_repo(credential_id, is_verified, is_used)
    except Exception:
        raise
    





#for testing
if __name__ == "__main__":
    print(create_email_verification_token())
