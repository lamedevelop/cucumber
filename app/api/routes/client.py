from fastapi import APIRouter, Request
from starlette import status

from app.db.services.client import ClientService

router = APIRouter()
service = ClientService()


@router.get(
    "/clients/{client_id}",
    name='api-v1:get-client',
    status_code=status.HTTP_200_OK
)
async def get_products(client_id: int, request: Request):
    client = await service.get_client(client_id)
    return {"data": client}
