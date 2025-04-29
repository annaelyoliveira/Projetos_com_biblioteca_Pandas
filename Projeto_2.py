!pip install Pandas
import pandas as pd

df = pd.read_csv('/content/Base_de_dados/registro_vendas.csv')
print(df)

# LIMPEZA DE DADOS
# 1. Identificando quais colunas contêm valores nulos e quantos valores nulos existem em cada uma
df.isnull().sum()

# 2. Substituindo os valores nulos na coluna Preço pela média dos valores não nulos
media_preco = df['Preço'].mean()
df = df.fillna({'Preço':media_preco}, inplace=False)
print(df)

# 3. Substituindo os valores nulos da coluna Estoque(Quantidade) por 0
df= df.fillna({'Estoque': 0}, inplace=False)

# Trocando valores nulos da categoria Produto por " - "
df = df.fillna({'Produto': ' - '}, inplace=False)
print(df)

# 4. Removendo as linhas onde a coluna Categoria possui valores nulos
df_sem_nulo_categoria = df.dropna(subset=['Categoria'], inplace=False)
print(df_sem_nulo_categoria)

# 5. Verificando se há dados duplicados
duplicados = df.duplicated()
print(duplicados)

print()

# Removendo dados duplicados do DF original
df = df.drop_duplicates(inplace=False)
print(df)
# *OBS Não tem dados duplicados

# 6. Criando um novo DataFrame contendo apenas os produtos da categoria “Grãos”
# OBS* não tem categoria Grãos ent ficou vazio o df

df_graos = df.loc[df['Categoria'] == 'Grãos']
print(df_graos)

# 7. Filtrando os produtos com preço superior a 10 e quantidade maior que 30
# *OBS no csv não tem quantidade e sim estoque, coloquei pra filtrar o estoque maior que 7 para que o df não ficasse vazio, caso fosse maior que 30 o df é vazio)

df_filtrado = df[(df['Preço'] > 10) & (df['Estoque'] > 7)]

print('Produtos com preço superior a 10 e Estoque maior que 7')
print(df_filtrado)


# MANIPULAÇÃO DE ESTRUTURAS

# 8. Adicionando uma coluna chamada “Receita”, que será o resultado de Preço multiplicado por Quantidade
df['Receita'] = df['Preço'] * df['Estoque']
print(df)

# 9. Criando uma nova coluna chamada “Margem de Lucro (%)”, com um valor fixo de 20% aplicado ao preço

def desconto_percentual(preco):
  desconto_fixo = 20
  return (desconto_fixo / preco) * 100

df['Margem de Lucro (%)'] = df['Preço'].apply(desconto_percentual)
# Arredondando os valores da coluna para 3 casas decimais
df['Margem de Lucro (%)'] = df['Margem de Lucro (%)'].round(3)
print(df)

# 10. Removendo a coluna Categoria do DataFrame
df_sem_categoria = df.drop(columns=['Categoria'], inplace=False)
print(df_sem_categoria)

# 11. Reorganizando as colunas do DataFrame para a seguinte ordem: Produto, Preço, Margem de Lucro (%), Quantidade, Receita
df = df[['Produto', 'Preço', 'Categoria', 'Margem de Lucro (%)', 'Estoque', 'Receita',]]
print(df)

# 12. Renomeando as colunas
df_renomeado = df.rename(columns={ 'Produto': 'Nome do Produto',
                        'Preço': 'Preço Unitário',
                        'Estoque': 'Quantidade Vendida' })
print(df_renomeado)

# 13. Renomeiando os índices para os dias da semana: ["Segunda", "Terça", "Quarta","Quinta", "Sexta", "Sábado", "Domingo"]

df = df.rename(index={0: 'Segunda', 1: 'Terça', 2: 'Quarta', 3: 'Quinta', 4: 'Sexta', 5: 'Sábado', 6: 'Domingo'})

#ORDENAÇÃO E FILTROS
# 14. Ordenando o DataFrame pelos valores de Preço em ordem crescente

df = df.sort_values(by='Preço', ascending= True,inplace=False)
print(df)

# 15. Ordenando os dados primeiro por Categoria (ascendente) e em seguida, por quantidade (estoque) (descendente)
df= df.sort_values(by=['Categoria','Estoque'], ascending= [True, False])

# 16. Reorganizando os índices do DataFrame em ordem alfabética
print("\n------- Ordenado pela ordem alfabética -------\n")
df.sort_index(ascending=True, inplace=True)

print(df)

# *OBS Ficou em ordem alfábetica Q, S, T

# Reordenando pelos dias da semana
dias_ordenados = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']

df = df.reindex(dias_ordenados)

print("\n------- Ordenado pelos dias da semana -------\n")
print(df)

# 17. Filtrando os produtos com preço entre 5 e 15
# *OBS não tem produtos com preço entre 5 e 15 ent alterei para filtrar os produtos com preço entre 500 e 1.500

df_between = df[df['Preço'].between(500, 1500)]
print('\n ------- Produtos com preço entre 500 e 1.500 ------\n')
print(df_between)

df_between = df[df['Estoque'].between(5, 10)]
print('\n ------- Produtos com estoque entre 5 e 10 ------\n')
print(df_between)

# Alterando os valores nulos da coluna Produto para poder selecionar os produto que contém a palavra 'Arroz'
df = df.fillna({'Produto': ' - '}, inplace=False)

# 18. Selecionando os produtos cujo nome contém a palavra "Arroz"

df_texto = df[df['Produto'].str.contains('Arroz', case = False)]

print(df_texto)

# *OBS Não tem produtos que contém a palavra "Arroz" ent o df está vazio

# 19. Filtrando linhas onde a Quantidade(estoque) seja maior que 20 e a Receita seja superior a 500 utilizando query
# OBS* Não tem produtos onde a Quantidade(estoque) seja maior que 20 e a Receita seja superior a 500

df_filtrado_query = df.query('Estoque >= 20 & Receita == 500')
print(df_filtrado_query)
