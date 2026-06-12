from dotenv import load_env
import os 

load_env()

SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')
TOKEN_EXPIRE_TIME = os.getenv('TOKEN_EXPIRE_TIME')

if __name__ == "__main__":
    print(SECRET_KEY)