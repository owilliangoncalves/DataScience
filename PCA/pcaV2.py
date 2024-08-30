#Import dos pacotes necessários
import numpy as np

def pcaV2 (input):
  mean = np.mean(input, axis=0) #Calculando a média de cada coluna
  normalisedInput = input - mean #Subtraindo a média da matriz de entrada 
  covMatriz = np.cov(normalisedInput, rowvar=False) #Calculando a matriz de covariância
  eigenvalues, eigenvectors, = np.linalg.eigh(covMatriz) #Localizando autovalores e autovetores utilizando uma função mais adequada (eigh) para matrizes simétricas

  #Ordenando os AUTOVETORES de acordo com os AUTOVALORES em ordem decrescente
  sortedIndices = np.argsort(eigenvalues) [::-1]
  sortedEigenValues = eigenvalues[sortedIndices]
  sortedEingenVectors = eigenvectors[:, sortedIndices]

  pcaOutput = np.dot(normalisedInput, sortedEingenVectors)

  return pcaOutput, sortedEigenValues, sortedEingenVectors, covMatriz