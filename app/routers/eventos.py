import os

import redis
from fastapi import APIRouter
from fastapi.responses import StreamingResponse

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")
CANAL = "frota_eventos"

router = APIRouter(prefix="/eventos", tags=["Eventos"])


def _stream_eventos():
    r = redis.from_url(REDIS_URL, decode_responses=True)
    pubsub = r.pubsub()
    pubsub.subscribe(CANAL)

    try:
        for mensagem in pubsub.listen():
            if mensagem["type"] == "message":
                dados = mensagem["data"]
                yield f"data: {dados}\n\n"
    except GeneratorExit:
        pass
    finally:
        pubsub.unsubscribe(CANAL)
        pubsub.close()
        r.close()


@router.get("/stream", summary="Stream de eventos em tempo real (SSE)")
def stream_eventos():
    return StreamingResponse(
        _stream_eventos(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no",
        },
    )
