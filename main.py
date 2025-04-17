from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import social_routes
import app.routes.social_routes as sr


print("Router encontrado?", hasattr(sr, "router"))

app = FastAPI(
    title="Termômetro Social",
    description="API para análise de reações e comentários no Facebook e Instagram",
    version="1.0.0"
)

# Permitir chamadas da interface web (se houver frontend separado)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Trocar para domínio específico no deploy
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Importando as rotas da pasta routes
app.include_router(social_routes.router, prefix="/api/social", tags=["Social"])

# Rota raiz só pra teste
@app.get("/")
def read_root():
    return {"status": "Termômetro Social rodando com sucesso!"}