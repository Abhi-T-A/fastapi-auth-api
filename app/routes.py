from fastapi import APIRouter, Request, HTTPException, status
from fastapi.responses import JSONResponse

public_router = APIRouter(
    prefix="/public",
    tags=["Public"]
)

protected_router = APIRouter(
    prefix="/protected",
    tags=["Protected"]
)


@public_router.get("/info", status_code=status.HTTP_200_OK)
def public_info():
    return {"message": "Welcome stranger! This info is public."}


@protected_router.get("/profile", status_code=status.HTTP_200_OK)
def protected_profile_stage2(request: Request):
    auth_header = request.headers.get("Authorization")
    
    if not auth_header or not auth_header.startswith("Bearer "):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={"error": "Access token required"}
        )
    
    token = auth_header.split(" ")[1].strip()
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={"error": "Access token required"}
        )

    # For Stage 2, unverified check passes token extraction
    return {"message": "Access token provided (unverified in Stage 2)", "token": token}
