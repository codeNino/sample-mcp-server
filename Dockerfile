FROM python:3.11-slim AS base

RUN apt-get update && apt-get install -y curl && apt-get clean

RUN curl -LsSf https://astral.sh/uv/install.sh | sh


ENV PATH="/root/.local/bin:${PATH}"

WORKDIR /app

COPY pyproject.toml uv.lock ./


RUN uv sync --frozen

COPY . .

EXPOSE 8000

CMD ["uv", "run", "python", "mcp_server.py"]


