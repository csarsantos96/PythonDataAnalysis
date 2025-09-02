import plotly.express as px
import pandas as pd
from matplotlib.pyplot import title

df=pd.read_csv('clientes-v3-preparado.csv')

# Gráfico de Dispersão
fig = px.scatter(df, x='idade', y='salario', color='nivel_educacao', hover_data=['estado_civil', 'area_atuacao'])
fig.update_layout(
    title='Idade vs Salário por Nível de Educação',
    xaxis_title='Idade',
    yaxis_title='Salário'

)
fig.write_image("grafico_dispersao_plotly.png", scale=2)
fig.show(renderer="browser")