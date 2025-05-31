.PHONY: build up down lint run

build:
	@docker build . -t llamachat

up:
	@docker compose up -d

down:
	@docker compose down

lint:
	@docker exec -it llamachat uv run black .; \
	docker exec -it llamachat uv run ruff check; \
	docker exec -it llamachat uv run mypy .

run:
	@docker exec -it llamachat uv run /app/src/llamachat/llamachat.py