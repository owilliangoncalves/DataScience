# Algoritmo de PCA (Principal Components Analysis)

É uma técnica de redução de dimensionalidade onde o objetivo principal é transformar um conjunto de variáveis POSSIVELMENTE CORRELACIONADAS em um conjunto de valores de variáveis LINEARMENTE NÃO CORRELACIONADAS. Este processo é realizado mantendo-se o máximo possível da variabilidade presente no conjunto de dados.

Reveja o que são autovalores e autovetores [aqui](autovalores_e_autovetores.md).

Reveja as propriedades de autovalores e autovetores [aqui](propiedades_autovalores_e_autovetores.md).

## O funcionamento do algoritmo de PCA pode ser descrito da seguinte maneira:

- **Normalização dos dados:** Inicialmente os dados são normalmente padronizados, especialmente se as variáveis tem unidades de medidas diferentes.

- **Cálculo da matriz de covariância:** A matriz de covariância é calculada para entender como as variáveis do conjunto de dados estão variando em relação uma às outras.

- **Determinação de autovalores e autovetores:** São calculados a partir da MATRIZ DE COVARIÂNCIA. Os AUTOVALORES indicam a quantidade de variância que pode ser atribuída a cada AUTOVETOR.

- **Seleção de componentes principais:** São selecionados com base na quantidade de variância que eles representam. Geralmente são escolhidos os componentes que somam a maior parte da variância total e isso permite um representação simplificada do conjunto de dados.

- **Transformação dos dados:** Os dados originais são transformados em um novo conjunto de dados com base nos componentes principais selecionados.

## Como o PCA funciona?

O PCA baseia-se nos conceitos de Matriz de Variância e Covariância.

- **Variância:** É uma medida de variabilidade dos dados. Matematicamente é o desvio quadrático médio da pontuação média.
  > variância populacional

$$\sigma^2 = \frac{\sum_{i=1}^{n} (x_i - \mu)^2}{n}$$

Ambas as formas são equivalentes e corretas!

onde:

- $\sigma^2$ é a variância
- $n$ é o número de observações
- $x_i$ é a i-ésima observação
- $\mu$ é a média da população

---

- **Covariância:** É uma medida da extensão em que os elementos correspondentes de dois conjuntos de dados **ordenados** se movem na mesma direção, ou seja, como dois conjuntos de dados estão relacionados

> covariância populacional

Aqui está a fórmula da covariância:

$$\text{Cov}(X, Y) = \frac{\sum_{i=1}^{n} (x_i - \mu_X)(y_i - \mu_Y)}{n}$$

Onde:

- $\text{Cov}(X, Y)$ é a covariância entre as variáveis $X$ e $Y$
- $n$ é o número de observações
- $x_i$ e $y_i$ são as i-ésimas observações das variáveis $X$ e $Y$, respectivamente
- $\mu_X$ e $\mu_Y$ são as médias das variáveis $X$ e $Y$, respectivamente

---

## Adendo

No algoritmo PCA precisamos calcular uma matriz que resume como todas as variáveis se relacionam. Depois, dividimos essa matriz em dois componentes principais: **direção** e **magnitude**.

---

## Descrição do algoritmo PCA

1. Seus dados devem estar divididos em uma ou mais colunas de entrada (representado por X) e uma ou mais colunas de saída (representada por Y). Aplicamos o PCA em X, se os dados tiverem uma variável de saída em Y ela não entra no calculo.

2. Use a matriz de variáveis independentes X e para cada coluna subtraia a média dessa coluna de cada entrada.

3. Decida se deve ou não padronizar. Dadas as colunas de X, os recursos com variação mais altas são os mais importantes em relação ao de menor variação ou a importância dos recursos é independente da variação?

## 🛠️ Construído com

- [NumPy](https://numpy.org/pt/) - NumPy
- [Pandas](https://pandas.pydata.org/) - Pandas
