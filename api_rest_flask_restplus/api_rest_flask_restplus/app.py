"""
Por padrão, a inicialização das aplicações Flask sempre ficam no arquivo app.py
"""
from tensorflow.keras.models import load_model
from flask import Flask, Blueprint
from flask_restplus import Api
from api_rest_flask_restplus.log import log
from api_rest_flask_restplus.endpoints.predict import ns_predict
from api_rest_flask_restplus.config import app_config
from api_rest_flask_restplus.config import api_restplus_config

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


"""
# Carrega o modelo treinado antes de abrir o servidor para requisições
@app.before_first_request
def load_model_to_app():
    app.predictor = load_model('./static/model/modelo1.h5')
"""


def initialize_app(app):
    app.config['RESTPLUS_VALIDATE'] = True  # Validação dos campos esperados em cada requisição
    app.config['ERROR_404_HELP'] = False  # Desabilita uma mensagem de erro padrão

    rest_app = Api(app, **api_restplus_config.app_infos)

    rest_app.add_namespace(ns_predict)  # Adiciona o nosso Namespaces (conjunto de endpoints)


def main():
    initialize_app(app)
    log.info(
        '>>>>> Starting development server at http://{}/ <<<<<'.format(app.config['SERVER_NAME']))
    app.run(host=app_config.HOST, port=app_config.PORT, debug=app_config.DEBUG)


if __name__ == '__main__':
    main()
