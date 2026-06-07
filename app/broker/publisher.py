import json
import os
from datetime import datetime, timezone

import redis

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")
CANAL = "frota_eventos"

_redis_client: redis.Redis | None = None


def get_redis() -> redis.Redis:
    global _redis_client
    if _redis_client is None:
        _redis_client = redis.from_url(REDIS_URL, decode_responses=True)
    return _redis_client


def publicar_evento(tipo: str, dados: dict) -> None:
    evento = {
        "tipo": tipo,
        "dados": dados,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
    try:
        get_redis().publish(CANAL, json.dumps(evento))
    except Exception as e:
        print(f"[BROKER] Falha ao publicar evento {tipo}: {e}")
