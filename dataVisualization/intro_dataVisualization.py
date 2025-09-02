import matplotlib.pyplot as plt
import seabornClass as sns
import pandas as pd

df = pd.read_csv('clientes-v3-preparado.csv')

print (df.head().to_string())

# Histograma
plt.hist(df['salario'])
plt.savefig("histograma_simples.png", dpi=300, bbox_inches='tight')
plt.show()

# Histograma - Parâmetros
plt.figure(figsize=(10,6))
plt.hist(df['salario'], bins=100, color='green', alpha=0.8)
plt.title('Histograma - Distribuição de Salários')
plt.xlabel('Salário')
plt.xticks(ticks=range(0, int(df['salario'].max())+2000, 2000))
plt.ylabel('Frequência')
plt.grid(True)
plt.savefig("histograma_detalhado.png", dpi=300, bbox_inches='tight')
plt.show()

# Múltiplos gráficos
plt.figure(figsize=(10,6))
plt.subplot(2,2,1) # 2 linhas, 2 colunas, 1 gráfico
#Gráfico de Dispersão
plt.scatter(df['salario'], df['salario'])
plt.title('Dispersão - Salário e Salário')
plt.xlabel('Salário')
plt.ylabel('Salário')

plt.subplot(1,2,2) # 1 linha, 2 colunas, 2 gráfico
plt.scatter(df['salario'], df['anos_experiencia'], color='#eba134', alpha=0.6, s=30) # cor hexadecimal online
plt.title('Dispersão - Idade e anos de experiência')
plt.xlabel('Salário')
plt.ylabel('Anos de Experiência')

# Mapa de calor
corr = df[['salario', 'anos_experiencia']].corr()
plt.subplot(2,2,3) # 1 linha, 2 colunas, 1 gráfico
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlação Salário e Idade')

plt.tight_layout() # Ajustar espaçamentos
plt.savefig("multiplos_graficos.png", dpi=300, bbox_inches='tight')
plt.show()