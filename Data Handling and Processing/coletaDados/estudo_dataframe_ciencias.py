# Estudo Dataframe
import pandas as pd

# Lista: Uma coleção ordenada de elements que podem ser de qualquer tipo
lista_nome = ['Ana', 'Marcos', 'Carlos']
print('Lista de nomes:  \n', lista_nome[0] )

# Dicionario: Estrutura composta de pares chaves-valor
dicionario_pessoa ={
    'nome': 'Ana',
    'idade': 20,
    'cidade': 'Porto Alegre'
}
print('Dicionario de pessoas:\n', dicionario_pessoa)
print('Atributo do Dicionario: \n', dicionario_pessoa.get('nome'))

# Lista de dicionários: Estrutura de dados que combina listas e dicionários
dados = [
    {'nome': 'Ana', 'idade': 20, 'cidade': 'Porto Alegre'},
    {'nome': 'Marcos', 'idade': 25, 'cidade': 'Restinga Sêca'},
    {'nome': 'Carlos', 'idade': 35, 'cidade': 'Bagé'},
]

# Data frame: Estrutura de dados bidimensional
df = pd.DataFrame(dados)
print('Data Frame:\n', df)

# Selecionar a coluna
print(df['nome'])

# Selecionar várias colunas
print(df[['nome','idade']])

# Selecionar linhas pelo índice
print('Primeira linha \n', df.iloc[0])

# Adicionar uma nova coluna
df['salario'] = [4100,3600,5200]

# Adicionar um novo registro
df.loc[len(df)] = {
    'nome': 'João',
    'idade': 30,
    'salario': 10000,
}
print('DataFrame Atual \n', df)

# Removendo uma coluna
df.drop('salario', axis=1, inplace=True)

# Filtrando pessoas com mais de 29 anos
filtro_idade = df[df['idade'] > 30]
print('Filtro \n', filtro_idade)

# Salvando o DataFrame em um arquivo CSV
df.to_csv('dados.csv', index=False)

# Lendo um arquivo CSV em um DataFrame
df_lido = pd.read_csv('dados.csv')
print('\n Leitura do CSV \n', df_lido)

