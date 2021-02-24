import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
## criando series
densidades = pd.Series([0.53, 0.97, 0.86, 1.53, 1.9])

print("Imprimindo densidades adicionando indices antes:")
print(densidades)

## criando um array de indices
indexElementos = ["Li","Na","K","Rb","Cs"]

## adicionando indice
densidades.index = indexElementos

print("Imprimindo densidades adicionando indices depois:")
print(densidades)
novoIndex = ["a", "b", "c", "d", "e"]
densidades.index = novoIndex

print("Alterando os indices:")
print(densidades)