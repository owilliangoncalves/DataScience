from pcaV2 import *
import pandas as pd

#Importando o dataset
df = pd.read_csv("PCA/dataset.csv", index_col=0)
# print(df.shape) repare que o df possui mais variáveis do que exemplos, ou seja, mais colunas do que linha e isso é um problema para um bom modelo de machine learning

#Convertendo os dados para um array numpy
matriz = df.to_numpy()
#Executando o PCA V2
pcaOut, eingenvalV2, principalComponent, covMatriz = pcaV2(matriz)

totalVariance = sum(eingenvalV2) #calculando a variância total
varianceExplained = [(i/totalVariance) for i in eingenvalV2] #calculando a variância explicada para cada elemento

cumulativeVarianceExplained = np.cumsum(varianceExplained) #calculando a variância explicada acumulada

print(f"variância explicada acumulada {cumulativeVarianceExplained}")
