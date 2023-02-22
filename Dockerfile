FROM python:3.11-slim

WORKDIR /backend

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONIOENCODING=UTF-8
ENV SHELL=/bin/sh LANG=en_US.UTF-8

RUN apt update && \
  apt install -y \
  curl \
  net-tools \
  build-essential \
  libpq-dev \
  python3-dev

COPY requirements.txt pyproject.toml /backend/
RUN pip install -r requirements.txt

COPY . /backend/

EXPOSE 8000