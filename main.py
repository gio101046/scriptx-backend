from fastapi import FastAPI
from api import user_router
from api import subscription_router

app = FastAPI()
app.include_router(user_router)
app.include_router(subscription_router)


