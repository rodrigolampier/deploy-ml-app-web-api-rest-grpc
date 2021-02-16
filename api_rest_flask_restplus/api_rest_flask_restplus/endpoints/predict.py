from flask_restplus import Resource
from flask import request, jsonify
from api_rest_flask_restplus.app import res
from api_rest_flask_restplus.serializers import predict
from api_rest_flask_restplus.business import tratamento_dados_previsao as tdp

"""
O RESTPlus utiliza o conceito de Resources e Namespaces. Um Resource é basicamente a representação de algum 
endpoint da sua API. E um Namespace é um conjunto de Resources.
"""

# Definição do Namespace para o endpoint /predict
ns_predict = api.namespace('predict',
                           description='Endpoint responsável por disponibilizar o modelo de predição Iris.')


@ns_predict.route("/")  # Este decorator é utilizado para definir qual é a URL do endpoint
class Predict(Resource):
    """
    Resource é uma classe que contêm funções que serão mapeadas em métodos HTTP. Ou seja, para implementar um método
    HTTP put é necessário implementar uma função com o mesmo nome.
    """

    @api.expect(predict.predict_serializer)  # Documenta e valida o formato de entrada deste método post
    def post(self):
        print('Passou aqui!!!!!')
        # Obtêm os parâmetros que foram passados na URL
        data = [request.args.get("sepal_length"),
                request.args.get("sepal_width"),
                request.args.get("petal_length"),
                request.args.get("petal_width")]

        data = tdp.tratamento_dados(data)
        predictions = tdp.previsao(data)
        pred_planta = tdp.tratamento_previsao(predictions)

        # Retorna a previsão em formato JSON
        return jsonify({'Previsão': pred_planta})
