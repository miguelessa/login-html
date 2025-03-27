import streamlit as st # biblioteca para construção de dashboards
import pandas as pd # biblioteca de manipulação de dados no python 
import plotly.express as px # construção de gráficos

st.set_page_config(layout="wide")

# Com uma visão mensal
# Faturamento por unidade
# Tipo de produto mais vendido, contribuição por filial;
# Desempenho das formas de pagamento.
# Como estão as avaliações das filiais 

df = pd.read_csv("supermarket_sales.csv", sep=";", decimal=",")
df ["Date"] = pd.to_datetime(df["Date"])
df=df.sort_values("Date")

df["Month"] = df["Date"].apply(lambda x: str(x.year) + "-" + str(x. month))
month = st.sidebar.selectbox ("Mês", df["Month"].unique())


df_filtred = df[df["Month"] == month]


col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)

# Coluna 1

fig_date = px.bar(df_filtred, x="Date", y="Total", color="City", title="Faturamentos por dia")
col1.plotly_chart(fig_date, use_container_width=True) 

# Coluna 2

fig_prod = px.bar(df_filtred, x="Date", y="Product line", color="City", title="Faturamentos por tipo de produto", orientation="h")

col2.plotly_chart(fig_prod, use_container_width=True)

# Coluna 3

city_total = df_filtred.groupby("City") [["Total"]].sum().reset_index()
fig_city = px.bar(df_filtred, x="City", y="Total", title="Faturamentos por filial")

col3.plotly_chart(fig_city, use_container_width=True)

# Coluna 4

fig_kind = px.pie(df_filtred, values="Total", names="Payment", title="Faturamentos por tipo de pagamento")

col4.plotly_chart(fig_kind, use_container_width=True)

# Coluna 5

city_total = df_filtred.groupby("City") [["Rating"]].mean().reset_index()
fig_rating = px.bar(df_filtred, y="Rating", x="City", title="Avaliação")

col5.plotly_chart(fig_rating, use_container_width=True)

