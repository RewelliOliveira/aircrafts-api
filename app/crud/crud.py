from sqlalchemy.orm import Session

from app.models.models import Aeronave, CompanhiaAerea
from app.schemas.schemas import AeronaveCreate, CompanhiaAereaCreate


def get_companhias(db: Session):
    return db.query(CompanhiaAerea).all()


def get_companhia(db: Session, companhia_id: int):
    return db.query(CompanhiaAerea).filter(CompanhiaAerea.id == companhia_id).first()


def get_companhia_por_iata(db: Session, iata: str):
    return db.query(CompanhiaAerea).filter(
        CompanhiaAerea.codigo_iata == iata.upper()
    ).first()


def criar_companhia(db: Session, dados: CompanhiaAereaCreate):
    companhia = CompanhiaAerea(**dados.model_dump())
    db.add(companhia)
    db.commit()
    db.refresh(companhia)
    return companhia


def remover_companhia(db: Session, companhia_id: int):
    companhia = get_companhia(db, companhia_id)
    if companhia:
        db.delete(companhia)
        db.commit()
    return companhia


def get_frota(db: Session, companhia_id: int):
    return db.query(Aeronave).filter(Aeronave.companhia_id == companhia_id).all()


def get_aeronave(db: Session, aeronave_id: int):
    return db.query(Aeronave).filter(Aeronave.id == aeronave_id).first()


def adicionar_aeronave(db: Session, companhia_id: int, dados: AeronaveCreate):
    aeronave = Aeronave(**dados.model_dump(), companhia_id=companhia_id)
    db.add(aeronave)
    db.commit()
    db.refresh(aeronave)
    return aeronave


def remover_aeronave(db: Session, companhia_id: int, aeronave_id: int):
    aeronave = db.query(Aeronave).filter(
        Aeronave.id == aeronave_id,
        Aeronave.companhia_id == companhia_id
    ).first()
    if aeronave:
        db.delete(aeronave)
        db.commit()
    return aeronave
