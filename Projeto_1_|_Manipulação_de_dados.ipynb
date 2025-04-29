!pip install pandas
import pandas as pd

# 2. Carregando base de dados localmente em um DataFrame
df = pd.read_csv('/content/base_de_dados/br_seeg_emissoes_brasil.csv.gz')

# 3. Carregando base de dados pela URL em um DataFrame
df = pd.read_csv('https://www.w3schools.com/python/pandas/data.csv') #tentei de todas as formas puxar o link csv do download do site do governo porém não consegui, ent fiz com o link do exemplo na aula

# 4. Exibindo as primeiras 15 linhas do DataFrame
df.head(15)

# 5. Exibindo as últimas 8 linhas do DataFrame
df.tail(8)

# 6. Verificando o tamanho do DataFrame e os tipos de dados e valores nulos
df.info()

# Obtendo as estatísticas das colunas numéricas
df.describe()

# 9.Salvando o DataFrame carregado nos formatos Excel e JSON
#Excel
df.to_excel("saida_excel.xlsx", index = False)

#JSON
df.to_json("saida_json.json", orient = 'records')

# 9. Criando um banco de dados SQLite e insirindo o DataFrame como uma tabela SQL

import sqlite3
conexao = sqlite3.connect('banco.db')
df.to_sql('tabela', conexao, if_exists='replace', index = False)

# 10. Usando uma consulta SQL para selecionar apenas colunas específicas

# Todas as colunas
df_sql = pd.read_sql_query("SELECT * FROM tabela", conexao)
print(df_sql.head())

# Coluna ano
df_sql = pd.read_sql_query("SELECT ano FROM tabela", conexao)
print(df_sql.head())

#Colunas tipo_emissao e gas
df_sql = pd.read_sql_query("SELECT tipo_emissao, gas FROM tabela", conexao)
print(df_sql.head())
