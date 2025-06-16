import pandas as pd
import numpy as np

url_produtos = "produtos_mercado.csv"
df_produtos = pd.read_csv(url_produtos)

# 18. Crie uma nova coluna chamada Valor_Total_Estoque
df_produtos['Valor_Total_Estoque'] = df_produtos['Preco_Kg'] * df_produtos['Estoque_Kg']

# 19. Aumento de 5% no preço das frutas
df_produtos.loc[df_produtos['Categoria'] == 'Fruta', 'Preco_Kg'] *= 1.05

# 20. Crie a coluna Status_Estoque
condicoes = [
    df_produtos['Estoque_Kg'] > 150,
    (df_produtos['Estoque_Kg'] > 50) & (df_produtos['Estoque_Kg'] <= 150),
    df_produtos['Estoque_Kg'] <= 50
]

valores = ['Alto', 'Médio', 'Baixo']

df_produtos['Status_Estoque'] = np.select(condicoes, valores, default='Indefinido')

print(df_produtos.head(10))
