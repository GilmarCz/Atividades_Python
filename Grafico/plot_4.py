import pandas as pd
import matplotlib.pyplot as plt

# Carregar o CSV
df_produtos = pd.read_csv("produtos_mercado.csv")

# Agrupar as vendas totais por produto
vendas_por_produto = df_produtos.groupby('Produto')['Vendas_Ultima_Semana_Kg'].sum().sort_values(ascending=False)

# Criar a figura com 4 subplots (2 linhas, 2 colunas)
fig, axs = plt.subplots(2, 2, figsize=(14, 10))

# 🎯 Gráfico de Barras Verticais
axs[0, 0].bar(vendas_por_produto.index, vendas_por_produto.values, color='skyblue')
axs[0, 0].set_title('Vendas - Barras Verticais')
axs[0, 0].set_xlabel('Produto')
axs[0, 0].set_ylabel('Vendas (Kg)')
axs[0, 0].tick_params(axis='x', rotation=45)

# 🎯 Gráfico de Barras Horizontais
axs[0, 1].barh(vendas_por_produto.index, vendas_por_produto.values, color='orange')
axs[0, 1].set_title('Vendas - Barras Horizontais')
axs[0, 1].set_xlabel('Vendas (Kg)')
axs[0, 1].set_ylabel('Produto')

# 🎯 Gráfico de Linha
axs[1, 0].plot(vendas_por_produto.index, vendas_por_produto.values, marker='o', linestyle='-', color='green')
axs[1, 0].set_title('Vendas - Linha')
axs[1, 0].set_xlabel('Produto')
axs[1, 0].set_ylabel('Vendas (Kg)')
axs[1, 0].tick_params(axis='x', rotation=45)
axs[1, 0].grid(True)

# 🎯 Gráfico de Pizza
axs[1, 1].pie(
    vendas_por_produto.values, 
    labels=vendas_por_produto.index, 
    autopct='%1.1f%%', 
    startangle=90, 
    colors=plt.cm.tab20.colors
)
axs[1, 1].set_title('Vendas - Pizza')

# Ajustar espaçamentos
plt.tight_layout()

# Exibir tudo
plt.show()
