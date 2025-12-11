import pytest
from uuid import uuid4
from pydantic import ValidationError
from app.models.study_plan import StudyPlan, StudyPlanCreate, StudyPlanUpdate


def test_study_plan_create_valid():
    data = StudyPlanCreate(
        title="План по Python",
        description="Изучение базовых тем",
        student_id=uuid4(),
        course_ids=[uuid4(), uuid4()]
    )
    assert data.title == "План по Python"
    assert len(data.course_ids) == 2


def test_study_plan_create_missing_title():
    with pytest.raises(ValidationError):
        StudyPlanCreate(
            description="Описание",
            student_id=uuid4(),
            course_ids=[]
        )


def test_study_plan_update_partial():
    update = StudyPlanUpdate(description="Новое описание")
    assert update.description == "Новое описание"
