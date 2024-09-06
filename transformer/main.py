from imports import *
from config import *
from functools import partial
import pandas as pd


def main ():
  """
  Função principal que inicializa as demais funções.
  """
  def init():
    imports()
    data()
    config()
  init()

  # Converte data para períodos de datas
  def convertPandasPeriod(date,freq):
    return pd.Period(date, freq)

  #Inicio de batch de dados
  def start(batch, freq):
    """"
    O batch de dados deve ser feito pois modelos de deep learning necessitam que os dados sejam entregues em "pacotes" devido recurso de memória
    """
    batch["start"] = [convertPandasPeriod(date, freq) for date in batch["start"]]
    return batch

  treino.set_transform(partial(start, freq = freq))
  teste.set_transform(partial(start, freq = freq))


if __name__ == "__main__":
  main()