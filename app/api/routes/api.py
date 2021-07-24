from fastapi import APIRouter, Request
from starlette import status
from starlette.responses import JSONResponse

from app.db.services.product import ProductService


router = APIRouter()


@router.get(
    "/products",
    name='api-v1:get-products',
    status_code=status.HTTP_200_OK
)
async def get_products(request: Request):
    # request = await request.json()

    service = ProductService()
    res = await service.get_products()

    return {"result": res}


@router.get(
    "/product/{product_id}",
    name='api-v1:get-product',
    status_code=status.HTTP_200_OK
)
async def get_products(product_id: int, request: Request):
    service = ProductService()
    res = await service.get_product(product_id)

    return {"result": res}
