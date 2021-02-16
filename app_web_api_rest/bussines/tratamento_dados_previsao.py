import numpy as np


def tratamento_dados(data):
    print(f'Valores de entrada: {data}')
    data = np.array([np.asarray(data, dtype=float)])  # Converte para o tipo array
    return data


def previsao(data, app):
    predictions = app.predictor.predict(data)  # Realiza as previsões
    print(f'Previsoes de Probabilidades: {predictions}')
    return predictions


def tratamento_previsao(predictions):
    # Como são retornadas probabilidades, extraímos a maior, que indica a categoria da planta
    tipo = np.where(predictions == np.amax(predictions, axis=1))[1][0]
    print(f'Previsao: {tipo}')

    if tipo == 0:
        pred_planta = 'Setosa'
    elif tipo == 1:
        pred_planta = 'Versicolor'
    else:
        pred_planta = 'Virginica'

    return pred_planta
