from fastapi import APIRouter, status, HTTPException
from fastapi.responses import JSONResponse
import httpx
import json
from core.config import settings


router = APIRouter(prefix="/podcasts", tags=["podcasts"])
