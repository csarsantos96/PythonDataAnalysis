import pandas as pd
from sklearn.preprocessing import LabelEncoder

pd.set_option('display.width', None)

df = pd.read_csv('clientes-v2-tratados.csv')

print(df.head())

# Codificação para one-hot para 'estado_civil'
df = pd.concat([df, pd.get_dummies(df['estado_civil'], prefix='estado_civil')], axis=1)

print("\nDataFrame após codificação one-hot para 'estado_civil':\n", df.head())

# Codificação ordinal para 'nível_educação'
educacao_ordem = {'Ensino Fundamental': 1, 'Ensino Médio': 2, 'Ensino Superior': 3, 'Pós-graduação': 4}
df['nivel_educacao_ordinal'] = df['nivel_educacao'].map(educacao_ordem)

print("\nDataFrame após transformar 'nivel_educação' em códigos numéricos:\n", df.head())

# Transformar 'area_atuacao' em categoria codificadas usando o método .cat.codes
df['area_atuacao_cod'] = df['area_atuacao'].astype('category').cat.codes

print("\nDataFrame após transformar 'area_atuacao' em códigos numéricos:\n", df.head())

# LabelEncoder para 'estado
# LabelEncoder converte cada valor único em números de 0 a n_classes-1
label_encoder = LabelEncoder()
df['estado_cod'] = label_encoder.fit_transform(df['estado'])

print("\nDataFrame após aplicar LabelEncoder em 'estado':\n", df.head())