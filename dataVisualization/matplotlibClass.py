import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('clientes-v3-preparado.csv')
print(df.head(20).to_string())

# Gráfico de Barras
plt.figure(figsize=(10, 6))
df['nivel_educacao'].value_counts().plot(kind='bar', color='#eee874')
plt.title('Divisão de Escolaridade -1')
plt.xlabel('Nível de Educação')
plt.ylabel('Quantidade')
plt.xticks(rotation=0)
plt.savefig("grafico_barras.png", dpi=300, bbox_inches='tight')
plt.show()

x = df['nivel_educacao'].value_counts().index
y = df['nivel_educacao'].value_counts().values

plt.figure(figsize=(10,6))
plt.bar(x, y, color='#60a')
plt.title('Divião de Escolaridade -2')
plt.xlabel('Nível de Educação')
plt.ylabel('Quantidade')

# Gráfico de Pizza
plt.figure(figsize=(10,6))
plt.pie(y, labels=x, autopct='%1.1f%%', startangle=90)
plt.title('Distribuição de Nível de Educação')
plt.savefig("grafico_pizza.png", dpi=300, bbox_inches='tight')
plt.show()

# Gráfico de Dispersão
plt.hexbin(df['idade'], df['salario'], gridsize=40, cmap='Blues')
plt.colorbar(label='Contagem dentro do bin')
plt.xlabel('Idade')
plt.ylabel('Salário')
plt.title('Dispersão de Idade e Salário')
plt.savefig("grafico_dispersao.png", dpi=300, bbox_inches='tight')
plt.show()

# Criar Gráfico de pizza
plt.figure(figsize=(8,8))