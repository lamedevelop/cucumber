FROM python:3 as builder

COPY requirements.txt /mnt/

RUN \
    python -m venv /app \
    && /app/bin/pip install -U pip \
    && /app/bin/pip install -Ur /mnt/requirements.txt


FROM python:3 as app

WORKDIR /app

COPY --from=builder /app /app
COPY . .

EXPOSE 8000

CMD /app/bin/python -m alembic upgrade head && /app/bin/uvicorn app.main:app --host=0.0.0.0 --port=8000