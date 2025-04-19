all:
	docker build . -t mcp-wasmpython-runner
start:
	docker compose up -d --build
dev:
	docker compose up -w
stop:
	docker compose down