from uuid import UUID
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ConfigDict


class StudyPlanBase(BaseModel):
    title: str
    description: Optional[str] = None
    student_id: UUID
    course_ids: List[UUID] = []


class StudyPlanCreate(StudyPlanBase):
    pass


class StudyPlanUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    course_ids: Optional[List[UUID]] = None


class StudyPlan(StudyPlanBase):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    status: str
    created_at: datetime
    updated_at: datetime