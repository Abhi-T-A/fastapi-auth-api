# FastAPI Auth API

A production-ready authentication API built with **FastAPI** and **Supabase**, featuring JWT-based auth, Pydantic schemas, and a clean modular structure.

---

## 📁 Project Structure

```
fastapi-auth-api/
│
├── .venv/
│
├── app/
│   ├── __init__.py
│   ├── main.py            # FastAPI app entry point
│   ├── config.py          # Environment variable loading
│   ├── supabase_client.py # Supabase client initialisation
│   ├── auth.py            # Stage 1 — Auth routes (signup / signin)
│   ├── dependencies.py    # Stage 4 — JWT auth dependency
│   ├── schemas.py         # Stage 1 — Pydantic request/response models
│   └── models.py          # (optional) ORM / DB models
│
├── screenshots/
│   └── swagger.png        # Stage 5 — Swagger UI screenshot
│
├── .env                   # ❗ Project root — local secrets (gitignored)
├── .env.example           # Template for required env vars
├── .gitignore
├── README.md
├── requirements.txt
└── walkthrough.md
```

---

## ⚙️ Setup

### 1. Clone & create virtual environment

```bash
git clone <repo-url>
cd fastapi-auth-api
python -m venv .venv
.venv\Scripts\activate   # Windows
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment variables

Copy `.env.example` to `.env` and fill in your Supabase credentials:

```bash
copy .env.example .env
```

```env
SUPABASE_URL=https://your-project-ref.supabase.co
SUPABASE_KEY=your-anon-or-service-role-key
```

### 4. Run the server

```bash
uvicorn app.main:app --reload
```

Visit **http://127.0.0.1:8000/docs** for the interactive Swagger UI.

---

## 🔑 Auth Endpoints

| Method | Endpoint        | Description              |
|--------|-----------------|--------------------------|
| POST   | `/auth/signup`  | Register a new user      |
| POST   | `/auth/signin`  | Sign in & get JWT token  |
| GET    | `/`             | Health check             |

---

## 🛡️ Protected Routes (Stage 4)

Use `get_current_user` from `app/dependencies.py` as a FastAPI dependency:

```python
from app.dependencies import get_current_user

@router.get("/me")
def get_me(user = Depends(get_current_user)):
    return user
```

Pass the token in the `Authorization` header:
```
Authorization: Bearer <access_token>
```

---

## 📸 Swagger UI

![Swagger UI](screenshots/swagger.png)

---

## 📄 License

MIT
