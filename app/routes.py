from fastapi import APIRouter, Request, HTTPException, status
from app.supabase_client import supabase

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
def protected_profile_stage3(request: Request):
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

    try:
        user_response = supabase.auth.get_user(token)
        if not user_response or not user_response.user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail={"error": "Invalid or expired token"}
            )
        
        user = user_response.user
        return {
            "id": user.id,
            "email": user.email,
            "created_at": str(user.created_at) if hasattr(user, "created_at") else None,
            "role": getattr(user, "role", "authenticated")
        }
    except HTTPException:
        raise
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={"error": "Invalid or expired token"}
        )

