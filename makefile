all:
	docker build . -t mcp-wasmpython-runner
start:
	docker compose up -d
stop:
	docker compose down