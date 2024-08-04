from fastapi import FastAPI
from routers import compress

app = FastAPI()

@app.get("/")
async def hello():
    return {"message": "Hello world"}

app.include_router(compress.router)
