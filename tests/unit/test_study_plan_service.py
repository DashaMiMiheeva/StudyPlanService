from datetime import datetime

import pytest
from uuid import uuid4
from unittest.mock import Mock
from app.services.study_plan_service import StudyPlanService
from app.models.study_plan import StudyPlanCreate, StudyPlan, StudyPlanUpdate


@pytest.fixture
def mock_repo():
    return Mock()


@pytest.fixture
def service(mock_repo):
    return StudyPlanService(mock_repo)


def test_create_study_plan(service, mock_repo):
    create_data = StudyPlanCreate(
        title="Test",
        description="desc",
        student_id=uuid4(),
        course_ids=[uuid4()]
    )

    expected = StudyPlan(
        id=uuid4(),
        title=create_data.title,
        description=create_data.description,
        student_id=create_data.student_id,
        course_ids=create_data.course_ids,
        updated_at=datetime.now(),
        status="created",
        created_at=datetime.now(),
    )

    mock_repo.create.return_value = expected

    result = service.create_study_plan(create_data)

    assert result.title == "Test"
    mock_repo.create.assert_called_once_with(create_data)


def test_update_plan(service, mock_repo):
    plan_id = uuid4()
    update_data = StudyPlanUpdate(title="Новое название")

    expected = StudyPlan(
        id=plan_id,
        title="Новое название",
        description="desc",
        student_id=uuid4(),
        course_ids=[],
        created_at=datetime.now(),
        updated_at=datetime.now(),
        status="created"
    )

    mock_repo.update.return_value = expected

    result = service.update_study_plan(plan_id, update_data)

    assert result.title == "Новое название"
    mock_repo.update.assert_called_once()


def test_delete_plan(service, mock_repo):
    plan_id = uuid4()
    mock_repo.delete.return_value = True

    assert service.delete_study_plan(plan_id) is True
    mock_repo.delete.assert_called_once()
