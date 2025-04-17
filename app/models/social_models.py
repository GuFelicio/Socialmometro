from pydantic import BaseModel

class CommentRequest(BaseModel):
    texto: str

class SentimentResponse(BaseModel):
    comentario: str
    sentimento: str
    estrelas: int
    porcentagem: int