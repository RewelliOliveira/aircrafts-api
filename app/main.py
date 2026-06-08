from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database.db import Base, engine
from app.routers import aeronaves, companhias, eventos, frota

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Aircraft API",
    description="API REST para gerenciamento de companhias aéreas e suas frotas",
    version="1.0.0",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(companhias.router)
app.include_router(aeronaves.router)
app.include_router(eventos.router)
app.include_router(frota.router)


@app.get("/", tags=["Root"])
def root():
    return {"message": "Aircraft API rodando"}
