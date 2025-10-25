from app.db.models import KYCRecord, KYCStatus

class FakedKYCProvider:
    """Simulates an external provider: it tests if the document ends with an even digit."""
    @staticmethod
    def verify(document_id: str) -> tuple[KYCStatus, str]:
        ref = f"prov-{document_id[-4:]}"
        try:
            last_digit = int(document_id[-1])
            return (KYCStatus.verified if last_digit % 2 == 0 else KYCStatus.rejected, ref)
        except Exception:
            return (KYCStatus.rejected, ref)
        
class KYCService:
    def __init__(self, provider: FakedKYCProvider):
        self.provider = provider
    
    def run_verification(self, record: KYCRecord) -> tuple[KYCStatus, str]:
        return self.provider.verify(record.document_id)
