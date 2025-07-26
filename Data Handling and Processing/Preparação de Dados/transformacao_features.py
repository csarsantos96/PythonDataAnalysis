import pandas as pd
import numpy as np
from scipy import stats

pd.set_option('display.width', None)

df = pd.read_csv('clientes-v2-tratados.csv')

print(df.head())

# Transformação Logarítima
df['salario_log'] = np.log1p(df['salario']) # log1p é usado para evitar problemas com valores zero

print("\nDataFrame após transformação logarítima no 'salario':\n", df.head())

# Transformação Box-Cox
df['salario_boxcox'], _ = stats.boxcox(df['salario'] + 1)

print("\nDataFrame após transformação Box-Cox  no 'salario':\n", df.head())

# Codificação de Frequência para 'estado'
estado_freq = df['estado'].value_counts() / len(df)
df['estado_freq'] = df['estado'].map(estado_freq)

print("\nDataFrame após codificação de frequência para  'estado':\n", df.head())

# Interações
df['interacao_idade_filhos'] = df['idade'] * df['numero_filhos']
print("\nDataFrame após criação de interações entre 'idade' e 'numero_filhos':\n", df.head())