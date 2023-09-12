from fastapi import APIRouter, Response
from fastapi_cache.decorator import cache
from tenji import MfcClient

from app.api.models.response import ResponseModel

router = APIRouter(
    prefix="/v1",
    tags=["shops"],
    responses={
        404: {"description": "Not found"},
        500: {"description": "Internal Server Error"},
    },
)

client = MfcClient()


@router.get("/shops/{id}")
@cache(expire=60)
async def get_shop(id: int):
    shop = await client.get_shop(id)
    return ResponseModel(data=sshop)


@router.get("/shops")
@cache(expire=60)
async def get_shops(
    keywords: str = None,
    location: str = None,
    average_score: int = None,
    category: int = None,
    page: int = 1,
):
    shops = await client.get_shops(keywords, location, average_score, category, page)
    return ResponseModel(data=shops)


@router.get("/partner_listings/{item_id}")
@cache(expire=60)
async def get_buys(item_id: int):
    buys = await client.get_partner_listings(item_id)
    return ResponseModel(data=sbuys)
