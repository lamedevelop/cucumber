# TODO: make ORM model

from pydantic import BaseModel, validator


class Client(BaseModel):
    client_id: int
    name: str
    surname: str
    phone: str
    email: str

    @validator('client_id')
    def id_validation(cls, v: int):
        if not (v >= 0 and isinstance(v, int)):
            raise ValueError('Id must be positive integer')
        return v

    @validator('phone')
    def phone_validation(cls, v: str):
        # todo: fix phone validation in CU-28
        if len(v) < 1:
            raise ValueError('Wrong phone format')
        return v

    @validator('email')
    def email_validation(cls, v: str):
        # todo: fix email validation in CU-28
        if '@' not in v:
            raise ValueError('Wrong email format')
        return v
