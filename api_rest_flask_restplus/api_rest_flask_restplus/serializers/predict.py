from flask_restplus import fields
from api_rest_flask_restplus.restplus import api

# Defini as variáveis de entrada para esse endpoint
predict_serializer = api.model('predict espera os seguintes campos e formatos:',
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
