from fastapi import FastAPI
from app.endpoints.study_plan_router import router as study_plan_router
from app.database import create_tables

app = FastAPI(
    title="Study Plan Service API",
    description="Микросервис для управления учебными планами",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

@app.on_event("startup")
def startup():
    create_tables()
    print("Study Plan Service запущен")

@app.get("/")
def root():
    return {
        "service": "Study Plan Service",
        "docs": "/docs",
        "endpoints": ["GET /api/study-plans", "POST /api/study-plans"]
    }

@app.get("/health")
def health():
    return {"status": "healthy"}

app.include_router(study_plan_router)