import pandas as pd
url_produtos ="produtos_mercado.csv"
df_produtos = pd.read_csv(url_produtos)

#7 Selecione e exiba apenas a coluna 'Produto'
exiba_produto = df_produtos['Produto']
print("Exibir a coluna Produto")
print(exiba_produto.head())
print("\n" + "="*60 + "\n")

#8 Selecione e exiba as colunas 'Produto', 'Categoria' e 'Preco_Kg'
selecao_produto = df_produtos[['Produto','Categoria','Preco_Kg']]
print("Exibir a seleção: Produto | Categoria | Preço_Kg")
print(selecao_produto.head())
print("\n" + "="*60 + "\n")

#9 Exiba os dados do produto com ID_Produto igual a 110 (Limão Tahiti).
id_produtos = df_produtos[df_produtos['ID_Produto'] >= 111]
print("ID's superiores a #110")
print(id_produtos[['Produto']].head())
print("\n" + "="*60 + "\n")

#10 Quais são os produtos da categoria 'Verdura'?
verduras = df_produtos[df_produtos['Categoria'] == 'Verdura']
print(f"\nProdutos da categoria 'Verdura' ")
print(verduras.head())
print("\n" + "="*60 + "\n")

#11 Quais frutas têm um Preco_Kg superior a R$ 10,00?
df_produtos['Preco_Kg'] = pd.to_numeric(df_produtos['Preco_Kg'],errors='coerce')
frutas = df_produtos[df_produtos['Categoria'] == 'Fruta']
frutas_caras = frutas[frutas['Preco_Kg'] >= 10.00]
print("\n#11 Frutas com Preco_Kg > R$10,00:")
print(frutas_caras[['Produto', 'Preco_Kg']].head())
print("\n" + "="*60 + "\n")

#12 Quais produtos foram repostos no dia '2024-06-01'?
foram_repostos = df_produtos[df_produtos['Data_Ultima_Reposicao'] == '2024-06-01']
print(f"\nQuais produtos foram repostos no dia '2024-06-01'?")
print(foram_repostos[['Produto','Data_Ultima_Reposicao']].head())
print("\n" + "="*60 + "\n")

#13 Quais produtos são fornecidos pela 'Fazenda Sol Nascente' E são da categoria 'Fruta'?
frutas_fazenda = df_produtos[df_produtos['Categoria'] == 'Fruta']
print(f"\nFrutas da Fazenda Sol Nascente:")
print(frutas_fazenda['Produto'].head())
print("\n" + "="*60 + "\n")

#14 Selecione os produtos que são 'Fruta' OU têm Estoque_Kg maior que 150 Kg. 
df_produtos['Estoque_Kg'] = pd.to_numeric(df_produtos['Estoque_Kg'],errors='coerce')
filtro = (df_produtos['Categoria'] == 'Fruta') | (df_produtos['Estoque_Kg'] > 150)
kilo = df_produtos[filtro]
print(f"\nProdutos que são 'Fruta' OU têm Estoque_Kg maior que 150 Kg:")
print(kilo[['Produto', 'Categoria', 'Estoque_Kg']])
print("\n" + "="*60 + "\n")