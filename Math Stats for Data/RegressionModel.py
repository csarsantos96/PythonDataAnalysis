import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import root_mean_squared_error, r2_score
import joblib

df = pd.read_csv('../dataVisualization/clientes-v3-preparado.csv')

#X = df[['anos_experiencia']] # Preditor
X= df[['idade','anos_experiencia', 'nivel_educacao_cod', 'area_atuacao_cod']] # Preditor
Y = df['salario'] # Prever

# Dividir dados: Treinamento e Teste
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Criar e Treinar modelo - Regressão Linear
modelo_lr = LinearRegression()
modelo_lr.fit(X_train, Y_train)

# Prever valores de teste
Y_prev = modelo_lr.predict(X_test)

#Métricas de avaliação
r2 = r2_score(Y_test, Y_prev)
print(f'Coeficiente de Determinação - R²: {r2:.2f}')

rmse = root_mean_squared_error(Y_test, Y_prev)
print(f'Raiz do Erro Quadrático Médio -RMSE: {rmse:.2f}')
print(f"Desvio Padrão do campo Salário: {df['salario'].std()}")

# Salvar modelo treinado
joblib.dump(modelo_lr, 'modelo_regressao_linear.pkl')