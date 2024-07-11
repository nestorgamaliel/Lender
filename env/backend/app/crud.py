from sqlalchemy.orm import Session
from . import models, schemas

def getDocumentsType(db: Session, documentsTypeId: int):
    return db.query(models.DocumentsTypes).filter(\
        models.DocumentsTypes.documentsTypesId == \
            documentsTypeId).first()

def getDocumentsTypes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.DocumentsTypes).offset(skip).limit(limit).all()

def createDocumentsType(db: Session, documentsTypes: schemas.DocumentsTypesCreate):
    db_item = models.DocumentsTypes(documentsTypesId=documentsTypes.documentsTypesId, documentsName=documentsTypes.documentsName)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def updateDocumentsTypes(db: Session, documentsTypesId: int, documentsTypes: schemas.ItemUpdate):
    db_item = db.query(models.DocumentsTypes).filter(models.DocumentsTypes.documentsTypesId == documentsTypesId).first()
    if db_item:
        db_item.documentsName = documentsTypes.documentsName
        db.commit()
        db.refresh(db_item)
    return db_item

def deleteDocumentsTypes(db: Session, documentsTypesId: int):
    db_item = db.query(models.DocumentsTypes).filter(models.DocumentsTypes.documentsTypesId == documentsTypesId).first()
    if db_item:
        db.delete(db_item)
        db.commit()
    return db_item
