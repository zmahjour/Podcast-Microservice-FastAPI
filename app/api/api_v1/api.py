from fastapi import APIRouter
from .endpoints.podcasts import router as podcasts_router
from .endpoints.interactions import router as interactions_router


router = APIRouter()
router.include_router(podcasts_router)
router.include_router(interactions_router)
