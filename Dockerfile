FROM python:3.12-alpine

WORKDIR /app

RUN wget -qO- https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.local/bin:$PATH"
ENV PATH="/app/.venv/bin:$PATH"

COPY pyproject.toml uv.lock /app
RUN uv sync --locked --no-install-project --no-dev


