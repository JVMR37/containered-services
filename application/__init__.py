from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from application.entities.database.config import engine, Base, SessionLocal
from application.entities.database.models import User
from application.routers import router
from application.routers.user import security

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.on_event('startup')
async def app_startup():
    session = SessionLocal()
    exists = session.query(User).filter_by(username='admin').first()
    if not exists:
        user = User(username='admin', password=security.hash('admin'), role='admin')
        session.add(user)
        session.commit()

    print('The super user has the following credentials:\nusername: admin\npassword: admin')


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
