# Cria o servidor gRPC

# Imports
import grpc
import time
from tensorflow.keras.models import load_model
from concurrent import futures
import numpy as np

# Import dos módulos gerados a partir da compilação do arquivo proto
from grpc import iris_pb2_grpc, iris_pb2

# Variável para definir o número de segundos por dia
_ONE_DAY_IN_SECONDS = 60 * 60 * 24


# Cria uma classe carregar o modelo
class IrisPredictor(iris_pb2_grpc.IrisPredictorServicer):
    _model = None

    @classmethod
    # Obtém o modelo de ML
    def get_model(cls):
        if cls._model is None:
            cls._model = load_model('static/model/modelo1.h5')
        return cls._model

    # Função para fazer as previsões
    def PredictIrisSpecies(self, request):
        model = self.__class__.get_model()

        data = [request.sepal_length, request.sepal_width, request.petal_length, request.petal_width]

        data = np.array([np.asarray(data, dtype=float)])

        # Previsão do modelo
        predictions = model.predict(data)

        # Como são retornadas probabilidades, extraímos a maior, que indica a categor
        tipo = np.where(predictions == np.amax(predictions, axis=1))[1][0]

        if tipo == 0:
            pred_planta = 'Setosa'
        elif tipo == 1:
            pred_planta = 'Versicolor'
        else:
            pred_planta = 'Virginica'

        return iris_pb2.IrisPredictReply(species=pred_planta)


# Função para servir o modelo na porta 50052
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    iris_pb2_grpc.add_IrisPredictorServicer_to_server(IrisPredictor(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


# Execução do programa
if __name__ == '__main__':
    serve()
