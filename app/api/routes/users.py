from fastapi import APIRouter, Response
from fastapi_cache.decorator import cache
from tenji import MfcClient
from tenji.request.user.collection import CollectionStatus
from tenji.exceptions import ParserException

from app.api.models.response import ResponseModel

router = APIRouter(
    prefix="/v1",
    tags=["users"],
    responses={
        404: {"description": "Not found"},
        500: {"description": "Internal Server Error"},
    },
)

client = MfcClient()


@router.get("/profile/{username}")
@cache(expire=60)
async def get_profile(username: str):
    try:
        profile = await client.get_profile(username)
        return ResponseModel(data=profile)
    except ParserException:
        return ResponseModel(message="Error parsing profile", status_code=500)
    return ResponseModel(message="User not found", status_code=404)


@router.get("/collection/{username}")
@cache(expire=60)
async def get_collection(
    username: str, status: CollectionStatus = CollectionStatus.Owned, page: int = 1
):
    collection = await client.get_collection(username, status, page)
    return ResponseModel(data=collection)


@router.get("/user_listings/{id}")
@cache(expire=60)
async def get_buys(id: int, jan: int):
    buys = await client.get_user_listings(id, jan)
    return ResponseModel(data=buys)
