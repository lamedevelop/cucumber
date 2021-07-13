from fastapi import APIRouter, Request
from starlette import status
from starlette.responses import JSONResponse


router = APIRouter()


@router.get(
    "/products",
    name='api-v1:get-products',
    status_code=status.HTTP_200_OK
)
async def get_products(request: Request):
    request = await request.json()
