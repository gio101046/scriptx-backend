#User can: Edit profile, Delete profile and Login profile

from fastapi import FastAPI
from pydantic import BaseModel

db = []

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

@app.get('/user/{user.id}')
def get_user(id : int):
    return db[id - 1]

@app.post('/user') # this is a test point, comment it out
def add_user(user: User):
    db.append(user.dict())
    return db[-1]


@app.put('/user/{user.id}')
def update_profile(user : User):
    db[user.id - 1] = user.dict()
    return db[user.id - 1]

@app.delete('/user/{user.id}')
def delete_profile(user: User):
    db.pop(user.id - 1)
    return {}


