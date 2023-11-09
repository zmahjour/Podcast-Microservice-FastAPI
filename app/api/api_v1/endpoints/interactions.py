from fastapi import APIRouter, status, HTTPException, Request, Header
from fastapi.responses import JSONResponse
import httpx
from db.database import likes_collection
from auth.jwt_auth import auth
from core.config import settings

router = APIRouter(prefix="/interactions", tags=["interactions"])


@router.post("/like/episode/{episode_id}", status_code=status.HTTP_201_CREATED)
async def like_episode(
    request: Request, episode_id: int, authorization: str = Header()
):
    payload = await auth.authenticate(request=request, auth_header=authorization)
    rss_check_episode_url = (
        f"{settings.RSS_APP_BASE_URL}/podcasts/check/episode/{episode_id}/"
    )

    if payload:
        async with httpx.AsyncClient() as client:
            response = await client.get(url=rss_check_episode_url)

        if response.status_code == status.HTTP_404_NOT_FOUND:
            raise HTTPException(
                status_code=response.status_code,
                detail=f"Episode with id {episode_id} does not exist.",
            )

        like_data = {"username": payload["username"], "episode_id": episode_id}
        if await likes_collection.find_one(like_data):
            return JSONResponse(
                content={"detail": "You have liked this episode before."},
                status_code=status.HTTP_201_CREATED,
            )

        await likes_collection.insert_one(like_data)

        return JSONResponse(
            content={"detail": "You have liked this episode."},
            status_code=status.HTTP_201_CREATED,
        )
