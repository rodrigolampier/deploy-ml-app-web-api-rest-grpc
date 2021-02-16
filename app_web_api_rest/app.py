# Imports
from tensorflow.keras.models import load_model
from flask import Flask, request, jsonify, render_template
from flask_restplus import Api, Resource, fields
from utils.general import versao_python
from bussines import tratamento_dados_previsao as tdp
from config import app_config, api_restplus_config

# Instanciamos o Flask em uma variável chamada app
app = Flask(__name__)


# Carrega o modelo treinado antes de abrir o servidor para requisições
@app.before_first_request
def load_model_to_app():
    app.predictor = load_model('model/modelo1.h5')


"""APIs REST usando Flask puro"""


# Rota para a raiz da aplicação, onde temos o "Status da aplicação"
@app.route("/", methods=['GET', 'POST'])
def status():
    # return "Aplicação funcionando corretamente!", 200
    return jsonify({'mensagem': 'Aplicação funcionando corretamente!'}), 200


# Responde as requisições quando o usuário usa a aplicação web (http://localhost:8080/app)
# É retornado o template index.html, onde temos a aplicação web construída
@app.route("/app")
def index():
    return render_template('index.html', pred=" ")


# Para as previsões usamos o método POST para enviar as variáveis de entrada ao modelo
@app.route('/api/rest/predict', methods=['POST'])
def predict():
    # Objeto com as variáveis de entrada que vieram a através do formulário
    data = [request.form.get("sepal_length"),
            request.form.get("sepal_width"),
            request.form.get("petal_length"),
            request.form.get("petal_width")]

    data = tdp.tratamento_dados(data)
    predictions = tdp.previsao(data, app)
    pred_planta = tdp.tratamento_previsao(predictions)

    # Entrega na página web a previsão que foi realizada
    return render_template('index.html', pred=pred_planta)


"""
Essa API acima (http://localhost:8080/api/rest/predict) também poderia ser consumido por alguma outra aplicação além
da nossa aplicação Web que foi disponibilizada (index.html).
Caso o consumo/entrada seja por um formulário publicado (exemplo: nonssa app web), é necessário utilizar 
"request.form.get("sepal_length")" para podermos acessar os dados passados na request.
Caso o consumo/entrada seja por parâmetros de consulta de URL, é necessário utilizar 
"request.args.get("sepal_length")" para podermos acessar os dados passados na request.
"""

"""API REST usando Flask RestPlus"""

"""
A solução dada acima já está funcional e pronta para uso. Porém, vamos construir mais uma API, agora utilizando um 
complemento do Flask, o Flask-RESTPlus, que vai nos ajudar a manter o código mais organizado, gerando documentação e
outras facilidades adicionais.
"""

# Instância  um App REST, onde é necessário receber um objeto do Flask
rest_app = Api(app, **api_restplus_config.API_INFOS)

# Definição do endpoint
predict_endpoint = rest_app.namespace('restplus/predict',
                                      description='Endpoint responsável por disponibilizar o modelo de predição Iris.')

# Defini as variáveis de entrada da nossa API
predict_model = rest_app.model('Variáveis que devem ser informadas para a correta previsão pelo modelo:',
                               {'sepal_length': fields.Float(required=True,
                                                             description="Valor float contendo a sepal_length",
                                                             help="Ex. 5.1"),
                                'sepal_width': fields.Float(required=True,
                                                            description="Valor float contendo a sepal_width",
                                                            help="Ex. 3.5"),
                                'petal_length': fields.Float(required=True,
                                                             description="Valor float contendo a petal_length",
                                                             help="Ex. 1.4"),
                                'petal_width': fields.Float(required=True,
                                                            description="Valor float contendo a petal_width",
                                                            help="Ex. 0.2"),
                                })


@predict_endpoint.route("/")
class Predict(Resource):

    @rest_app.expect(predict_model)  # Indica que a função espera receber as variáveis configuradas no model acima
    def post(self):
        # Obtêm os parâmetros que foram passados na URL
        data = [request.args.get("sepal_length"),
                request.args.get("sepal_width"),
                request.args.get("petal_length"),
                request.args.get("petal_width")]

        data = tdp.tratamento_dados(data)
        predictions = tdp.previsao(data, app)
        pred_planta = tdp.tratamento_previsao(predictions)

        # Retorna a previsão em formato JSON
        return jsonify({'Previsão': pred_planta})


# Função main para execução do programa
def main():
    print(versao_python())
    app.run(host=app_config.HOST, port=app_config.PORT, debug=app_config.DEBUG)


# Execução do programa
if __name__ == '__main__':
    main()
