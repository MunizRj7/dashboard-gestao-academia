import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Dashboard de Gestão - Academia",
    page_icon="💪",
    layout="wide"
)

@st.cache_data
def carregar_dados():
    df = pd.read_csv('data/processed/dados_academia_tratados.csv', sep=';')
    return df

df = carregar_dados()

st.title("💪 Dashboard de Desempenho e Retenção - Academia")
st.markdown("Painel gerencial para acompanhamento de alunos, planos e engajamento.")

st.sidebar.header("Filtros")
plano_selecionado = st.sidebar.multiselect(
    "Selecione o Plano:",
    options=df['plano'].unique(),
    default=df['plano'].unique()
)

df_filtrado = df[df['plano'].isin(plano_selecionado)]

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total de Alunos", len(df_filtrado))
with col2:
    st.metric("Média de Visitas/Mês", f"{df_filtrado['visitas_mes'].mean():.1f}")
with col3:
    st.metric("Satisfação Média", f"{df_filtrado['satisfacao'].mean():.1f} / 5.0")
with col4:
    st.metric("Gasto Extra Médio", f"R$ {df_filtrado['gasto_extra_mensal'].mean():.2f}")

st.markdown("---")

col_A, col_B = st.columns(2)

with col_A:
    st.subheader("Distribuição por Tipo de Plano")
    fig_plano = px.pie(df_filtrado, names='plano', hole=0.4, color_discrete_sequence=px.colors.sequential.Teal)
    st.plotly_chart(fig_plano, use_container_width=True)

with col_B:
    st.subheader("Nível de Engajamento dos Alunos")
    fig_eng = px.histogram(df_filtrado, x='engajamento', color='engajamento', text_auto=True, color_discrete_sequence=px.colors.sequential.Blues)
    st.plotly_chart(fig_eng, use_container_width=True)

st.subheader("Visão Detalhada dos Alunos")
st.dataframe(df_filtrado, use_container_width=True)