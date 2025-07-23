"""Interface en ligne de commande."""  # pragma: no cover

from __future__ import annotations

import typer  # type: ignore
from uvicorn import run

from .server import app
from .config import get_settings

cli = typer.Typer(help="Serveur MCP Légifrance")


@cli.command()  # type: ignore[misc]
def start() -> None:
    """Démarre le serveur."""
    settings = get_settings()
    run(
        app, host="0.0.0.0", port=settings.port, log_level=settings.log_level
    )  # nosec B104


if __name__ == "__main__":
    cli()
