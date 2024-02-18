from random import random

from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/")
async def root():
    if random() < 0.1:
        raise HTTPException(status_code=418, detail="I'm a teapot")

    return {"message": "Hello World"}
