from datetime import date, datetime
from typing import Optional

from sqlalchemy import String, DateTime
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

engine = create_async_engine("postgresql+asyncpg://postgres:12345678@localhost:5432/finance_manager")

new_session = async_sessionmaker(engine, expire_on_commit=False)

class Model(DeclarativeBase):
    pass

class UserORM(Model):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(primary_key = True)
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[Optional[str]] = mapped_column(unique=True)
    hashed_password: Mapped[str]

class CategoryORM(Model):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key = True)
    name: Mapped[str]
    description: Mapped[Optional[str]]

class TransactionORM(Model):
    __tablename__ = "transactions"

    id: Mapped[int] = mapped_column(primary_key = True)
    user_id: Mapped[int]
    category_id: Mapped[int]
    amount: Mapped[float]
    description: Mapped[Optional[str]]
    type: Mapped[str] = mapped_column(String(10))
    date: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)

async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)