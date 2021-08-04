#User can: Edit profile, Delete profile and Login profile

from fastapi import FastAPI
from pydantic import BaseModel


class User(BaseModel):
    def __init__(self):
        self.id : int = None
        self.first_name : str = None
        self.last_name : str = None
        self.age : int = None
        self.email : str = None
        self.password_hash : str = None
        self.password_salt : str = None
        self.profile_url : str = None # Bonus, as noted in the documents

app = FastAPI()

db = []

@app.get('/')
def index():
    return {'key' : 'value'}

@app.post('/user/{user.id}')
def update_profile(user : User):
    db[user.id] = user.dict()
    return db[user.id]


