from fastapi import APIRouter, Depends, status
from app.dependencies import get_current_user

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
def get_profile(current_user=Depends(get_current_user)):
    return {
        "id": current_user.id,
        "email": current_user.email,
        "created_at": str(current_user.created_at) if hasattr(current_user, "created_at") else None,
        "role": getattr(current_user, "role", "authenticated")
    }


@protected_router.get("/dashboard", status_code=status.HTTP_200_OK)
def get_dashboard(current_user=Depends(get_current_user)):
    return {
        "message": "Welcome to your protected dashboard!",
        "user_id": current_user.id,
        "email": current_user.email
    }


