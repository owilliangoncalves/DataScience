#Import dos pacotes necessários
import numpy as np

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