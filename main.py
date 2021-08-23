from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import backend.main as backend
import frontend.main as frontend

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(backend.router)
app.mount('/', frontend.router)
