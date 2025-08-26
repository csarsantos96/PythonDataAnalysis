import pandas as pd
# import numpy as np


pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv('clientes-v3-preparado.csv')

# Uso do Pandas
print('Estatística do dataframe: \n', df.describe())

print('Estatística de um campo: \n', df[['salario', 'idade']].describe())

print('Correlação: \n', df[['salario', 'idade']].corr())
print('Correlação com Normalização: \n', df[['salarioMinMaxScaler', 'idadeMinMaxScaler']].corr())
print('Correlação com Padronização: \n', df[['salarioStandardScaler', 'idadeStandardScaler']].corr())
print('Correlação com Padronização: \n', df[['salarioRobustScaler', 'idadeRobustScaler']].corr())