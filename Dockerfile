# Use an official Python image
FROM python:3.11-slim AS base

# Install curl (required to install uv), and other useful libs
RUN apt-get update && apt-get install -y curl && apt-get clean

# Install uv
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

# Add uv to PATH
ENV PATH="/root/.local/bin:${PATH}"

# Set work directory
WORKDIR /app

# Copy project metadata first (faster builds due to caching)
COPY pyproject.toml uv.lock ./

# Install dependencies using uv
RUN uv sync --frozen

COPY . .


EXPOSE 8000

CMD ["uv", "run", "uvicorn", "app.main:server", "--host", "0.0.0.0", "--port", "8000"]


