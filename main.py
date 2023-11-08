from fastapi import FastAPI
import uvicorn
from api.api_v1.api import router as podcast_router


app = FastAPI()
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8003, reload=True)
