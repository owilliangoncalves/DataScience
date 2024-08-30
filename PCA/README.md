# Algoritmo de PCA (Principal Components Analysis)

É uma técnica de redução de dimensionalidade onde o objetivo principal é transformar um conjunto de variáveis POSSIVELMENTE CORRELACIONADAS em um conjunto de valores de variáveis LINEARMENTE NÃO CORRELACIONADAS. Este processo é realizado mantendo-se o máximo possível da variabilidade presente no conjunto de dados.
Aqui você encontrara 3 versões do algoritmo PCA sendo a v1 a mais difícil (mais linhas de código) e v3 a versão com menos linhas de código, todas as versões usando o mesmo dataset.

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

1. Seus dados de entrada devem estar divididos em uma ou mais colunas de entrada (representado por X) e uma ou mais colunas de saída (representado por Y). Aplicamos o PCA em X. Se os seus dados tiverem a variável de saída Y, ela não entra no cálculo do PCA. Nesse caso você reduziria a dimensionalidade de X para então tentar prever Y. PCA trabalha no X.

2. Pegue a matriz de variáveis independentes X e para cada coluna, subtraia a média dessa coluna de cada entrada (Isso garante que cada coluna tenha uma média de zero).

3. Decida se deve ou não padronizar. Dadas as colunas de X os recursos com variação mais alta são mais importantes em relação aos recursos com variação menor ou a importância dos recursos é independente da variação?

4. Pegue a matriz Z, transponha e multiplique a matriz transposta por Z (Escrevendo isso matematicamente, teríamos ZᵀZ.) A matriz resultante é a matriz de covariância de Z.

5. Calcule os autovetores e seus autovalores correspondentes de Z. A composição automática de ZᵀZ é onde decompomos ZᵀZ em PDP⁻¹, onde P é a matriz de autovetores e D é a matriz diagonal com autovalores na diagonal e valores de zero em qualquer outro lugar. Os autovalores na diagonal de D serão associados à coluna correspondente em P. Ou seja, o primeiro elemento de D é λ₁ e o autovetor correspondente é a primeira coluna de P. Isso vale para todos os elementos em D e seus autovetores correspondentes em P. Sempre poderemos calcular o PDP⁻¹ dessa maneira.

6. Pegue os autovalores λ₁, λ₂,…, λn e classifique-os do maior para o menor. Ao fazer isso, classifique os autovetores em P. Por exemplo, se λ₂ é o maior autovalor, pegue a segunda coluna de P e coloque-a na posição da primeira coluna. Dependendo do pacote de computação, isso pode ser feito automaticamente. Chame essa matriz classificada de autovetores P* (As colunas de P* devem ser as mesmas que as de P, mas talvez em uma ordem diferente). Observe que esses autovetores são independentes um do outro.

7. Calcular Z* = ZP*. Essa nova matriz, Z*, é uma versão centralizada/padronizada de X, mas agora cada observação é uma combinação das variáveis originais, onde os pesos são determinados pelo autovetor. Como um bônus, porque nossos autovetores em P* são independentes um do outro, cada coluna de Z\* também é independente uma da outra!

8. Finalmente, precisamos determinar quantos componentes principais manter versus quantos deixar de fora. Existem três métodos comuns para determinar isso, discutidos abaixo:

- Método 1: Selecionamos arbitrariamente quantas dimensões queremos manter.

- Método 2: Calculamos a proporção de variação explicada para cada recurso, escolhemos um limite e adicionamos recursos até atingir esse limite (Por exemplo, se você deseja explicar 80% da variabilidade total possivelmente explicada pelo seu modelo, adicionamos recursos com a maior proporção de variação explicada até que a proporção de variação explicada atinja ou exceda 80%). **Este é o método ideal** para o caso que estamos trabalhando.

- Método 3: Este está intimamente relacionado ao método 2. Calculamos a proporção de variação explicada para cada recurso, classificamos os recursos por proporção de variação explicada e plotamos a proporção acumulada de variação explicada à medida que mantemos mais recursos. É possível escolher quantos recursos incluir, identificando o ponto em que a adição de um novo recurso tem uma queda significativa na variação explicada em relação ao recurso anterior e a escolha de recursos até esse ponto (Chamamos isso de método “encontre o cotovelo”, pois olhar para a “curva” ou “cotovelo” no gráfico determina onde ocorre a maior queda na proporção da variação explicada).

Como cada autovalor é aproximadamente a importância do seu autovetor correspondente, a proporção de variação explicada é a soma dos autovalores dos recursos que você manteve divididos pela soma dos autovalores de todos os recursos.

Os autovetores da matriz de covariância são as direções principais, enquanto os autovalores representam a magnitude dessas direções. Os autovalores são importantes para entender a quantidade de variação capturada por cada componente principal.

#### Variância e Variância Acumulada nos Componentes Principais:

## 🛠️ Construído com:

- [NumPy](https://numpy.org/pt/) - NumPy
- [Pandas](https://pandas.pydata.org/) - Pandas
- [Scikit-learn] (https://scikit-learn.org/stable/) - Scikit-learn
