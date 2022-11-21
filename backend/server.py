from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import transactions_api
import uvicorn


app = FastAPI()
origins = [ #how can get to the serevr
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(transactions_api.router)


@app.get("/")
def root():
    return "server is running"


if __name__ == "__main__":
    uvicorn.run("server:app", host="localhost", port=8000, reload=True)
