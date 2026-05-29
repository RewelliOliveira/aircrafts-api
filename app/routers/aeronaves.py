from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.crud import crud
from app.database.db import get_db
from app.schemas.schemas import AeronaveCreate, AeronaveResponse

router = APIRouter(prefix="/companhias/{companhia_id}/aeronaves", tags=["Aeronaves"])


@router.get("/", response_model=List[AeronaveResponse])
def listar_frota(companhia_id: int, db: Session = Depends(get_db)):
    companhia = crud.get_companhia(db, companhia_id)
    if not companhia:
        raise HTTPException(status_code=404, detail="Companhia não encontrada")
    return crud.get_frota(db, companhia_id)


@router.get("/{aeronave_id}", response_model=AeronaveResponse)
def buscar_aeronave(companhia_id: int, aeronave_id: int, db: Session = Depends(get_db)):
    aeronave = crud.get_aeronave(db, aeronave_id)
    if not aeronave or aeronave.companhia_id != companhia_id:
        raise HTTPException(status_code=404, detail="Aeronave não encontrada")
    return aeronave


@router.post("/", response_model=AeronaveResponse, status_code=201)
def adicionar_aeronave(companhia_id: int, dados: AeronaveCreate, db: Session = Depends(get_db)):
    companhia = crud.get_companhia(db, companhia_id)
    if not companhia:
        raise HTTPException(status_code=404, detail="Companhia não encontrada")
    return crud.adicionar_aeronave(db, companhia_id, dados)


@router.delete("/{aeronave_id}", status_code=204)
def remover_aeronave(companhia_id: int, aeronave_id: int, db: Session = Depends(get_db)):
    aeronave = crud.remover_aeronave(db, companhia_id, aeronave_id)
    if not aeronave:
        raise HTTPException(status_code=404, detail="Aeronave não encontrada")
