import numpy as np
import pandas as pd
# import numpy as np


pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv('../dataVisualization/clientes-v3-preparado.csv')

# Uso do Pandas
print('Estatística do dataframe: \n', df.describe())

print('Estatística de um campo: \n', df[['salario', 'idade']].describe())

print('Correlação: \n', df[['salario', 'idade']].corr())
print('Correlação com Normalização: \n', df[['salarioMinMaxScaler', 'idadeMinMaxScaler']].corr())
print('Correlação com Padronização: \n', df[['salarioStandardScaler', 'idadeStandardScaler']].corr())
print('Correlação com Padronização: \n', df[['salarioRobustScaler', 'idadeRobustScaler']].corr())

print('Correlação: \n', df[['salario', 'idade', 'idadeMinMaxScaler', 'idadeStandardScaler','idadeRobustScaler']].corr())

df_filtro_idade = df[df['idade'] < 65]
print('Correlação de Clientes menores de 65 anos: \n', df_filtro_idade[['salario', 'idade']].corr())

#Variável de espúria - aumenta com o tempo
df['variavel_espuria'] = np.arange(len(df))

print('Variavel-espuria', df['variavel_espuria'].values)

pearson_corr = df[['salario', 'idade', 'anos_experiencia', 'idade_anos_experiencia_interac','numero_filhos','nivel_educacao_cod', 'area_atuacao_cod', 'estado_cod', 'variavel_espuria']].corr()
spearman_corr = df[['salario', 'idade', 'anos_experiencia', 'idade_anos_experiencia_interac','numero_filhos','nivel_educacao_cod', 'area_atuacao_cod', 'estado_cod', 'variavel_espuria']].corr(method='spearman')

