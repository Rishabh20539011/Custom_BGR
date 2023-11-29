FROM ubuntu:latest

WORKDIR /frontend

RUN apt-get update -y >/dev/null 2>&1

RUN apt-get install -y ca-certificates curl gnupg supervisor

COPY supervisord_frontend.conf /etc/supervisor/conf.d/supervisord_frontend.conf

RUN mkdir -p /etc/apt/keyrings
RUN curl -fsSL https://deb.nodesource.com/gpgkey/nodesource-repo.gpg.key | gpg --dearmor -o /etc/apt/keyrings/nodesource.gpg

RUN echo "deb [signed-by=/etc/apt/keyrings/nodesource.gpg] https://deb.nodesource.com/node_16.x nodistro main" | tee /etc/apt/sources.list.d/nodesource.list
RUN apt update
RUN apt -y install nodejs -y
RUN npm i -g yarn >/dev/null 2>&1

COPY ./custom_bgr/project ./custom_bgr_frontend

