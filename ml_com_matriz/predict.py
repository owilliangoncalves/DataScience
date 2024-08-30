import numpy as np
import ast
from ml_com_matriz import NeuralNetwork

taxa_aprendizado = 0.01
num_iteracoes = 1000
mymodel = NeuralNetwork(taxa_aprendizado, num_iteracoes)

"""
Dados de entrada, é aqui que vamos determinar os valores de X la do arquivo ml_com_matriz.py. Aqui usarei dados fictícios, fique a vontade para testar com outros dados.
No exemplo os dados representam compras em um cartão de crédito, temos 2 atributos (variáveis) e 8 registros (linhas)
"""
#Abrindo arquivo txt em que possui os dados de entrada que vou utilizar para o treinamento do modelo
with open ('data_train.txt', 'r') as dados:
  dados = dados.read()

#captando e transformando os dados em um np.ndarray
dadosTeste = ast.literal_eval(dados)
dadosEntrada = np.array(dadosTeste)

"""
Dados de saída, representam por exemplo se transação foi ou não suspeita.
Aqui eu estou fazendo o input direto dos dados, mas é claro que eles poderiam vir de um outro arquivo. 
"""
#Classe 0 não é transação suspeita. Classe 1 é transação suspeita 
dadosSaida = np.array([0, 0, 1, 0, 1, 1])

#Treinando o modelo com dados aleatórios que eu coloquei no arquivo "data_train.txt"
XTreino = dadosEntrada
yTreino = dadosSaida

"""
Treinando o modelo
"""

mymodel.fit(XTreino, yTreino)

"""
Avaliação do modelo
"""
#Abrindo arquivo txt em que possui os dados de entrada que vou utilizar para o treinamento do modelo
with open ('data_test.txt', 'r') as dados_Teste:
  dados_Teste = dados_Teste.read()

#captando e transformando os dados em um np.ndarray
dados_Teste = ast.literal_eval(dados_Teste)
dadosEntradaTeste = np.array(dados_Teste)
xTeste = dados_Teste
yTeste = [0, 1]

# Previsão do modelo
previsaoNova = mymodel.predict(xTeste)

for i, previsao in enumerate(previsaoNova):
  entrada = dados_Teste[i]
  if previsao == 0:
    print(f"\nPara os atributos de entrada{entrada} a previsão foi {previsao}: Não é transação suspeita ")
  else:
    print(f"\nPara os atributos de entrada{entrada} a previsão foi {previsao}: É transação suspeita")