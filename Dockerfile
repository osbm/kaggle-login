FROM python:3

ADD . /app

ENTRYPOINT ["python", "/app/entrypoint.py"]