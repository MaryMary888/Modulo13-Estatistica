import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
df= pd.read_csv("MODULO7_PROJETOFINAL_BASE_SUPERMERCADO.csv")

print(df.head(30))
# Utiliza-se 'print(df['Categoria'].dtype)' para descobrir tipo de dado das colunas

# Preenchendo coluna Preco_Normal que estão com valores vazios
# Substituindo valor 0 de Preco_Normal para o valor de Preco_Anterior
df['Preco_Normal'] = df.apply(lambda x: x['Preco_Anterior'] if x['Preco_Anterior'] != 0 else x['Preco_Normal'], axis=1)

# Substituindo Preco_Normal = 0 pela média do mesmo por categoria
media_preco_vazio = df.groupby('Categoria')['Preco_Normal'].mean().to_dict()  # Utiliza-se 'to_dict()' para tornar os dados legíveis para lambda na linha abaixo
df['Preco_Normal'] = df.apply(lambda x: media_preco_vazio[x['Categoria']] if x['Preco_Desconto'] == 0 and x['Preco_Normal'] ==0 else x['Preco_Normal'], axis=1)
df['Preco_Normal'] = df['Preco_Normal'].astype(int)

# Substituindo Preco_Normal = 0 pela soma da média de Desconto (gerada por categoria) e do Preco_Desconto
media_desc_vazio = df.groupby('Categoria')['Desconto'].mean().to_dict()
df['Desconto'] = df.apply(lambda x: media_desc_vazio[x['Categoria']] if x['Preco_Desconto'] != 0 and x['Preco_Normal'] == 0 else x['Desconto'], axis=1)
df['Desconto'] = df['Desconto'].astype(int)
df['Preco_Normal'] = df.apply(lambda x: x['Desconto'] + x['Preco_Desconto'] if x['Preco_Normal'] == 0 else x['Preco_Normal'], axis=1)
# print(df.iloc[813:].to_string()) - Verificam-se as linhas que apresentavam Preco_Normal = 0

# Trazendo a média e a mediana de Preco_Normal por categoria de produto.
#Trazendo Média
media_preco_categoria = df.groupby('Categoria')['Preco_Normal'].mean().reset_index().sort_values(by= 'Categoria', ascending=False)
print('\n\nMédias dos preços por categoria de produto:\n', media_preco_categoria)

#Trazendo Mediana
mediana_preco_categoria = df.groupby('Categoria')['Preco_Normal'].median().reset_index().sort_values(by='Categoria',ascending=False)
print('\nMedianas dos preços por categoria de produto:\n', mediana_preco_categoria)

# Trazendo o desvio padrão por Categoria de produto.
desvio_padrao_por_categoria = df.groupby('Categoria')['Preco_Normal'].std().reset_index().sort_values(by='Categoria',ascending=False)
print('\nDesvio Padrão por Categoria de Produto\n', desvio_padrao_por_categoria)

# Boxplot da distribuição do Preco_Normal da categoria com maior desvio padrão.
# Separando por categoria específica
df_categ = df.loc[df['Categoria'] == 'lacteos']

# Plot do Boxplot
plt.figure(figsize=(8,6))
plt.boxplot(df_categ['Preco_Normal'])
plt.title('Distribuição dos Preços - Categoria: Lacteos')
plt.ylabel('Preço Normal do Produto')
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()

# Gráfico de barras da média de descontos por categoria.
# Média de descontos
df_media_desc = df.groupby('Categoria')['Desconto'].mean().reset_index().sort_values(by= 'Desconto', ascending=False)

fig= px.bar(df_media_desc, x = 'Categoria', y = 'Desconto', orientation = 'v', title = 'Média de Descontos por Categoria',
        labels={'Categoria':'Tipo de Produto', 'Desconto':'Média de Desconto'})
fig.show()

# Gráfico interativo agrupando os dados por categoria, marca e trazendo média de descontos.
df_media_desc_categ = df.groupby(['Categoria','Marca'])['Desconto'].mean().reset_index().round(2)

fig = px.sunburst(df_media_desc_categ, path=['Categoria', 'Desconto', 'Marca'], values=None, color='Categoria',
                  title='Relação entre Marcas, Categoria de Produto e Média de Desconto')
fig.show()
