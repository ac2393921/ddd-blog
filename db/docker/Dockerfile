FROM python:3.9.13-slim as python-base

ENV PYTHON_VERSHIN=python3.9 \
    PYTHONUNBUFFERED=1 \
    # prevents python creating .pyc files
    PYTHONDONTWRITEBYTECODE=1 \
    \
    # pip
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    \
    # make rye install to this location
    RYE_HOME="/home/.rye" \
    # paths
    # this is where our requirements + virtual environment will live
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"

# prepend rye and venv to path
ENV PATH ${RYE_HOME}/shims:$VENV_PATH/bin:$PATH

FROM python-base as builder-base
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
    # deps for installing rye
    curl \
    # deps for building python deps
    build-essential \
    gcc libmariadb-dev

RUN curl -sSf https://rye-up.com/get | RYE_NO_AUTO_INSTALL=1 RYE_INSTALL_OPTION="--yes" bash

WORKDIR $PYSETUP_PATH
COPY pyproject.toml requirements.lock requirements-dev.lock ./

RUN --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    --mount=type=bind,source=requirements.lock,target=requirements.lock \
    --mount=type=bind,source=requirements-dev.lock,target=requirements-dev.lock \
    --mount=type=bind,source=.python-version,target=.python-version\
    --mount=type=bind,source=README.md,target=README.md \
    rye sync --no-lock

ENV PYTHONPATH /src

FROM builder-base as develop
COPY --from=builder-base $PYSETUP_PATH/.venv/lib/$PYTHON_VERSHIN/site-packages /user/local/lib/$PYTHON_VERSHIN/site-packages

ENV PYTHONPATH /src
