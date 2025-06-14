import pandas as pd
url_produtos ="produtos_mercado.csv"
df_produtos = pd.read_csv(url_produtos)

# 25. Qual é o preço médio por Categoria de produto?
preco_medio_categoria = df_produtos.groupby('Categoria')['Preco_Kg'].mean()
print("\nPreço médio por Categoria:")
print(preco_medio_categoria)


# 26. Qual é o estoque total (soma de Estoque_Kg) para cada Fornecedor?
estoque_total_fornecedor = df_produtos.groupby('Fornecedor')['Estoque_Kg'].sum()
print("\nEstoque total por Fornecedor:")
print(estoque_total_fornecedor)


# 27. Para cada Categoria, qual foi o produto com maior Vendas_Ultima_Semana_Kg?
produto_mais_vendido = df_produtos.loc[
    df_produtos.groupby('Categoria')['Vendas_Ultima_Semana_Kg'].idxmax(),
    ['Categoria', 'Produto', 'Vendas_Ultima_Semana_Kg']
]

print("\nProduto com maior venda na última semana por Categoria:")
print(produto_mais_vendido)


# 28. Qual o número de produtos distintos fornecidos por cada Fornecedor?
produtos_por_fornecedor = df_produtos.groupby('Fornecedor')['Produto'].nunique()
print("\nNúmero de produtos distintos por Fornecedor:")
print(produtos_por_fornecedor)


# 29. Calcule a soma das Vendas_Ultima_Semana_Kg e o Valor_Total_Estoque médio para cada Categoria.
resumo_categoria = df_produtos.groupby('Categoria').agg(
    Soma_Vendas_Ultima_Semana_Kg=('Vendas_Ultima_Semana_Kg', 'sum'),
    Media_Valor_Total_Estoque=('Valor_Total_Estoque', 'mean')
)

print("\nSoma das vendas e valor médio do estoque por Categoria:")
print(resumo_categoria)
