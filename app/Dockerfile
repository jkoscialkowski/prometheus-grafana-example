FROM python:3.11-slim

WORKDIR /code

RUN pip install uv && uv venv

ARG VIRTUAL_ENV=./.venv

COPY ./requirements.txt /code/requirements.txt

RUN uv pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./main.py /code/main.py

CMD [".venv/bin/uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
