#Import dos pacotes necessários
import numpy as np
import pandas as pd

#Importando o dataset
df = pd.read_csv("PCA/dataset.csv", index_col=0)
print(df.shape) #repare que o df possui mais variáveis do que exemplos, ou seja, mais colunas do que linha e isso é um problema para um bom modelo de machine learning

#Convertendo os dados para um array numpy
matriz = df.to_numpy()

def pcaV2 (input):
  