#Import dos pacotes necessários
import numpy as np
import pandas as pd

#Importando o dataset
df = pd.read_csv("PCA/dataset.csv", index_col=0)
print(df.shape) #repare que o df possui mais variáveis do que exemplos, ou seja, mais colunas do que linha e isso é um problema para um bom modelo de machine learning

#Convertendo os dados para um array numpy
matriz = df.to_numpy()

#Função de implementação
def pcaV1(input):
  mean = np.mean(input, 0) #calculando a média de cada coluna

  normalisedInput = np.subtract(input, mean) #Subtraindo a média da matriz de entrada

  normalisedInputTranspose = np.transpose(normalisedInput) #Calculando a transposta da matriz normalizada

  samples = input.shape[0] #Numero de amostras

  covMatriz = (np.dot(normalisedInputTranspose, normalisedInput))/ (samples) #Calculando a matriz de covariância 

  value, vector = np.linalg.eig(np.array(covMatriz)) #Localizando autovalores e autovetores

  #Ordenando os valores
  index = value.argsort()[::-1]
  eigenValue = value[index]
  component = vector[:, index]

  pcaOutput = np.dot(normalisedInput, component) #Multiplicando a matriz de componente principal com a matriz de dados de entrada para obter o PCA

  return pcaOutput, eigenValue, component, covMatriz

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





