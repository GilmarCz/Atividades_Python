import pandas as pd
url_produtos ="produtos_mercado.csv"
df_produtos = pd.read_csv(url_produtos)

# 18. Crie uma nova coluna chamada Valor_Total_Estoque que seja o resultado da multiplicação de
# Preco_Kg por Estoque_Kg.
df_produtos['Valor_Total_Estoque'] = df_produtos['Preco_Kg'] * df_produtos['Estoque_Kg']



# 19. Suponha que todos os produtos da categoria 'Fruta' terão um aumento de 5% no preço. Atualize a
# coluna Preco_Kg para refletir esse aumento APENAS para as frutas. (Cuidado para não alterar os
# preços dos legumes e verduras).
df_produtos.loc[df_produtos['Categoria'] == 'Fruta', 'Preco_Kg'] *= 1.05


# 20. Crie uma coluna chamada Status_Estoque que contenha:
# ○ 'Alto' se Estoque_Kg > 150
# ○ 'Médio' se Estoque_Kg > 50 e <= 150
# ○ 'Baixo' se Estoque_Kg <= 50

condicoes = [
    df_produtos['Estoque_Kg'] > 150,
    (df_produtos['Estoque_Kg'] > 50) & (df_produtos['Estoque_Kg'] <= 150),
    df_produtos['Estoque_Kg'] <= 50
]

# Definir os valores correspondentes às condições
valores = ['Alto', 'Médio', 'Baixo']

# Criar a nova coluna
df_produtos['Status_Estoque'] = np.select(condicoes, valores)
condicoes = [
    df_produtos['Estoque_Kg'] > 150,
    (df_produtos['Estoque_Kg'] > 50) & (df_produtos['Estoque_Kg'] <= 150),
    df_produtos['Estoque_Kg'] <= 50
]

# Definir os valores correspondentes às condições
valores = ['Alto', 'Médio', 'Baixo']

# Criar a nova coluna
df_produtos['Status_Estoque'] = np.select(condicoes, valores)

print(df_produtos.head(10))

#verificar resolução e prints