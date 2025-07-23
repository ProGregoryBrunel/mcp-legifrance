"""Validation des variables d'environnement nécessaires."""

from __future__ import annotations

import os
import sys

REQUIRED = ["CLIENT_ID", "CLIENT_SECRET", "PORT", "LOG_LEVEL"]


def main() -> None:
    """Vérifie que toutes les variables sont présentes."""
    missing = [var for var in REQUIRED if not os.getenv(var)]
    if missing:
        print(f"Variables manquantes : {', '.join(missing)}", file=sys.stderr)
        sys.exit(1)
    print("Environnement valide.")


if __name__ == "__main__":
    main()
