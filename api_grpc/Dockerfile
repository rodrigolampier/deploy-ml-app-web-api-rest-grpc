FROM ubuntu:16.04

WORKDIR /root

# Obtém a imagem do Ubuntu e as dependências
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        curl \
        pkg-config \
        rsync \
        software-properties-common \
        unzip \
        git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Instala o miniconda
RUN curl -LO https://repo.continuum.io/miniconda/Miniconda3-4.7.12.1-Linux-x86_64.sh \
      && bash Miniconda3-4.7.12.1-Linux-x86_64.sh -p /miniconda -b \
      && rm Miniconda3-4.7.12.1-Linux-x86_64.sh
ENV PATH /miniconda/bin:$PATH

# Limpa tudo que foi executado e remove arquivos usados apenas na instalação
RUN conda clean -tp -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

EXPOSE 50052

COPY . /root/
CMD ["python", "grpc_server.py"]