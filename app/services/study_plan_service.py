from uuid import UUID
from typing import List, Optional
from app.models.study_plan import StudyPlan, StudyPlanCreate, StudyPlanUpdate
from app.repositories.study_plan_repository import StudyPlanRepository

from prometheus_client import Counter

study_plan_created = Counter("study_plan_created_total", "Количество созданных учебных планов")
study_plan_updated = Counter("study_plan_updated_total", "Количество обновленных учебных планов")
study_plan_deleted = Counter("study_plan_deleted_total", "Количество удаленных учебных планов")


class CourseValidationService:

    def validate_course(self, course_id: UUID) -> bool:
        print(f"Валидация курса {course_id}...")
        return True

class StudyPlanService:
    def __init__(self, repository: StudyPlanRepository):
        self.repository = repository
        self.course_validator = CourseValidationService()

    def create_study_plan(self, plan_data: StudyPlanCreate) -> StudyPlan:
        study_plan_created.inc()
        for course_id in plan_data.course_ids:
            if not self.course_validator.validate_course(course_id):
                raise ValueError(f"Курс {course_id} не существует")

        return self.repository.create(plan_data)

    def update_study_plan(self, plan_id: UUID, update_data: StudyPlanUpdate) -> Optional[StudyPlan]:
        study_plan_updated.inc()
        return self.repository.update(plan_id, update_data)

    def delete_study_plan(self, plan_id: UUID) -> bool:
        study_plan_deleted.inc()
        return self.repository.delete(plan_id)


