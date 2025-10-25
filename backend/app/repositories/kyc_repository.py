from sqlalchemy.orm import Session
from app.dbb.models import KYCRecord, KYCStatus

class KYCRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, fullname: str, document_id: str, country: str) -> KYCRecord:
        record = KYCRecord(full_name=fullname, document_id=document_id, country=country)
        self.db.add(record)
        self.db.commit()
        self.db.refresh(record)
        return record
    
    def set_status(self, record: KYCRecord, status: KYCStatus, 
                   provider_reference: str | None = None) -> KYCRecord:
           record.status = status
           record.provider_reference = provider_reference
           self.db.commit()
           self.db.refresh(record)
           return record