# API for registering new user
from fastapi import FastAPI
from pydantic import BaseModel

# Schema
class User(BaseModel):
        id : int 
        first_name : str
        last_name : str
        age : int 
        email : str 
        password_hash : str
        password_salt : str
        profile_url : str # Bonus, as noted in the documents

app = FastAPI()

@app.post('/register')
def register_user(user: User):
    # this should post a new
    # user to the database
    return {}
