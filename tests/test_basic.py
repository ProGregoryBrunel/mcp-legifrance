"""Tests basiques du serveur."""

from fastapi.testclient import TestClient
import os

os.environ.setdefault("CLIENT_ID", "test")
os.environ.setdefault("CLIENT_SECRET", "secret")

from legifrance_mcp.server import app


def test_unauthorized() -> None:
    """Vérifie la réponse 401."""
    client = TestClient(app)
    response = client.post("/messages", json={"token": "bad"})
    assert response.status_code == 401
