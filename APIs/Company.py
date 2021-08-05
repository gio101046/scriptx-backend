#Get companie(s)

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# schema
class Company():
    service_id : int # This denotes to which user the subscription belongs
    name : str 
    logo_url : str
    ticker : str
    price : float

@app.get('/companies')
def get_companies():
    # this should return the
    # internal list of companies
    # available
    return {}