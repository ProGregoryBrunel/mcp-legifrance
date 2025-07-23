"""Serveur FastAPI exposant l'endpoint MCP."""

from __future__ import annotations

from fastapi import FastAPI, HTTPException, Request

from .config import get_settings

app = FastAPI(title="Legifrance MCP")
settings = get_settings()


@app.post("/messages")
async def messages(request: Request) -> dict[str, str]:
    """Endpoint principal JSON-RPC."""
    data = await request.json()
    if data.get("token") != settings.client_secret:
        raise HTTPException(status_code=401, detail="Non autorisé")
    return {"message": "ok"}
