# Projeto de Análise estatística
## Sobre o Projeto
- O projeto a seguir traz uma análise sobre uma base de dados 
de um Supermercado contendo informações sobre os produtos 
disponíveis no mesmo. Com essa base, analisaremos preços e 
descontos de cada categoria de produtos que o mercado oferece,
a fim de entender o funcionamento da distribuição de preços 
entre as marcas e se existem muitos outliers entre esses 
produtos.

## Código em Geral
### Alterações dos dados 
- O dataframe inicialmente possuia alguns dos dados de preços 
com valor 0 e foram identificados 3 cenários. Por não ser um 
valor plausível para a análise de preços, foram realizadas 
algumas alterações nesses dados zerados:
  1. O primeiro cenário apresentavam os dados de Preco_Desconto, 
  Preco_Anterior e Desconto com valores, porém Preco_Normal 
  estava atribuído 0. Para contornar esta situação, o 
  Preco_Normal zerado foi substituído pelo valor de 
  Preço_Anterior, corrigindo este cenário de maneira precisa.
  2. Para o segundo cenário, todos os campos citados acima 
  estavam com valor 0 atribuídos a eles. Como solução, foi 
  implementada uma inserção de preços baseado nas médias de 
  preço de cada categoria e atualizadas no campo Preco_Normal.
  3. Por fim, no último cenário, dos quatro mesmos campos 
  citados anteriormente, apenas o valor de Preco_Desconto 
  apresenta-se preenchido com valores, indicando que havia 
  algum desconto atribuído àquele produto. Para solucionar este 
  problema, o campo Desconto zerado foi preenchido com a média 
  de descontos por Categoria. Em seguida, a soma dos dois campos 
  resultou no valor original do produto, e assim foi inserido 
  seu total no Preco_Normal também zerado.

### Cálculos e ferramentas utilizadas para a análise
- Os cálculos realizados na análise são: Média, Mediana, Desvio 
Padrão e Construção de gráficos (Boxplot, Barras e Sunburst).

### Análise dos Cálculos
#### Média e Mediana
- Inicialmente, foram feitos os cálculos de média e mediana para 
extrair os preços de seu respectivo agrupamento de categoria de 
produto.
- Podemos observar em seu output que, Frutas e principalmente os 
Lácteos possuem médias muito acima das medianas apresentadas, 
indicando a presença de outliers nos preços, que aumentam 
significativamente os valores da média dessas categorias. 
- Já as demais categorias possuem variações não muito distantes, 
acima dos valores das medianas. Isso indica que não há valores 
discrepantes e pouca oscilação entre os preços dos produtos de 
mesma categoria.

#### Desvio Padrão em relação à Média e Mediana
- O cálculo do desvio padrão foi usado para podermos verificar 
o quão dispersos os valores estão em relação à média dos preços 
de cada categoria.
- Segundo os valores, podemos compreender que apesar de haver 
um desvio enorme na categoria Lácteos, a categoria Frutas não 
apresenta desvio exacerbado em comparação à primeira categoria.
- Isso pode indicar que, a categoria de Lácteos, além de possuir 
outliers já indicados na média e mediana, insinua também que 
estes tem preços extremamente acima dos demais acerca da média, 
afetando o resultado dela e do próprio desvio, enquanto a 
categoria Frutas possui uma quantidade não tão alta de preços 
dispersos.
- É importante notar também, que existe um desvio padrão elevado 
das categorias Beleza/cuidado pessoal e Verduras. Isso pode 
ocorrer devido à distribuição mais uniforme de preços em torno 
da média e mediana, indicando que não há outliers e que existe 
apenas uma faixa mais ampla nos preços em ambas as categorias.

### Análise dos gráficos
#### Boxplot da distribuição de preços para a categoria de Lácteos
- A categoria de Lácteos foi selecionada para a análise do 
Boxplot, pois a mesma apresenta um maior desvio padrão.
- A distribuição dos dados está mais concentrada aproximadamente 
entre os preços 560 e 2640 Pesos Chilenos. Entre estes valores, 
a mediana do preço desses produtos encontra-se em torno de 
1600 CLP. Os valores máximo e mínimo que um produto desta 
categoria pode chegar são, respectivamente, 5719 e 209 CLP.
- É possível observar uma quantidade considerável de outliers 
acima dos demais dados no gráfico, confirmando assim que existem 
preços muito exacerbados para esta categoria, o que desencadeou 
na grande alteração da média em relação à mediana e no desvio 
padrão.

#### Gráfico de Barras com média de Desconto por categoria
- Com a montagem do gráfico de Barras, conseguimos observar que 
há uma quantidade de descontos maior e em maior quantidade nas 
categorias de congelados e de beleza/cuidado pessoal, enquanto 
nas categorias de comidas preparadas e lácteos a quantidade e 
valor de descontos são mais baixas. Por fim, as demais 
categorias não apresentam descontos em seus produtos no 
supermercado. 

#### Gráfico interativo de Sunburst
- Neste gráfico foi analisado a quantidade de produtos de cada 
categoria ocupando as prateleiras, seguida por uma subdivisão de
valor de Desconto dentro das Categorias e logo após outra 
subdivisão referindo-se às Marcas dos produtos.
- As três categorias que possuem mais produtos disponíveis no 
supermercado, em ordem, são Beleza/cuidado pessoal, Lácteos e 
Congelados que, por consequência, também são as categorias que 
mais apresentam mais valores de desconto.