from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.crud import crud
from app.database.db import get_db
from app.schemas.schemas import AeronaveResponse

router = APIRouter(prefix="/aeronaves", tags=["Frota Global"])

@router.get("/", response_model=List[AeronaveResponse])
def listar_todas_aeronaves(db: Session = Depends(get_db)):
    """Retorna todas as aeronaves de todas as companhias."""
    return crud.get_todas_aeronaves(db)
