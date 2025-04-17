from fastapi import APIRouter
from app.models.social_models import CommentRequest, SentimentResponse
from app.services.sentiment_service import analisar_sentimento

router = APIRouter()

@router.post("/analisar-comentario", response_model=SentimentResponse)
def analisar_comentario(payload: CommentRequest):
    comentario = payload.texto
    resultado = analisar_sentimento(comentario)

    return {
        "comentario": comentario,
        "sentimento": resultado["sentimento"],
        "estrelas": resultado["estrelas"],
        "porcentagem": resultado["porcentagem"]
    }