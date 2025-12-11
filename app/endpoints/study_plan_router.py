from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.study_plan import StudyPlan, StudyPlanCreate, StudyPlanUpdate
from app.services.study_plan_service import StudyPlanService
from app.repositories.study_plan_repository import StudyPlanRepository
from app.database import get_db

router = APIRouter(prefix="/api/study-plans", tags=["study-plans"])

def get_service(db: Session = Depends(get_db)) -> StudyPlanService:
    return StudyPlanService(StudyPlanRepository(db))

@router.post("/", response_model=StudyPlan, status_code=201)
def create_plan(
    plan: StudyPlanCreate,
    service: StudyPlanService = Depends(get_service)
):
    try:
        return service.create_study_plan(plan)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/{plan_id}", response_model=StudyPlan)
def update_plan(
    plan_id: UUID,
    plan_data: StudyPlanUpdate,
    service: StudyPlanService = Depends(get_service)
):
    plan = service.update_study_plan(plan_id, plan_data)
    if not plan:
        raise HTTPException(status_code=404, detail="План не найден")
    return plan

@router.delete("/{plan_id}")
def delete_plan(
    plan_id: UUID,
    service: StudyPlanService = Depends(get_service)
):
    if not service.delete_study_plan(plan_id):
        raise HTTPException(status_code=404, detail="План не найден")
    return {"message": "План удалён"}


