from pydantic import BaseModel

class DocumentsTypesBase(BaseModel):
    name: str
    description: str

class DocumentsTypesCreate(DocumentsTypesBase):
    pass

class DocumentsTypesUpdate(DocumentsTypesBase):
    pass

class DocumentsTypes(DocumentsTypesBase):
    id: int

    class Config:
        orm_mode = True
