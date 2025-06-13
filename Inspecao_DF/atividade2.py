#2 Quais são os nomes de todas as colunas?

import pandas as pd
url_produtos ="produtos_mercado.csv"
df_produtos = pd.read_csv(url_produtos)
print("Dados carregados com sucesso!!!")
print(f"Colunas disponíveis: {list(df_produtos.columns)}")
print("\n" + "="*60 + "\n")