from fastapi import FastAPI
from .api.main_router import main_router

app = FastAPI(title="Wordle project")

app.include_router(main_router, prefix="/api")

@app.get("/health")
def health_check():
    return {"status": "ok"}
