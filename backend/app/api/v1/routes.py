from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.sessions import get_db, Base, engine
from app.shcemas.kyc import KYCRequest, KYCResponse
from app.repositories.kyc_repository import KYCRepository
from app.services.kyc_service import KYCService, FakedKYCProvider
from app.db.models import KYCStatus

router = APIRouter()

#Create databse on the fly (demo purposes only). On production use Alembic migrations
Base.metadata.create_all(bind=engine)

@router.post("/kyc/verify", response_model=KYCResponse)
def verify_kyc(payload: KYCRequest, db: Session = Depends(get_db)):
    repo = KYCRepository(db)
    service = KYCService(FakedKYCProvider())

    record = repo.create(full_name=payload.full_name, document_id=payload.doucumrnt_id, 
                         country=payloady.country)
    status, provider_ref = service.run_verification(record)
    record = repo.set_status(record, status, provider_ref)

    if record.status == KYCStatus.rejected:
        # Error handling example
        raise HTTPException(status_code=400, detail="Verification rejected by provider")
    return KYCResponse(id=record.id, status=record.status, provider_reference=record.provider_reference)