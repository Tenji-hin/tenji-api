from distutils.util import strtobool
import logging
import os
from fastapi import FastAPI
import aioredis
from dotenv import load_dotenv
from fastapi_cache import FastAPICache
from fastapi.middleware.cors import CORSMiddleware
from fastapi_cache.backends.redis import RedisBackend
from app.api.routes import items, lists, shops, users
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

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(items.router)
app.include_router(lists.router)
app.include_router(shops.router)
app.include_router(users.router)


@app.on_event("startup")
async def startup():
    redis = aioredis.from_url("redis://localhost")
    FastAPICache.init(RedisBackend(redis), prefix="tenji-cache")
