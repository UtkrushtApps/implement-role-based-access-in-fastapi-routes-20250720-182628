import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from db.models import Employee
import os

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./test.db")
engine = create_async_engine(DATABASE_URL, echo=False, future=True)
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def seed():
    async with AsyncSessionLocal() as session:
        exists = await session.execute("SELECT COUNT(*) FROM employees")
        count = exists.scalar()
        if count == 0:
            session.add_all([
                Employee(name="Alice Smith", department="HR"),
                Employee(name="Bob Johnson", department="Engineering"),
                Employee(name="Charlie Lee", department="HR"),
            ])
            await session.commit()
asyncio.run(seed())
