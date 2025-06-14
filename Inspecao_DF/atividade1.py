# Quantas linhas e colunas tem o nosso DataFrame?
import pandas as pd
url_produtos ="produtos_mercado.csv"
df_produtos = pd.read_csv(url_produtos)
print("Dados carregados com sucesso!!!")
print(f"As linhas e colunas do nosso DataFrame: {df_produtos.shape}")
print("\n" + "="*60 + "\n")