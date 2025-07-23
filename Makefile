install:
pip install -e .[dev]

lint:
ruff . && black --check . && mypy legifrance_mcp

test:
pytest --cov=legifrance_mcp --cov-report=term-missing

run:
legifrance-mcp

docker-build:
docker build -t legifrance-mcp .

compose-up:
docker-compose up
