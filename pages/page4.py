import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

def show():
     st.header("Pagina4")
     st.write("conteudo da pagina 4")

# Configurações iniciais
st.set_page_config(page_title="Análise de Dados", layout="wide")
st.title("📊 Análise de Dados")

# Carregar dados
try:
    df = pd.read_csv("data/dados.csv")
    st.success("Dados carregados com sucesso!")
except FileNotFoundError:
    st.error("Arquivo 'dados.csv' não encontrado na pasta 'data/'.")
    st.stop()

# 1. Apresentação dos dados e tipos de variáveis
st.subheader("🔍 Visualização Inicial")
st.markdown("""
**Sobre o conjunto de dados:**  
Este dataset contém informações sobre colaboradores da empresa, como salário, idade, tempo de experiência, escolaridade e setor.  
""")
st.dataframe(df.head())

st.write("### Colunas disponíveis no dataset:")
st.write(df.columns.tolist())

st.subheader("📌 Tipos de Variáveis")
tipos = pd.DataFrame(df.dtypes, columns=["Tipo"])
st.dataframe(tipos)

st.markdown("""
**Principais perguntas de análise:**  
- Qual é a média salarial dos colaboradores?  
- Existe correlação entre idade e salário?  
- A média salarial está alinhada com o valor de mercado?  
""")

# 2. Estatísticas descritivas
st.subheader("📈 Estatísticas Descritivas")
st.write(df.describe())

# Selecionar coluna numérica para análise detalhada
num_cols = df.select_dtypes(include=["float64", "int64"]).columns
coluna = st.selectbox("Selecione uma variável numérica para análise:", num_cols)

st.write(f"**Mediana de {coluna}:** {df[coluna].median():.2f}")
st.write(f"**Moda de {coluna}:** {df[coluna].mode()[0]:.2f}")
st.write(f"**Variância de {coluna}:** {df[coluna].var():.2f}")

# 3. Correlação entre variáveis numéricas
st.subheader("🔗 Correlação")
if len(num_cols) >= 2:
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(df[num_cols].corr(), annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)
else:
    st.info("Não há colunas numéricas suficientes para gerar o mapa de correlação.")

# 4. Intervalo de Confiança e Teste de Hipótese
st.subheader("🧪 Intervalo de Confiança e Teste de Hipótese")

# Definir média teórica
media_teorica = st.number_input("Informe a média teórica para comparação:", value=5000.0)

# Cálculo do IC
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

# Interpretação final
st.markdown(f"""
**Interpretação:**  
A média amostral de **{coluna}** foi de R$ {media_amostral:,.2f}.  
O intervalo de confiança indica que, com 95% de certeza, a média populacional está entre R$ {ic_95[0]:,.2f} e R$ {ic_95[1]:,.2f}.  
Como o p-valor foi {'menor' if p_valor < 0.05 else 'maior'} que 0.05, {'rejeitamos' if p_valor < 0.05 else 'não rejeitamos'} a hipótese nula de que a média é igual à média teórica.
""")

# Visualização da distribuição
st.subheader("📊 Distribuição da variável selecionada")
fig2, ax2 = plt.subplots()
sns.histplot(df[coluna], kde=True, ax=ax2)
ax2.axvline(media_teorica, color='blue', linestyle='--', label='Média Teórica')
ax2.axvline(ic_95[0], color='red', linestyle='--', label='Limite Inferior (IC)')
ax2.axvline(ic_95[1], color='green', linestyle='--', label='Limite Superior (IC)')
ax2.axvline(media_amostral, color='black', linestyle='-', label='Média Amostral')
ax2.legend()
st.pyplot(fig2)