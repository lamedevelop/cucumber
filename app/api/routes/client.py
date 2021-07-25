from starlette import status
from starlette.responses import JSONResponse
from fastapi import APIRouter, Request
from fastapi.responses import FileResponse

from app.db.services.client import ClientService
from app.db.services.validation import ValidationService

router = APIRouter()
service = ClientService()


@router.post(
    "/client",
    name='api-v1:post-client',
    status_code=status.HTTP_201_CREATED
)
async def set_client(request: Request):
    client = await request.json()
    client = client['data']

    client_id = await service.register_client(client)

    return {'client_id': client_id} if client_id \
        else JSONResponse(
            {'error': 'Client was not created'},
            status_code=status.HTTP_400_BAD_REQUEST,
        )


@router.post(
    "/client/{client_id}/validation",
    name='api-v1:validate-client',
    status_code=status.HTTP_200_OK
)
async def validate_client(client_id: int, request: Request):
    validation = await request.json()
    pin = validation['data']['pin']
    client = await service.get_client(client_id)

    validation_res = await ValidationService().check_validation(client, pin)

    return {'result': "Validation success"} if validation_res \
        else JSONResponse(
            {'error': 'Wrong validation pin'},
            status_code=status.HTTP_400_BAD_REQUEST,
        )


@router.patch(
    "/client/{client_id}",
    name='api-v1:patch-client',
    status_code=status.HTTP_200_OK
)
async def update_client(client_id: int, request: Request):
    update_fields = await request.json()
    update_fields = update_fields['data']

    client = await service.update_client(client_id, update_fields)

    return {'result': 'Client was updated'} if client \
        else JSONResponse(
            {'error': 'Client was not updated'},
            status_code=status.HTTP_400_BAD_REQUEST,
        )


@router.get(
    "/client/{client_id}",
    name='api-v1:get-client',
    status_code=status.HTTP_200_OK
)
async def get_client(client_id: int, request: Request):
    client = await service.get_client(client_id)
    return {"data": client}


@router.get(
    "/client/{client_id}/image",
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
