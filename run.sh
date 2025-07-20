#!/bin/bash
set -e

./install.sh

echo "[run.sh] Starting FastAPI server..."
exec uvicorn main:app --host 0.0.0.0 --port 8000
