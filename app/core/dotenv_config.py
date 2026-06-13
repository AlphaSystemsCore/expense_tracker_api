from dotenv import load_dotenv
import os 

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')
TOKEN_EXPIRE_TIME = int(os.getenv('TOKEN_EXPIRE_TIME'))
EMAIL_VERIFICATION_TOKEN_EXPIRY = int(os.getenv('EMAIL_VERIFICATION_TOKEN_EXPIRY'))

# FOR DEBUGGING
if __name__ == "__main__":
    print(EMAIL_VERIFICATION_TOKEN_EXPIRY,SECRET_KEY, ALGORITHM, TOKEN_EXPIRE_TIME, 
    )