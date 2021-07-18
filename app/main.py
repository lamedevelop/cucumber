import aiopg

from app.api.routes.router import router

from fastapi import FastAPI

from app.db.settings import DbSettings


def get_application() -> FastAPI:
    application = FastAPI()
    application.include_router(router)

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
