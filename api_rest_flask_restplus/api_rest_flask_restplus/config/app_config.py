import os

# Armazena a localização atual do arquivo de config/base do projeto
BASEDIR = os.path.dirname(os.path.realpath(__file__))

HOST = '0.0.0.0'  # Isso é igual a localhost
PORT = 8080

# Caso o servidor note alterações ele reinicia automaticamente
DEBUG = True
