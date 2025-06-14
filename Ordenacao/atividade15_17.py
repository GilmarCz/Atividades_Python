import pandas as pd
url_produtos ="produtos_mercado.csv"
df_produtos = pd.read_csv(url_produtos)

# 15. Liste todos os produtos ordenados alfabeticamente pelo nome.
df_ordem_alfa = df_produtos.sort_values(by='Produto')
print(f"\nOrdenando por ordem alfabetica: ")
print(df_ordem_alfa['Produto'].head())
print("\n" + "="*60 + "\n")

# 16. Quais são os 5 produtos mais caros (maior Preco_Kg)?
df_mais_caros = df_produtos.sort_values(by='Preco_Kg', ascending=False)
print(f"\nTop 5 maior Preco_Kg: ")
print(df_mais_caros[['Produto','Preco_Kg']].head())
print("\n" + "="*60 + "\n")

# 17. Liste os produtos ordenados pela Data_Ultima_Reposicao (do mais recente para o mais antigo) e,para datas iguais, pelo nome do produto em ordem alfabética.
df_data_reposicao = df_produtos.sort_values(
    by=['Data_Ultima_Reposicao', 'Produto'],
    ascending=[False, True]
)

print(f"\nProdutos ordenados pela Data_Ultima_Reposicao (mais recente) e Produto (ordem alfabética):")
print(df_data_reposicao[['Produto', 'Data_Ultima_Reposicao']].head(200))
print("\n" + "="*60 + "\n")