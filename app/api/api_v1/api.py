from fastapi import APIRouter
from .endpoints.podcasts import router as podcasts_router


router = APIRouter()
router.include_router(podcasts_router)
