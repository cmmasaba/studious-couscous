FROM python:3.12.0-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /api_service

COPY Pipfile* /api_service/
RUN pip install pipenv && pipenv install --system

ENV DJANGO_READ_DOT_ENV_FILE=True
ENV DOT_ENV_FILE=/api-service/.env

COPY . /api_service/