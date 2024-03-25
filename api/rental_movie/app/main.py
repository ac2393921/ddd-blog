from logging import getLogger

from fastapi import FastAPI

logger = getLogger("uvicorn.app")
app = FastAPI()


@app.post("/")
async def test():
    return {"message": "Hello World!"}