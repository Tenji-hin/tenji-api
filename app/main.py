from distutils.util import strtobool
import logging
import os
from fastapi import FastAPI
import aioredis
from dotenv import load_dotenv
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from app.api.routes import mfc
from logtail import LogtailHandler

load_dotenv(".env")
DEBUG = bool(strtobool(os.getenv("DEBUG", "True")))

logger = logging.getLogger("TenjiLogger")
logging.root.setLevel(logging.INFO if not DEBUG else logging.DEBUG)

if os.getenv("LOGTAIL_TOKEN"):
    logger.addHandler(LogtailHandler(os.getenv("LOGTAIL_TOKEN")))

logger.info("Starting up...")

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