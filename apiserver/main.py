import datetime

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    ts = datetime.datetime.now().timestamp()

    return {
        "message": "Hello, welcome to TechWideHub!",
        "timestamp": ts,
    }
