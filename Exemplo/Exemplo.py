import pandas as pd

# Carregando dados de um arquivo CSV
data = pd.read_csv("dados.csv")

# Imprimindo as primeiras linhas dos dados
print(data.head())

# Calcular a média de uma coluna específica
mean = data["coluna"].mean()
print("Média: ", mean)

# Calcular a moda de uma coluna específica
mode = data["coluna"].mode()
print("Moda: ", mode)

# Calcular a mediana de uma coluna específica
median = data["coluna"].median()
print("Mediana: ", median)

# Calcular a correlação entre duas colunas
correlation = data["coluna1"].corr(data["coluna2"])
print("Correlação: ", correlation)

# Criar gráficos para visualizar os dados
data.plot(kind="scatter", x="coluna1", y="coluna2")
