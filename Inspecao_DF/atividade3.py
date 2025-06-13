#3  Quais são os tipos de dados de cada coluna? A coluna Data_Ultima_Reposicao está no formato correto de data?

import pandas as pd
url_produtos ="produtos_mercado.csv"
df_produtos = pd.read_csv(url_produtos)
print("Tipos de dados das colunas:")
print(df_produtos.info)
print(df_produtos.dtypes)
print("\n" + "="*60 + "\n")
print("\nVerificando o formato da coluna 'Data_Ultima_Reposicao':")
print(f"Tipo original: {df_produtos['Data_Ultima_Reposicao'].dtype}")
print(f"Exemplos de valores: {df_produtos['Data_Ultima_Reposicao'].head().tolist()}")
print("A data NÃO está no formato dd/mm/aaaa")
print("\n" + "="*60 + "\n")