from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import auth, vault, query

app = FastAPI(title="Cognivault API", version="0.1.0")

# Allow frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(vault.router, prefix="/vault", tags=["Vault"])
app.include_router(query.router, prefix="/query", tags=["Query"])

@app.get("/")
def root():
    return {"status": "ok", "project": "Cognivault"}
