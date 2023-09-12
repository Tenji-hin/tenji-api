from fastapi import APIRouter
from fastapi_cache.decorator import cache
from tenji import MfcClient

from app.api.models.response import ResponseModel

router = APIRouter(
    prefix="/v1",
    tags=["items"],
    responses={
        404: {"description": "Not found"},
        500: {"description": "Internal Server Error"},
    },
)

client = MfcClient()


@router.get("/item/{id}")
@cache(expire=60)
async def get_item(id: int):
    item = await client.get_item(id)
    return ResponseModel(data=item)
