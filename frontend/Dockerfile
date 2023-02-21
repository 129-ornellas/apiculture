FROM node:18-slim

WORKDIR /frontend

ENV SHELL=/bin/sh LANG=en_US.UTF-8

RUN apt update && \
  apt install -y \
  curl \
  net-tools \
  build-essential

COPY package.json package-lock.json /frontend/

RUN npm install && \
  npm cache clean --force && \
  npm cache verify

COPY . /frontend/

RUN npm run build
CMD npm run start