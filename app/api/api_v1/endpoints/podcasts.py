from fastapi import APIRouter, status, HTTPException
from fastapi.responses import JSONResponse
import httpx
import json
from core.config import settings


router = APIRouter(prefix="/podcasts", tags=["podcasts"])


@router.get("/channels", status_code=status.HTTP_200_OK)
async def all_channels():
    rss_channels_url = f"{settings.RSS_APP_BASE_URL}/podcasts/channels/"
    async with httpx.AsyncClient() as client:
        response = await client.get(url=rss_channels_url)

    return JSONResponse(content=json.loads(response.text))

