from fastapi import FastAPI
from routers import compress
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://compress-frontend.eba-x3xxyuke.us-west-2.elasticbeanstalk.com"],  # Adjust according to your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def hello():
    return {"message": "Hello world"}

app.include_router(compress.router)
