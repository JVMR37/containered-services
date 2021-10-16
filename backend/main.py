from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.entities.database.config import engine, Base
from backend.routers import router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
