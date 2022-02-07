"""This is a main program."""
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import controller

app = FastAPI()

app.include_router(controller.router)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run("main:app", host="116.80.80.54", port=8000, reload=False)
