import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('../Advanced Data Visualization/clientes-v3-preparado.csv')
print(df.head().to_string())

# Gráfico de Dispersão
sns.jointplot(x='idade', y='salario', data=df, kind='scatter')  # ['scatter', 'hist', 'hex', 'reg', 'resid']
plt.savefig("grafico_dispersao.png", dpi=300, bbox_inches='tight')
plt.show()

# Gráfico de Densidade
plt.figure(figsize=(10,6))
sns.kdeplot(df['salario'], fill=True, color="#863e9c", bw_adjust=0.5)
plt.title('Densidade de Salários')
plt.xlabel('Salário')
plt.tight_layout()
plt.savefig("grafico_densidade.png", dpi=300, bbox_inches='tight')
plt.show()

# Gráfico de Pairplot - Dispersão e Histograma
sns.pairplot(df[['idade', 'salario', 'anos_experiencia', 'nivel_educacao']])
plt.savefig("grafico_pairplot.png", dpi=300, bbox_inches='tight')
plt.show()

# Gráfico de Regressão
plt.figure(figsize=(10,6))
sns.regplot(  x='idade', y='salario', data=df, color='#278',scatter_kws={'alpha':0.5, 'color': '#cc2052'}
)
plt.title('Regressão de Salário por Idade')
plt.xlabel('Idade')
plt.ylabel('Salário')
plt.tight_layout()
plt.savefig("grafico_regressao.png", dpi=300, bbox_inches='tight')
plt.show()

# Gráfico countplot com hue
plt.figure(figsize=(10,6))
sns.countplot(x='estado_civil', hue='nivel_educacao', data=df, palette='pastel')
plt.xlabel('Estado Civil')
plt.ylabel('Quantidade Clientes')
plt.legend(title='Nível de Educação')
plt.tight_layout()
plt.savefig("grafico_countplot.png", dpi=300, bbox_inches='tight')
plt.show()
