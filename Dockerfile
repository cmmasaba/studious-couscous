FROM python:3.12-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /api_service

COPY Pipfile Pipfile.lock /api_service/
RUN pip install pipenv && pipenv install --system

COPY . /api_service/