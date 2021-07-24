from starlette import status
from starlette.responses import JSONResponse
from fastapi import APIRouter, Request
from fastapi.responses import FileResponse

from app.db.services.client import ClientService


router = APIRouter()
service = ClientService()


@router.get(
    "/clients/{client_id}",
    name='api-v1:get-client',
    status_code=status.HTTP_200_OK
)
async def get_client(client_id: int, request: Request):
    client = await service.get_client(client_id)
    return {"data": client}


@router.get(
    "/clients/{client_id}/image",
    name='api-v1:get-client',
    status_code=status.HTTP_200_OK
)
async def get_client_image(client_id: int, request: Request):
    filename = await service.get_client_image_filename(client_id)
    return FileResponse(filename) if filename \
        else JSONResponse(
            {'error': 'File not exist'},
            status_code=status.HTTP_404_NOT_FOUND,
        )
