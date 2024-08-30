import numpy as np
#Classe para definição do algoritmo
class NeuralNetwork:
  #método construtor
  """
  Método de função de ativação sigmoide para gerar a previsão no formato que possa ser interpretado como probabilidade (valores entre 0 e 1)
  Args:
    param taxa_aprendizado: (float) Taxa de Aprendizado do modelo.
    param num_iteracoes: (int) Numero de iteracoes que o modelo ira executar.
  """
  def __init__(self, taxa_aprendizado, num_iteracoes):
    self.taxa_aprendizado = taxa_aprendizado
    self.num_iteracoes = num_iteracoes
    self.pesos = None
    self.bias = None
  def act_sigmoid(self, pred):
    sig = 1 / (1 + np.exp(-pred))
    return sig
  
  #Método de treinamento. X representando dados de entrada e y dados de saída
  def fit(self, X, y):
    #Extrai do shape o numero de linhas e colunas
    num_registros, num_atributos = X.shape
    #Matriz de pesos com 0 no mesmo shape de "num_atributos""
    self.pesos = np.zeros(num_atributos)
    #Escalar BIAS sendo 0
    self.bias = 0

    print("\n Treinamento iniciado")

    #Loop de treinamento pelo número de iterações
    for i in range(self.num_iteracoes):
      print("Treino do modelo na iteração", i)
      """
      Primeira parte do método é o foward pass
      """
      #Faz a previsão usando o valor de X (dados de entrada), pesos e BIAS
      previsao = np.dot(X, self.pesos) + self.bias
      print("Previsão antes da função de ativação", previsao)

      #Converte a previsão inicial para um valor que possa ser interpretado como probabilidade pela função sigmoide
      previsao_final = self.act_sigmoid(previsao)
      print("Previsão após a função Sigmoide", previsao_final)

      #Calcula erro do modelo
      erro = previsao_final - y
      print("Erro do modelo", erro)
      """
      Segunda parte do modelo é o backward pass (backpropagation)
      """
      #Calcula os gradientes (derivadas da matriz de peso e BIAS)
      dw = (1/ num_registros) * np.dot(X.T, erro)
      db = (1/num_registros) * np.sum (previsao_final - y)

      # Atualiza os pesos e bias usando o valor das derivadas e a taxa de aprendizado
      self.pesos -= self.taxa_aprendizado * dw
      print("Valores de peso", self.pesos)
      self.bias -= self.taxa_aprendizado * db
      print("Valores de BIAS", self.bias)

    print("Treinamento concluído")

  def predict (self, X):
    
    #faz as previsões com os novos dados de entrada com os valores de pesos e BIAS
    previsao = np.dot(X, self.pesos) + self.bias
    print("Previsão antes de passar pela função de ativação", previsao)

    previsao_final = self.act_sigmoid(previsao)
    print("Previsão depois de passar pela função de ativação", previsao_final)

    #Aplica o cut-off e converte probabilidades para classes binárias (0 ou 1)
    prevista = [1 if i > 0.5 else 0 for i in previsao_final]

    return prevista