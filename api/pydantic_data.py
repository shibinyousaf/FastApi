from pydantic import BaseModel


class Users(BaseModel):
    user_id : int
    first_name:str
    last_name:str| None
    password:str

class AccountCreate(BaseModel):
    account_id :int
    account_name:str
    

