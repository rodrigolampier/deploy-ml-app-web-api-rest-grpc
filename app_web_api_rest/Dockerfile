# Inicia imagem do Ubuntu 18.04
FROM ubuntu:18.04

# Install pipenv
RUN apt-get update
RUN apt-get install -y build-essential python3.7 python3.7-dev python3-pip python3.7-venv

# Cria a pasta de trabalho
RUN set -ex && mkdir /app_web_api_rest
WORKDIR /app_web_api_rest

# Copia a pasta com a app
COPY . /app_web_api_rest

# Instala as dependências
RUN set -ex && pip3 install -r requirements.txt

# Executa o servidor web
EXPOSE 8080
ENV PYTHONPATH /app_web_api_rest
CMD python3 app.py