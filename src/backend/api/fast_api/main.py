from fastapi import FastAPI

from src.api.fast_api.routes.address import address_create
from src.api.fast_api.routes.user import user_create, user_get_by_id

app = FastAPI()

app.include_router(user_create.router)
app.include_router(address_create.router)
app.include_router(user_get_by_id.router)
