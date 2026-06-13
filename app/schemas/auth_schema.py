from pydantic import BaseModel,EmailStr

class User_In(BaseModel):
    email: EmailStr 
    password:str
    confirm_password:str