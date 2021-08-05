from fastapi import FastAPI
from api import user_router
from api import subscription_router

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Hello World"}

app.include_router(user_router)
app.include_router(subscription_router)


