from pydantic import BaseModel


class ExtraBase(BaseModel):
    name: str
    price: float


class ExtraCreate(ExtraBase):
    pass


class Extra(ExtraBase):
    id: int

    class Config:
        orm_mode = True
