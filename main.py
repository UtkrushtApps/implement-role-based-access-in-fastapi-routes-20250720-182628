from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from api.hr.employees import router as employees_router
from api.hr.finance import router as finance_router
import uvicorn

app = FastAPI()

# CORS middlewar for development/demo
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Custom structured error handler
@app.exception_handler(Exception)
async def custom_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "error": True,
            "message": str(exc),
            "detail": type(exc).__name__
        },
    )

# Routers
app.include_router(employees_router, prefix="/api/hr/employees", tags=["hr-employees"])
app.include_router(finance_router, prefix="/api/hr/finance", tags=["hr-finance"])

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)