from fastapi import APIRouter
from .endpoints.podcasts import router as podcasts_router


router = APIRouter()
