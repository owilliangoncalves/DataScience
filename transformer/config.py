from data import *

from transformers import TimeSeriesTransformerConfig,TimeSeriesTransformerForPrediction
from gluonts.time_feature import get_lags_for_frequency
from gluonts.time_feature import time_features_from_frequency_str

prediction_length = 24
freq = "1M"
dataset, treino, teste = data()

def config ():
    # TimeSeries Transformer Config
    timeSeries = TimeSeriesTransformerConfig(

    # Comprimento de previsão
        prediction_length = prediction_length,

    # Comprimento do contexto
        context_length = prediction_length * 2,

    # Lags sequence
    # "lag" é um atraso temporal. Por exemplo, em uma série temporal mensal, o "lag" de um mês refere-se aos dados do mês anterior.
        lags_sequence = get_lags_for_frequency(freq),

    # Adicionaremos 2 características de tempo ("mês do ano" e "idade da série"):
        num_time_features = len(time_features_from_frequency_str(freq)) + 1,

    # Temos um único recurso categórico estático, ou seja, o ID da série temporal
        num_static_categorical_features = 1,

    # Temos 366 valores possíveis
        cardinality = [len(treino)],

    # O modelo receberá uma embedding de tamanho 2 para cada um dos 366 valores possíveis:
        embedding_dimension = [2],

    # Parâmetros da rede neural do Transformer
        encoder_layers = 4,
        decoder_layers = 4,
        d_model = 32,
    )
    return timeSeries

