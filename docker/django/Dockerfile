FROM python:3.11-buster AS builder

RUN pip install poetry==1.8.3

ENV POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /app

COPY pyproject.toml poetry.lock .
RUN touch README.md

RUN poetry install --with dev --no-interaction && rm -rf $POETRY_CACHE_DIR

FROM python:3.11-slim AS runtime

ENV VIRTUAL_ENV=/app/.venv \
    PATH="/app/.venv/bin:$PATH" \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}
