# import pytest
# from fastapi.testclient import TestClient
# from uuid import uuid4
# from app.main import app
# from app.database import Base, get_db
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
#
# SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
# engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
# TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#
# def override_get_db():
#     db = TestingSessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
#
# app.dependency_overrides[get_db] = override_get_db
#
# Base.metadata.create_all(bind=engine)
#
# client = TestClient(app)
#
# @pytest.fixture
# def sample_plan_data():
#     return {
#         "title": "Учебный план",
#         "description": "Описание плана",
#         "student_id": str(uuid4()),
#         "course_ids": [str(uuid4()), str(uuid4())]
#     }
#
# @pytest.fixture
# def created_plan(sample_plan_data):
#     response = client.post("/api/study-plans/", json=sample_plan_data)
#     assert response.status_code == 201
#     return response.json()
#
#
# def test_create_plan(sample_plan_data):
#     response = client.post("/api/study-plans/", json=sample_plan_data)
#     assert response.status_code == 201
#     data = response.json()
#     assert data["title"] == sample_plan_data["title"]
#     assert data["description"] == sample_plan_data["description"]
#     assert data["student_id"] == sample_plan_data["student_id"]
#     assert data["course_ids"] == sample_plan_data["course_ids"]
#     assert "id" in data
#
# def test_update_plan(created_plan):
#     plan_id = created_plan["id"]
#     update_data = {"title": "Обновлённый план"}
#     response = client.put(f"/api/study-plans/{plan_id}", json=update_data)
#     assert response.status_code == 200
#     data = response.json()
#     assert data["title"] == "Обновлённый план"
#     assert data["description"] == created_plan["description"]
#
# def test_delete_plan(created_plan):
#     plan_id = created_plan["id"]
#     response = client.delete(f"/api/study-plans/{plan_id}")
#     assert response.status_code == 200
#     data = response.json()
#     assert data["message"] == "План удалён"
#     response = client.put(f"/api/study-plans/{plan_id}", json={"title": "test"})
#     assert response.status_code == 404
