from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database.db import Base


class CompanhiaAerea(Base):
    __tablename__ = "companhias"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    codigo_iata = Column(String, unique=True, nullable=False, index=True)
    pais = Column(String, nullable=False)
    ano_fundacao = Column(Integer, nullable=False)

    frota = relationship("Aeronave", back_populates="companhia", cascade="all, delete-orphan")


class Aeronave(Base):
    __tablename__ = "aeronaves"

    id = Column(Integer, primary_key=True, index=True)
    prefixo = Column(String, unique=True, nullable=False)
    modelo = Column(String, nullable=False)
    fabricante = Column(String, nullable=False)
    ano_fabricacao = Column(Integer, nullable=False)
    autonomia_km = Column(Float, nullable=False)
    tipo = Column(String, nullable=False)  
    piloto_automatico_ativo = Column(Boolean, default=False)
    companhia_id = Column(Integer, ForeignKey("companhias.id"), nullable=False)
    companhia = relationship("CompanhiaAerea", back_populates="frota")
    num_assentos = Column(Integer, nullable=True)
    classes_disponiveis = Column(String, nullable=True)
    tripulacao_minima = Column(Integer, nullable=True)
    capacidade_carga_kg = Column(Float, nullable=True)
    tipo_mercadoria = Column(String, nullable=True)
    temperatura_controlada = Column(Boolean, nullable=True)