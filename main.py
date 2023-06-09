from fastapi import FastAPI
from routes import post_router

app = FastAPI()

app.include_router(post_router.router)
