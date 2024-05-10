FROM python:3.13.0b1-slim as builder

RUN python3 -m venv /venv && /venv/bin/pip install -U pip wheel setuptools && mkdir /src && mkdir /src/src

COPY pyproject.toml /src/

RUN /venv/bin/pip install '/src[bot]'

FROM python:3.13.0b1-slim

WORKDIR /src
COPY --from=builder /venv /venv
COPY src /src/src

CMD  ["/venv/bin/python", "-m", "medsyncapp.tgbot.bot"]
