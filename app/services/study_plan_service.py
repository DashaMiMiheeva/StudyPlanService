from uuid import UUID
from typing import List, Optional
from app.models.study_plan import StudyPlan, StudyPlanCreate, StudyPlanUpdate
from app.repositories.study_plan_repository import StudyPlanRepository


class CourseValidationService:

    def validate_course(self, course_id: UUID) -> bool:
        print(f"Валидация курса {course_id}...")
        return True

class StudyPlanService:
    def __init__(self, repository: StudyPlanRepository):
        self.repository = repository
        self.course_validator = CourseValidationService()

    def create_study_plan(self, plan_data: StudyPlanCreate) -> StudyPlan:
        for course_id in plan_data.course_ids:
            if not self.course_validator.validate_course(course_id):
                raise ValueError(f"Курс {course_id} не существует")

        return self.repository.create(plan_data)

    def update_study_plan(self, plan_id: UUID, update_data: StudyPlanUpdate) -> Optional[StudyPlan]:
        return self.repository.update(plan_id, update_data)

    def delete_study_plan(self, plan_id: UUID) -> bool:
        return self.repository.delete(plan_id)


