FROM node:20-alpine

LABEL name="olhadinha_front_end"
LABEL maintainer="Giovanny Cordeiro giovannycordeiropb@gmail.com"
LABEL description="Container frontend"
LABEL version="1.0"

RUN mkdir /app
WORKDIR /app

COPY package.json .

RUN npm install

COPY . .