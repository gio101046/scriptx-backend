#User can add subscription, edit a subscription, delete a subscription(s), get subscriptions 
# API for subscriptions
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from datetime import date

# Schema
class Subscription(BaseModel):
    id : int # This is the ID of the specific subscription itself
    user_id : int # This denotes to which user the subscription belongs
    service_id : int # This denotes to which service the subscription is paying to
    amount : float # how much is charged each cycle
    subscription_date : Optional[date] # Date the subscription was first started
    cycle : int # The cycle of the subscription, measured in days
    notes : str # Any additional notes
    # Bonus: Category

app = FastAPI()

@app.get('/subscriptions')
def get_subs(sub : Subscription):
    # this one may be a bit trickier
    # as it should retrieve all
    # subscriptions bearing a specific user id
    # and not necessarily based on the subscrpition id
    return {}

@app.post('/add_subscription')
def add_sub(sub : Subscription):
    # this should add
    # a new subscription to the database
    return {}

@app.put('/edit_subscription/{sub.id}')
def update_sub(sub: Subscription):
    # this should retrieve the data
    # from the referenced subscription
    # in the list and display
    # it in editable fields for editing
    return {}

@app.delete('/delete_subscription/{sub.id}')
def delete_sub(sub : Subscription):
    # this should delete the
    # specific subscription
    # from the database
    return {}
