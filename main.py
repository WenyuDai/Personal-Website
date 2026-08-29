from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from experiences import Experience, experiences
from portfolio import Portfolio, portfolio
from researches import Research, researches

app = FastAPI()

origins = [
    "http://localhost:5173",
    "https://wenyudai.github.io"
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

@app.get("/researches", response_model=list[Research])
def getResearches():
    return researches

# check loading status
@app.get("/health")
def health():
    return {"status": "ok"}