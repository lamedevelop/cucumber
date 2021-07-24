from fastapi import APIRouter, Request
from starlette import status
from starlette.responses import JSONResponse

from app.db.services.product import ProductService


router = APIRouter()
service = ProductService()


@router.get(
    "/products",
    name='api-v1:get-products',
    status_code=status.HTTP_200_OK
)
async def get_products(request: Request):
    res = await service.get_products()
    return {"result": res}


@router.get(
    "/categories",
    name='api-v1:get-categories',
    status_code=status.HTTP_200_OK
)
async def get_categories(request: Request):
    res = await service.get_categories()
    return {"result": res}
