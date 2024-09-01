from pcaV1 import *
import pandas as pd

#Importando o dataset
df = pd.read_csv("PCA/dataset.csv", index_col=0)
# print(df.shape) repare que o df possui mais variáveis do que exemplos, ou seja, mais colunas do que linha e isso é um problema para um bom modelo de machine learning

#Convertendo os dados para um array numpy
matriz = df.to_numpy()
#Executando o PCA V1
pcaOut, eingenvalV1, principalComponent, covMatriz = pcaV1(matriz)

#Somando a variância explicada por 10 componentes
varianciaExplicadaV1 = (eingenvalV1[0]/sum(eingenvalV1)) + \
                       (eingenvalV1[1]/sum(eingenvalV1)) + \
                       (eingenvalV1[2]/sum(eingenvalV1)) + \
                       (eingenvalV1[3]/sum(eingenvalV1)) + \
                       (eingenvalV1[4]/sum(eingenvalV1)) + \
                       (eingenvalV1[5]/sum(eingenvalV1)) + \
                       (eingenvalV1[6]/sum(eingenvalV1)) + \
                       (eingenvalV1[7]/sum(eingenvalV1)) + \
                       (eingenvalV1[8]/sum(eingenvalV1)) + \
                       (eingenvalV1[9]/sum(eingenvalV1))


#Convertendo para percentual
percentualVarianciaExplicadaV1 = varianciaExplicadaV1*100

print("Total de variância dos dados explicada por 10 componentes principais: ", percentualVarianciaExplicadaV1)

#Calculando a variância total 
varianciaTotal = sum(eingenvalV1)

#Calculando a variância explicada por cada componente
varianciaExplicadaPorComponente= [ (i/varianciaTotal) for i in eingenvalV1]

#Calculando a variância explicada acumulada
varianciaExplicadaAcumulada = np.cumsum(varianciaExplicadaV1)

print(f"Cerca de {np.round(varianciaExplicadaAcumulada*100).real.squeeze()}% dos dados são explicados por 10 componentes")