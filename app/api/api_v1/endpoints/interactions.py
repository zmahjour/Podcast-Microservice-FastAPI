from fastapi import APIRouter, status, HTTPException
from fastapi.responses import JSONResponse
import httpx


router = APIRouter(prefix="/interactions", tags=["interactions"])


