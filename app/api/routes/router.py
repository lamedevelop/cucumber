import sys

from fastapi import APIRouter, Request
from starlette import status
from starlette.responses import JSONResponse
from starlette.templating import Jinja2Templates

from app.api.routes import product, client


import base64
from PIL import Image
from io import BytesIO

router = APIRouter()
templates = Jinja2Templates(directory="static")


router.include_router(product.router, tags=["api"], prefix="/api/v1")
router.include_router(client.router, tags=["api"], prefix="/api/v1")


@router.get(
    "/",
    name='static:main-page',
    status_code=status.HTTP_200_OK
)
async def get_main(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@router.post(
    "/phone",
    name='test:post-phone',
    status_code=status.HTTP_200_OK
)
async def post_phone(request: Request):
    request = await request.json()
    print(request)
    return request


@router.post(
    "/image/post",
    name='test:post-image',
    status_code=status.HTTP_201_CREATED
)
async def post_image(request: Request):
    print("POST image method")
    body = await request.json()
    im = Image.open(BytesIO(base64.b64decode(body['key'])))
    im.save('media/image1.png', 'PNG')


@router.get(
    "/image/get",
    name='test:get-image',
    status_code=status.HTTP_200_OK
)
async def get_image(request: Request):
    filename = 'media/image1.png'
    with open(filename, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
        encoded_string = encoded_string.decode('utf-8')
        return {'key': encoded_string}


@router.get(
    "/test",
    name='test:get-json',
    status_code=status.HTTP_200_OK
)
async def get_test_json(request: Request):
    return JSONResponse(
        {
            'products': [
                {
                  'p_id': 1,
                  'p_name': 'Колбаса',
                  'p_price': 100
                },
                {
                    'p_id': 2,
                    'p_name': 'Молоко',
                    'p_price': 515
                },
            ]
        },
        status_code=status.HTTP_200_OK,
    )
