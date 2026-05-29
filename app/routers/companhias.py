from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.crud import crud
from app.database.db import get_db
from app.schemas.schemas import CompanhiaAereaCreate, CompanhiaAereaResponse

router = APIRouter(prefix="/companhias", tags=["Companhias"])


@router.get("/", response_model=List[CompanhiaAereaResponse])
def listar_companhias(db: Session = Depends(get_db)):
    return crud.get_companhias(db)


@router.get("/iata/{codigo}", response_model=CompanhiaAereaResponse)
def buscar_por_iata(codigo: str, db: Session = Depends(get_db)):
    companhia = crud.get_companhia_por_iata(db, codigo)
    if not companhia:
        raise HTTPException(status_code=404, detail="Companhia não encontrada")
    return companhia


@router.get("/{companhia_id}", response_model=CompanhiaAereaResponse)
def buscar_companhia(companhia_id: int, db: Session = Depends(get_db)):
    companhia = crud.get_companhia(db, companhia_id)
    if not companhia:
        raise HTTPException(status_code=404, detail="Companhia não encontrada")
    return companhia


@router.post("/", response_model=CompanhiaAereaResponse, status_code=201)
def criar_companhia(dados: CompanhiaAereaCreate, db: Session = Depends(get_db)):
    return crud.criar_companhia(db, dados)


@router.delete("/{companhia_id}", status_code=204)
def remover_companhia(companhia_id: int, db: Session = Depends(get_db)):
    companhia = crud.remover_companhia(db, companhia_id)
    if not companhia:
        raise HTTPException(status_code=404, detail="Companhia não encontrada")
