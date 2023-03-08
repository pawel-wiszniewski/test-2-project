FROM python:3.10.6-slim-buster AS base

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=240 \
  POETRY_HOME="/opt/poetry" \
  POETRY_NO_INTERACTION=1 \
  POETRY_VERSION=1.4.0 \
  POETRY_VIRTUALENVS_IN_PROJECT=true \
  PIPX_VERSION=1.1.0 \
  PIPX_BIN_DIR=/opt/pipx/bin \
  PATH=/opt/pipx/bin:$PATH

WORKDIR /app

RUN apt-get update -y && \
    apt-get install -y curl

RUN pip install -U pipx=="$PIPX_VERSION" && \
    pipx ensurepath && \
    pipx install poetry=="$POETRY_VERSION"

COPY pyproject.toml poetry.lock /app/
RUN poetry install --no-ansi --only main --no-root

COPY ./src /app

ENV VIRTUAL_ENV=/app/.venv
ENV PATH="${VIRTUAL_ENV}/bin:$PATH"

ENTRYPOINT ["python"]
