import pandas as pd
from scipy import stats
import re

# Melhor visualização no terminal
pd.set_option('display.width', None)

# Carregar dataset
df = pd.read_csv('clientes_limpeza.csv')

# Filtro inicial por idade
df_filtro_basico = df[df['idade'] > 20]
print('Filtro básico \n', df_filtro_basico[['nome', 'idade']])

# ------------------ OUTLIERS - Z-SCORE ------------------
z_scores = stats.zscore(df['idade'].dropna())
outliers_z = df[z_scores >= 3]
print('Outliers pelo Z-score:\n', outliers_z)

# Mantendo apenas registros com z-score < 3
df_zscore = df[(stats.zscore(df['idade']) < 3)]

# ------------------ OUTLIERS - IQR ------------------
Q1 = df['idade'].quantile(0.25)
Q3 = df['idade'].quantile(0.75)
IQR = Q3 - Q1

limite_baixo = Q1 - 1.5 * IQR
limite_alto = Q3 + 1.5 * IQR  # CORRIGIDO aqui

print('Limites IQR:', limite_baixo, limite_alto)

outliers_iqr = df[(df['idade'] < limite_baixo) | (df['idade'] > limite_alto)]
print('Outliers pelo IQR:\n', outliers_iqr)

# Filtrando os registros válidos com base no IQR
df_iqr = df[(df['idade'] >= limite_baixo) & (df['idade'] <= limite_alto)]

# ------------------ Limite manual (1 a 100 anos) ------------------
limite_baixo = 1
limite_alto = 100
df = df[(df['idade'] >= limite_baixo) & (df['idade'] <= limite_alto)]

# ------------------ Validar endereço ------------------
# Se o endereço tiver menos de 3 quebras de linha, consideramos inválido
df['endereco'] = df['endereco'].apply(
    lambda x: 'Endereço inválido' if isinstance(x, str) and len(x.split('\n')) < 3 else x
)

# ------------------ Validar nome ------------------
# Primeiro, remove espaços extras
df['nome'] = df['nome'].apply(lambda x: x.strip() if isinstance(x, str) else x)

# Depois, marca como inválido se for maior que 80 caracteres ou tiver números
df['nome'] = df['nome'].apply(
    lambda x: 'Nome inválido' if not isinstance(x, str) or len(x) > 80 or re.search(r'\d|\n', x) else x
)

# Exibir quantidade de nomes considerados inválidos
print('Qtd de registros com nomes inválidos:', (df['nome'] == 'Nome inválido').sum())

# ------------------ Exibir resultado final ------------------
print('Dados com outliers tratados:\n', df.head())

# ------------------ Salvar novo arquivo ------------------
df.to_csv('clientes_remove_outliers.csv', index=False)
print('Arquivo "clientes_remove_outliers.csv" salvo com sucesso! ✅')
