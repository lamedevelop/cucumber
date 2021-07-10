from fastapi import APIRouter, Request
from starlette import status
from starlette.responses import JSONResponse
from starlette.templating import Jinja2Templates


router = APIRouter()
templates = Jinja2Templates(directory="static")


@router.get(
    "/",
    name='static:main-page',
    status_code=status.HTTP_200_OK
)
async def get_main(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


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
