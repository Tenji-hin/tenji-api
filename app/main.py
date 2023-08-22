from fastapi import FastAPI
import aioredis


from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from app.api.routes import mfc

app = FastAPI(
    title="MyFigureCollection API",
    description="An unofficial API for MyFigureCollection.net",
    version="0.1.0",
)

app.include_router(mfc.router)


@app.on_event("startup")
async def startup():
    redis = aioredis.from_url("redis://localhost")
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")