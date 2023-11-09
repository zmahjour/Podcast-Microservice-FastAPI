from fastapi import FastAPI
from contextlib import asynccontextmanager
import uvicorn
import aioredis
from api.api_v1.api import router as podcast_router
from core.config import settings



app = FastAPI()
app.include_router(podcast_router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8003, reload=True)
