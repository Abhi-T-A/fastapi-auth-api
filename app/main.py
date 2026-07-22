from fastapi import FastAPI
from app.supabase_client import supabase

app = FastAPI(
    title="FastAPI Auth API"
)

@app.get("/")
def root():
    return {
        "message": "Hey Abhi,Server running and connected to Supabase"
    }