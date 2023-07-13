FROM python:3.11

LABEL name="olhadinha_back_end"
LABEL maintainer="Giovanny Cordeiro giovannycordeiropb@gmail.com"
LABEL description="Ambiente de desenvolvimento para o projeto"
LABEL version="1.0"

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

COPY ./requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

RUN mkdir /src
WORKDIR /src
COPY ./src /src

RUN adduser user
USER user
