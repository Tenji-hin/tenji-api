from fastapi import APIRouter
from fastapi_cache.decorator import cache
from tenji import MfcClient
from tenji.request.user.collection import CollectionStatus

router = APIRouter(
    prefix="/v1",
    tags=["mfc"],
    responses={404: {"description": "Not found"}},
)


class DataResponse:
    def __init__(self, data):
        self.data = data


client = MfcClient()


@router.get("/profile/{username}")
@cache(expire=60)
async def get_profile(username: str):
    profile = await client.get_profile(username)
    return DataResponse(profile)


@router.get("/collection/{username}")
@cache(expire=60)
async def get_collection(
    username: str, status: CollectionStatus = CollectionStatus.Owned, page: int = 1
):
    collection = await client.get_collection(username, status, page)
    return DataResponse(collection)


@router.get("/list/{id}")
@cache(expire=60)
async def get_list(id: int, page: int = 1):
    l = await client.get_list(id, page)
    return DataResponse(l)


@router.get("/lists/{username}")
@cache(expire=60)
async def get_lists(username: str):
    lists = await client.get_lists(username)
    return DataResponse(lists)


@router.get("/item/{id}")
@cache(expire=60)
async def get_item(id: int):
    item = await client.get_item(id)
    return DataResponse(item)


@router.get("/shop/{id}")
@cache(expire=60)
async def get_shop(id: int):
    shop = await client.get_shop(id)
    return DataResponse(shop)


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
    return DataResponse(shops)


@router.get("/partner_listings/{item_id}")
@cache(expire=60)
async def get_buys(item_id: int):
    buys = await client.get_partner_listings(item_id)
    return DataResponse(buys)


@router.get("/user_listings/{id}")
@cache(expire=60)
async def get_buys(id: int, jan: int):
    buys = await client.get_user_listings(id, jan)
    return DataResponse(buys)
