# TODO: make ORM model

from pydantic import BaseModel, validator


class Product(BaseModel):
    product_id: int
    name: str
    price: float
    category: int
    availability: bool = True

    @validator('product_id')
    def id_validation(cls, v: int):
        if not (v >= 0 and isinstance(v, int)):
            raise ValueError('Id must be positive integer')
        return v

    @validator('price')
    def price_validation(cls, v: float):
        if v < 0:
            raise ValueError('Price must be positive float')
        return v


class Category(BaseModel):
    category_id: int
    name: str

    @validator('category_id')
    def id_validation(cls, v: int):
        if not (v >= 0 and isinstance(v, int)):
            raise ValueError('Id must be positive integer')
        return v
