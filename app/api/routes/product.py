from fastapi import APIRouter, Request
from starlette import status

from app.db.services.product import ProductService


router = APIRouter()
service = ProductService()


@router.get(
    "/categories",
    name='api-v1:get-categories',
    status_code=status.HTTP_200_OK
)
async def get_categories(request: Request):
    categories = await service.get_categories()
    return {"data": categories}


@router.get(
    "/products",
    name='api-v1:get-products',
    status_code=status.HTTP_200_OK
)
async def get_products(request: Request):
    products = await service.get_products()
    return {"data": products}


@router.get(
    "/products/{product_id}",
    name='api-v1:get-product',
    status_code=status.HTTP_200_OK
)
async def get_products(product_id: int, request: Request):
    product = await service.get_product(product_id)
    return {"data": product}
