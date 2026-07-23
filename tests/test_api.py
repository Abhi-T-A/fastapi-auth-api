from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Server running and connected to Supabase"}


def test_public_info_endpoint():
    response = client.get("/public/info")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome stranger! This info is public."}


def test_protected_profile_unauthorized_missing_header():
    response = client.get("/protected/profile")
    assert response.status_code == 401
    assert response.json() == {"error": "Access token required"}


def test_protected_profile_unauthorized_invalid_token():
    headers = {"Authorization": "Bearer invalid_jwt_token_12345"}
    response = client.get("/protected/profile", headers=headers)
    assert response.status_code == 401
    assert response.json() == {"error": "Invalid or expired token"}


def test_protected_dashboard_unauthorized():
    response = client.get("/protected/dashboard")
    assert response.status_code == 401
    assert response.json() == {"error": "Access token required"}


def test_signup_missing_parameters():
    response = client.post("/auth/signup", json={"email": "test@example.com"})
    assert response.status_code == 400
    assert "error" in response.json()


def test_login_invalid_credentials():
    response = client.post("/auth/login", json={"email": "invalid_user_9999@example.com", "password": "wrongpassword"})
    assert response.status_code == 401
    assert response.json() == {"error": "Invalid login credentials"}
