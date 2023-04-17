import os
from fastapi import FastAPI
from fastapi.middleware.cores import CORSMiddleware

app = FastAPI()

origins = [
    'http://localhost',
    'localhost'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_method=["*"],
    allow_headers=["*"]
)


@app.get("/")
async def root():
    return {"Msg": "Hello World!"}
