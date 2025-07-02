# Makefile for ML/NLP infra starter kit

build:
	docker compose up -d --build

bash:
	docker exec -it infra_kit_dev bash

stop:
	docker compose down

logs:
	docker logs infra_kit_dev

rebuild:
	docker compose down && docker compose up -d --build

test:
	pytest tests/

lint:
	black src/ tests/ scripts/ && isort src/ tests/ scripts/ && flake8 src/ tests/ scripts/
