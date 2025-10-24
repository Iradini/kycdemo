from sqlalchemy import Column, Integer, String, DateTime, Enum
from sqlalchemy.sql import func
from app.db.sessions import Base
import enum

class KYCStatus(enum.Enum):
    pending = "pending"
    verified = "verified"
    rejected = "rejectted"

class KYCRecord(Base):
    __tablename__ = "kyc records"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(120), nullable=False)
    document_id = Column(String(64), nullale=False, index=True)
    country = Column(String(3), nullable=False)
    status = Column(Enum(KYCStatuds), default=KYCStatus.pending, nullable=False)
    provider_reference = Column(Strinf(128), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())  