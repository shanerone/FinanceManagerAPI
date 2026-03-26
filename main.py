from fastapi import FastAPI

from contextlib import asynccontextmanager

from database import create_tables, delete_tables
from router import router as transaction_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # await delete_tables()
    await create_tables()
    print("DB ready")
    yield
    print("Off")


app = FastAPI(title = "Personal Finance Manager API", lifespan=lifespan)

app.include_router(transaction_router)


