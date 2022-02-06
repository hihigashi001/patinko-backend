"""This is a main program."""
import uvicorn
from fastapi import FastAPI
import controller

app = FastAPI()

app.include_router(controller.router)

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
