#User can add subscription, edit a subscription, delete a subscription(s), get subscriptions 
# API for subscriptions
from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional
from datetime import date
from data import subscriptions_cache

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

subscription_router = APIRouter()

@subscription_router.get('/subscription/{userId}')
def get_subsciptions(userId: int):
    return subscriptions_cache[userId] # <-- list of all subscriptions for user

@subscription_router.post('/subscription/{userId}')
def add_subscription(userId: int, subscription: Subscription):
    # check to make sure key is not already in cache
    if userId not in subscriptions_cache:
        subscriptions_cache[userId] = []

    # add subscription to cache for user
    subscriptions_cache[userId].append(subscription)
    return subscription

@subscription_router.put('/subscription/{userId}')
def update_subscription(userId: int, subscription: Subscription):
    # TODO: check to make sure userId exists in cache

    index_of_subscription = -1
    for i, cached_subscription in enumerate(subscriptions_cache[userId]):
        if cached_subscription.id == subscription.id:
            index_of_subscription = i
            break

    if index_of_subscription == -1:
        return None
    
    subscriptions_cache[userId].pop(index_of_subscription)
    subscriptions_cache[userId].append(subscription)

    return subscription

@subscription_router.delete('/subscription/{subscriptionId}/{userId}')
def delete_subscription(userId: int, subscriptionId: int):
    # TODO: check to make sure userId exists in cache
    
    index_of_subscription = -1
    for i, cached_subscription in enumerate(subscriptions_cache[userId]):
        if cached_subscription.id == subscriptionId:
            index_of_subscription = i
            break

    if index_of_subscription == -1:
        return None

    removed_subscription = subscriptions_cache[userId].pop(index_of_subscription)
    return removed_subscription
