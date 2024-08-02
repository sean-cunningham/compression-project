from fastapi import FastAPI, UploadFile, File
import time

app = FastAPI()


@app.get("/")
def hello_world():
    return {"message": "hello world!"}
