import pandas as pd
import plotly.express as px

tabela = pd.read_excel("/home/usuario/Downloads/Vendas_Teste.xlsx")

# tabela = tabela.drop("nome", eixo=0"linha")
# tabela = tabela.drop("nome", eixo=1"coluna")
tabela = tabela.drop("Loja", axis=1)

# força a informação a virar um numero
tabela["Quantidade"] = pd.to_numeric(tabela["Quantidade"],errors="coerce")
print(tabela.info())

# exclui todas as colunas vazias
tabela = tabela.dropna(how="all", axis=1)

# exclui algumas as linhas vazias
tabela = tabela.dropna(how="any", axis=0)

print(tabela["Quantidade"].value_counts())
print(tabela["Quantidade"].value_counts(normalize=True))
print(tabela["Quantidade"].value_counts(normalize=True).map("{:.1%}".format))

for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna", color="Churn", text_auto=True)
    grafico.show()