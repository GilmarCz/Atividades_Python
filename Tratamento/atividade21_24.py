import pandas as pd
url_produtos ="produtos_mercado.csv"
df_produtos = pd.read_csv(url_produtos)

# 21. Verifique quantas valores ausentes (NaN) existem em cada coluna do DataFrame.
print("Valores ausentes por coluna:")
print(df_produtos.isnull().sum())


# 22. O 'Morango' está com Preco_Kg ausente. Preencha esse valor ausente com a média de preço de
# todos os outros produtos da categoria 'Fruta'.
# Calcular a média dos preços das frutas, ignorando valores nulos
media_frutas = df_produtos.loc[
    (df_produtos['Categoria'] == 'Fruta') & (df_produtos['Preco_Kg'].notnull()),
    'Preco_Kg'
].mean()

# Preencher o preço do Morango
df_produtos.loc[df_produtos['Produto'] == 'Morango', 'Preco_Kg'] = media_frutas


# 23. O 'Kiwi' está com Estoque_Kg ausente. Preencha esse valor com 0 (zero).
df_produtos.loc[df_produtos['Produto'] == 'Kiwi', 'Estoque_Kg'] = 0


# 24. Após os preenchimentos, verifique novamente se ainda existem valores ausentes.
print("\nVerificação após preenchimentos:")
print(df_produtos.isnull().sum())


