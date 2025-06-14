#4 Exiba as 7 primeiras linhas do DataFrame.
#5 Exiba as 3 últimas linhas do DataFrame.
#6 Obtenha um resumo estatístico das colunas numéricas (como preço e estoque).

import pandas as pd
url_produtos ="produtos_mercado.csv"
df_produtos = pd.read_csv(url_produtos)

print("Primeiras 5 linhas do DataFrame")
print(df_produtos.head())
print("\n" + "="*60 + "\n")
print(f"\nUltimas 3 linhas do DataFrame")
print(df_produtos.tail(3))
print("\n" + "="*60 + "\n")
print("6. Resumo estatístico das colunas numéricas:")
print(df_produtos.describe())
print("\n" + "="*60 + "\n")