from sqlalchemy import Column, String, Text, DateTime, JSON
from sqlalchemy.dialects.postgresql import UUID, ARRAY
from sqlalchemy.sql import func
from app.schemas.base_schema import Base

class StudyPlanDB(Base):
    __tablename__ = "study_plans"

    # id = Column(UUID(as_uuid=True), primary_key=True, server_default=func.gen_random_uuid())
    id = Column(String, primary_key=True)
    title = Column(String(200), nullable=False)
    description = Column(Text)
    # student_id = Column(UUID(as_uuid=True), nullable=False)
    student_id = Column(String, nullable=False)
    # course_ids = Column(ARRAY(UUID(as_uuid=True)), default=[])
    course_ids = Column(JSON, default=list)
    status = Column(String(20), default="draft", nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())