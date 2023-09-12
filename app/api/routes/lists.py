from fastapi import APIRouter
from fastapi_cache.decorator import cache
from tenji import MfcClient

from app.api.models.response import ResponseModel

router = APIRouter(
    prefix="/v1",
    tags=["lists"],
    responses={
        404: {"description": "Not found"},
        500: {"description": "Internal Server Error"},
    },
)

client = MfcClient()


@router.get("/list/{id}")
@cache(expire=60)
async def get_list(id: int, page: int = 1):
    l = await client.get_list(id, page)
    return ResponseModel(data=sl)


@router.get("/lists/{username}")
@cache(expire=60)
async def get_lists(username: str):
    lists = await client.get_lists(username)
    return ResponseModel(data=slists)
