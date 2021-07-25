# TODO: make ORM model
from typing import Optional
from pydantic import BaseModel, validator


class ClientInRequest(BaseModel):
    name: str
    surname: Optional[str] = ''
    phone: str
    email: Optional[str] = ''

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


class Client(ClientInRequest):
    client_id: int

    @validator('client_id')
    def id_validation(cls, v: int):
        if not (v >= 0 and isinstance(v, int)):
            raise ValueError('Id must be positive integer')
        return v


class ClientValidation(BaseModel):
    client_id: int
    pin: int
    method: int
    date: int

    @validator('client_id')
    def id_validation(cls, v: int):
        if not (v >= 0 and isinstance(v, int)):
            raise ValueError('Id must be positive integer')
        return v


class ClientValidationFull(ClientValidation):
    validation_id: int

    @validator('validation_id')
    def id_validation(cls, v: int):
        if not (v >= 0 and isinstance(v, int)):
            raise ValueError('Id must be positive integer')
        return v
