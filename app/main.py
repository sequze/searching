from fastapi import FastAPI
from contextlib import asynccontextmanager
import uvicorn
from api import router as api_router
from core.config import settings
from core.models import db_helper, Base

@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    yield
    # shotdown
    db_helper.dispose()


app = FastAPI(lifespan=lifespan)
app.include_router(api_router, prefix=settings.api_prefix.prefix)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
    