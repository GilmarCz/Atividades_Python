import pandas as pd
import matplotlib.pyplot as plt

# Carregar o CSV
df_produtos = pd.read_csv("produtos_mercado.csv")

# Agrupar as vendas totais por produto
vendas_por_produto = df_produtos.groupby('Produto')['Vendas_Ultima_Semana_Kg'].sum().sort_values(ascending=False)

# Plotar o gráfico de barras
plt.figure(figsize=(12,6))
vendas_por_produto.plot(kind='bar', color='skyblue')

plt.title('Vendas Totais da Última Semana por Produto', fontsize=14)
plt.xlabel('Produto', fontsize=12)
plt.ylabel('Vendas (Kg)', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

plt.show()
