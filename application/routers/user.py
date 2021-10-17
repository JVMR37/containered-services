from __future__ import annotations

import os
from datetime import datetime, timedelta
from typing import Optional

import sqlalchemy.exc
from fastapi import Depends, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from application.entities.database.models import User as dbUser
from application.entities.serializers import UserCreate, User
from application.entities.serializers.token import Token, TokenData
from application.routers.dependencies import get_db

SECRET_KEY = os.environ.get('SECRET_KEY', 'unsafe-secret-key')
ALGORITHM = os.environ.get('ALGORITHM', 'HS256')
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.environ.get('ACCESS_TOKEN_EXPIRE_MINUTES', 30))

security = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/token")

router = APIRouter(
    prefix='/users',
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


def get_user(username: str, db: Session) -> User | None:
    """Queries for a user in the database using it's username.

    :param db: a database session.
    :param username: the username to be queried.
    :return: the user with that username, if it exists, None otherwise.
    """

    user: dbUser = db.query(dbUser).filter_by(username=username).first()

    if not user:
        return None

    return User(
        id=user.id,
        username=user.username,
        password=user.password,
        role=user.role
    )


def authenticate_user(db: Session, username: str, password: str) -> User | None:
    """Queries for a user in the database with the given information

    :param db: a database session.
    :param username: the username to be queried.
    :param password: the password provided by the user.
    :return: the user, if it exists and the passwords match, None otherwise.
    """

    user: dbUser = db.query(dbUser).filter_by(username=username).first()
    if not user or not security.verify(password, user.password):
        return None

    return User(
        id=user.id,
        username=user.username,
        password=user.password,
        role=user.role
    )


def create_access_token(data: dict, expires_delta: timedelta) -> str:
    """Creates a encoded JWTs token with the given data.

    :param data: the data to be encoded.
    :param expires_delta: time to expire the token.
    :return: a string with the encoded information.
    """

    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, key=SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# user Depends(get_current_user) to access the current user in the function
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    """Returns the current user based on the token received. Raises HTTP 401 if credentials couldn't be validated.

    :param token: the token of the user.
    :param db: a database session.
    :return: the corresponding user.
    """

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")

        if username is None:
            raise credentials_exception

        token_data = TokenData(username=username)

    except JWTError:
        raise credentials_exception

    user = get_user(username=token_data.username, db=db)
    if user is None:
        raise credentials_exception

    return user


class RoleChecker:
    def __init__(self, accessible_by_roles: Optional[list[str]] = None):
        self.accessible_by_roles = accessible_by_roles

    def __call__(self, current_user=Depends(get_current_user)):
        current_user: User
        if self.accessible_by_roles and current_user.role not in self.accessible_by_roles:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=f"Only {self.accessible_by_roles} can do this action."
            )

        return current_user


@router.post("/register", response_model=User, dependencies=[Depends(RoleChecker(['admin', 'caixa']))])
def register(user: UserCreate, db: Session = Depends(get_db)):
    instance = dbUser(
        username=user.username,
        password=security.hash(user.password),
        role=user.role
    )

    db.add(instance)
    try:
        db.commit()

    except sqlalchemy.exc.IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="This username is already taken, use another one."
        )

    db.refresh(instance)

    return instance


@router.post("/token", response_model=Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={
                "WWW-Authenticate": "Bearer"
            },
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={
            "sub": user.username
        },
        expires_delta=access_token_expires
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


@router.get("/me", response_model=User)
def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user
