from fastapi import APIRouter, status, HTTPException, Request, Header
from fastapi.responses import JSONResponse
import httpx
from db.database import likes_collection
from auth.jwt_auth import auth
from core.config import settings

router = APIRouter(prefix="/interactions", tags=["interactions"])


