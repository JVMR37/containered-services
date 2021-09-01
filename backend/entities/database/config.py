import os

from sqlalchemy import create_engine, event
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv


# noinspection PyUnusedLocal
def _fk_pragma_on_connect(dbapi_con, con_record):
    dbapi_con.execute('pragma foreign_keys=ON')


def get_configured_engine(database_url):
    if SQLALCHEMY_DATABASE_URL.startswith('sqlite'):
        engine_ = create_engine(database_url, connect_args={
                                "check_same_thread": False})
        event.listen(engine_, 'connect', _fk_pragma_on_connect)
        return engine_

    return create_engine(SQLALCHEMY_DATABASE_URL)


load_dotenv()

SQLALCHEMY_DATABASE_URL = os.environ.get("DATABASE_URL")
engine = get_configured_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
