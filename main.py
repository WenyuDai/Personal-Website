from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from experiences import Experience, experiences
from portfolio import Portfolio, portfolio

app = FastAPI()

origins = [
    "http://localhost:5173",
    "https://WenyuDai.github.io"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get("/", response_model=Portfolio)
def root():
    return portfolio

@app.get("/experiences", response_model=list[Experience])
def getExperiences():
    return experiences

