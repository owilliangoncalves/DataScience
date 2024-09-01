import sklearn 
from sklearn.decomposition import PCA
import pandas as pd
import numpy as np

#Carregando o data frame
df = pd.read_csv("PCA/dataset.csv", index_col=0)

#aplicando PCA
pca = PCA(n_components = 10)
X_PCA = pca.fit_transform(df)

varianceExplained = pca.explained_variance_ #variância explicada por cada componente

varianceExplainedRatio = pca.explained_variance_ratio_ #variância explicada por cada componente

cumulativeVarianceExplained = np.cumsum(varianceExplainedRatio)


print(f"variância explicada acumulada {cumulativeVarianceExplained}")

