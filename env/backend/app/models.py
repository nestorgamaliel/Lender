from sqlalchemy import Column, Integer, String
from .database import Base

class DocumentsTypes(Base):
    __tablename__ = "documents_types"

    documentsTypesId = Column(Integer, primary_key=True, index=True)
    documentsName = Column(String, index=True)

