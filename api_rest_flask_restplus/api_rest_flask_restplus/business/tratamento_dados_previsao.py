import numpy as np
from tensorflow.keras.models import load_model


def tratamento_dados(data):
    print(f'Valores de entrada: {data}')
    data = np.array([np.asarray(data, dtype=float)])  # Converte para o tipo array
    return data


def previsao(data):
    predictor = load_model('./static/model/modelo1.h5')
    predictions = predictor.predict(data)  # Realiza as previsões
    print(f'Previsões de Probabilidades: {predictions}')
    return predictions


def tratamento_previsao(predictions):
    # Como são retornadas probabilidades, extraímos a maior, que indica a categoria da planta
    tipo = np.where(predictions == np.amax(predictions, axis=1))[1][0]
    print(f'Previsão: {tipo}')

    if tipo == 0:
        pred_planta = 'Setosa'
    elif tipo == 1:
        pred_planta = 'Versicolor'
    else:
        pred_planta = 'Virginica'

    return pred_planta
