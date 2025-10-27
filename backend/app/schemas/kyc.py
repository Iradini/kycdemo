from pydantic import BaseModel, Field
from typing import Optional

class KYCRequest(BaseModel):
    full_name: str = Field(..., min_length=2)
    document_id: str = Field(..., min_length=4)
    country: str = Field(..., min_length=2, max_length=3)

class KYCResponse(BaseModel):
    id: int
    status: str
    provider_reference: Optional[str] = None