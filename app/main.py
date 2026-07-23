from fastapi import FastAPI, Request, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from app.supabase_client import supabase
from app.auth import router as auth_router
from app.routes import public_router, protected_router

app = FastAPI(
    title="FastAPI Auth API",
    version="1.0.0"
)

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    if isinstance(exc.detail, dict):
        return JSONResponse(status_code=exc.status_code, content=exc.detail)
    return JSONResponse(status_code=exc.status_code, content={"error": exc.detail})

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"error": "Missing or invalid request parameters"}
    )

app.include_router(auth_router)
app.include_router(public_router)
app.include_router(protected_router)

@app.get("/")
def root():
    return {
        "message": "Server running and connected to Supabase"
    }
