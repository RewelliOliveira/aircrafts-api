from typing import List, Optional
from pydantic import BaseModel, ConfigDict

class AeronaveCreate(BaseModel):
    prefixo: str
    modelo: str
    fabricante: str
    ano_fabricacao: int
    autonomia_km: float
    tipo: str
    piloto_automatico_ativo: bool = False

    # Campos exclusivos de AeronavePassageiros
    num_assentos: Optional[int] = None
    classes_disponiveis: Optional[str] = None 
    tripulacao_minima: Optional[int] = None

    # Campos exclusivos de AeronaveCarga
    capacidade_carga_kg: Optional[float] = None
    tipo_mercadoria: Optional[str] = None
    temperatura_controlada: Optional[bool] = None


class AeronaveResponse(AeronaveCreate):
    model_config = ConfigDict(from_attributes=True)

    id: int
    companhia_id: int

class CompanhiaAereaCreate(BaseModel):
    nome: str
    codigo_iata: str
    pais: str
    ano_fundacao: int


class CompanhiaAereaResponse(CompanhiaAereaCreate):
    model_config = ConfigDict(from_attributes=True)

    id: int
    frota: List[AeronaveResponse] = []
