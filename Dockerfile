FROM python:3.13-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

COPY . /app

WORKDIR /app

RUN uv sync --frozen --no-cache

CMD ["/app/.venv/bin/fastapi", "run", "src/tlacuilo/api/routes.py", "--port", "8000", "--host", "0.0.0.0"]
