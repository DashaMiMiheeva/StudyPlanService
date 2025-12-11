from uuid import UUID
from typing import List, Optional
from sqlalchemy.orm import Session

from app.models.study_plan import StudyPlan, StudyPlanCreate, StudyPlanUpdate
from app.schemas.study_plan import StudyPlanDB


class StudyPlanRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, plan_data: StudyPlanCreate) -> StudyPlan:
        db_plan = StudyPlanDB(
            title=plan_data.title,
            description=plan_data.description,
            student_id=plan_data.student_id,
            course_ids=plan_data.course_ids
        )
        self.db.add(db_plan)
        self.db.commit()
        self.db.refresh(db_plan)
        return StudyPlan.model_validate(db_plan)

    def update(self, plan_id: UUID, update_data: StudyPlanUpdate) -> Optional[StudyPlan]:
        db_plan = self.db.query(StudyPlanDB).filter(StudyPlanDB.id == plan_id).first()
        if not db_plan:
            return None

        update_dict = update_data.model_dump(exclude_unset=True)
        for field, value in update_dict.items():
            if value is not None:
                setattr(db_plan, field, value)

        self.db.commit()
        self.db.refresh(db_plan)
        return StudyPlan.model_validate(db_plan)

    def delete(self, plan_id: UUID) -> bool:
        db_plan = self.db.query(StudyPlanDB).filter(StudyPlanDB.id == plan_id).first()
        if not db_plan:
            return False

        self.db.delete(db_plan)
        self.db.commit()
        return True


