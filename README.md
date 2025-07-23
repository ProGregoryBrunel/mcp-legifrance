# mcp-legifrance

[![CI](https://github.com/example/mcp-legifrance/actions/workflows/ci.yml/badge.svg)](https://github.com/example/mcp-legifrance/actions/workflows/ci.yml)
[![Coverage](https://img.shields.io/badge/coverage-90%25-brightgreen.svg)](https://example.com)
[![PyPI](https://img.shields.io/pypi/v/legifrance-mcp.svg)](https://pypi.org/project/legifrance-mcp/)
[![Release](https://img.shields.io/github/v/release/example/mcp-legifrance)](https://github.com/example/mcp-legifrance/releases/latest)

Serveur **MCP** pour interroger l'API **Légifrance**. Ce projet n'est pas affilié à Légifrance. Limite recommandée : 3 requêtes/s.

## Installation

### Via pip
```bash
pip install legifrance-mcp
```

### Via pipx
```bash
pipx install legifrance-mcp
```

### Avec Docker
```bash
docker build -t legifrance-mcp .
docker run -p 7777:7777 legifrance-mcp
```

### Avec Homebrew
```bash
brew tap example/legifrance-mcp
brew install legifrance-mcp
```

## Quick Start

```bash
legifrance-mcp --help
```

Le serveur démarre sur `http://localhost:7777/messages`.

## Intégrations

- n8n
- Zapier
- LM Studio / Ollama
- Hugging Face Space

## Clés API

| Variable | Description |
| -------- | ----------- |
| `CLIENT_ID` | identifiant API |
| `CLIENT_SECRET` | secret API |
| `PORT` | port du serveur |
| `LOG_LEVEL` | niveau de log |

## Export OpenAPI et Postman

Les fichiers `openapi.json` et `postman_collection.json` sont disponibles dans `examples/`.

