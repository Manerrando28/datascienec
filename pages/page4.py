import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

# Configuração da página
st.set_page_config(page_title="📊 Análise de Dados", layout="wide")
st.title("📊 Análise de Dados")

# Função para carregar dados
@st.cache_data
def carregar_dados(caminho):
    try:
        return pd.read_csv(caminho)
    except FileNotFoundError:
        st.error("Arquivo 'dados.csv' não encontrado na pasta 'data/'.")
        return None

# Carregamento
df = carregar_dados("data/dados.csv")
if df is None:
    st.stop()
else:
    st.success("✅ Dados carregados com sucesso!")

# 🔍 Visualização Inicial
st.subheader("🔍 Visualização Inicial")
st.markdown("""
**Sobre o conjunto de dados:**  
Este dataset contém informações sobre colaboradores da empresa, como salário, idade, tempo de experiência, escolaridade e setor.
""")
st.dataframe(df.head())
st.write("### Colunas disponíveis no dataset:")
st.write(df.columns.tolist())

# 📌 Tipos de Variáveis
st.subheader("📌 Tipos de Variáveis")
st.dataframe(pd.DataFrame(df.dtypes, columns=["Tipo"]))

st.markdown("""
**Principais perguntas de análise:**  
- Qual é a média salarial dos colaboradores?  
- Existe correlação entre idade e salário?  
- A média salarial está alinhada com o valor de mercado?
""")

# 📈 Estatísticas Descritivas
st.subheader("📈 Estatísticas Descritivas")
st.write(df.describe())

# Seleção de variável numérica
num_cols = df.select_dtypes(include=["float64", "int64"]).columns
coluna = st.selectbox("Selecione uma variável numérica para análise:", num_cols)

# Estatísticas adicionais
st.write(f"**Mediana de {coluna}:** {df[coluna].median():.2f}")
st.write(f"**Moda de {coluna}:** {df[coluna].mode()[0]:.2f}")
st.write(f"**Variância de {coluna}:** {df[coluna].var():.2f}")

# 🔗 Correlação
st.subheader("🔗 Correlação")
if len(num_cols) >= 2:
    fig_corr, ax_corr = plt.subplots(figsize=(10, 6))
    sns.heatmap(df[num_cols].corr(), annot=True, cmap="coolwarm", ax=ax_corr)
    st.pyplot(fig_corr)
else:
    st.info("Não há colunas numéricas suficientes para gerar o mapa de correlação.")

# 🧪 Intervalo de Confiança e Teste de Hipótese
st.subheader("🧪 Intervalo de Confiança e Teste de Hipótese")
media_teorica = st.number_input("Informe a média teórica para comparação:", value=5000.0)

media_amostral = df[coluna].mean()
desvio_padrao = df[coluna].std()
n = df[coluna].count()
ic_95 = stats.norm.interval(0.95, loc=media_amostral, scale=desvio_padrao / np.sqrt(n))

st.markdown(f"""
**Intervalo de Confiança (95%) para a média de {coluna}:**  
De R$ {ic_95[0]:,.2f} até R$ {ic_95[1]:,.2f}
""")

# Teste de hipótese
t_stat, p_valor = stats.ttest_1samp(df[coluna].dropna(), media_teorica)
st.write(f"**T-estatística:** {t_stat:.2f}")
st.write(f"**P-valor:** {p_valor:.4f}")

if p_valor < 0.05:
    st.success("✅ Rejeitamos H₀: a média é significativamente diferente da média teórica.")
else:
    st.info("ℹ️ Não rejeitamos H₀: a média pode ser igual à média teórica.")

# Interpretação
st.markdown(f"""
**Interpretação:**  
A média amostral de **{coluna}** foi de R$ {media_amostral:,.2f}.  
O intervalo de confiança indica que, com 95% de certeza, a média populacional está entre R$ {ic_95[0]:,.2f} e R$ {ic_95[1]:,.2f}.  
Como o p-valor foi {'menor' if p_valor < 0.05 else 'maior'} que 0.05, {'rejeitamos' if p_valor < 0.05 else 'não rejeitamos'} a hipótese nula de que a média é igual à média teórica.
""")

# 📊 Visualização da Distribuição
st.subheader("📊 Distribuição da variável selecionada")
fig_dist, ax_dist = plt.subplots()
sns.histplot(df[coluna], kde=True, ax=ax_dist)
ax_dist.axvline(media_teorica, color='blue', linestyle='--', label='Média Teórica')
ax_dist.axvline(ic_95[0], color='red', linestyle='--', label='Limite Inferior (IC)')
ax_dist.axvline(ic_95[1], color='green', linestyle='--', label='Limite Superior (IC)')
ax_dist.axvline(media_amostral, color='black', linestyle='-', label='Média Amostral')
ax_dist.legend()
st.pyplot(fig_dist)
