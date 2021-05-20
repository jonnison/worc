FROM docker.io/library/python:3.8-slim

ENV PYTHONUNBUFFERED 1

COPY requirements.txt /tmp/
COPY . /src
RUN pip install -U pip
RUN pip install --no-cache-dir -r /tmp/requirements.txt
WORKDIR /src