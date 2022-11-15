from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from routers import pokemons_api, trainers_api
import uvicorn


app = FastAPI()
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# app.include_router(pokemons_api.router)
# app.include_router(trainers_api.router)

@app.get("/")
def root():
    return "server is running"


if __name__ == "__main__":
    uvicorn.run("server:app", host="localhost", port=8000, reload=True)







# rest of the routes