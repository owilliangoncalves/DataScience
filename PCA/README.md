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

## 🛠️ Construído com

- [NumPy](https://numpy.org/pt/) - NumPy
- [Pandas](https://pandas.pydata.org/) - Pandas
