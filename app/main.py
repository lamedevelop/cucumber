from app.api.routes.router import router
from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI


def get_application() -> FastAPI:
    application = FastAPI()
    application.include_router(router)

    origins = [
        "*",
    ]

    application.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return application


app = get_application()



# @app.on_event("startup")
# async def startup():
#     app.state.pool = await aiopg.create_pool(DbSettings.dsn())
#
#
# @app.on_event("shutdown")
# async def shutdown():
#     await app.state.pool.close()
