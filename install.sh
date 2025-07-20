#!/bin/bash
set -e

echo "[install.sh] Building and setting up the environment..."

pip install --upgrade pip > /dev/null
echo "[install.sh] Installing dependencies..."
pip install -r requirements.txt

if [ ! -d alembic ]; then
    echo "[install.sh] Alembic migration folder missing. Exiting."
    exit 1
fi

export DATABASE_URL="sqlite+aiosqlite:///./test.db"
echo "[install.sh] Running migrations..."
alembic upgrade head

python3 -c "import db.models, sqlalchemy; from sqlalchemy.ext.asyncio import create_async_engine; import asyncio; async def ins():\n    engine = create_async_engine(\"sqlite+aiosqlite:///./test.db\");\n    async with engine.begin() as conn: await conn.run_sync(db.models.Base.metadata.create_all)\n; asyncio.run(ins())"

echo "[install.sh] Inserting sample employees..."
python3 scripts/seed_employees.py

echo "[install.sh] Environment ready."
