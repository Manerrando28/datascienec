import streamlit as st

def show():
     st.header("Pagina1")
     st.write("conteudo da pagina 1")

# Configuração da página
st.set_page_config(page_title="Dashboard CP1 - Gabriel", layout="wide")

# Título principal
st.title("👋 Bem-vindo ao Dashboard CP1 - Gabriel")

# Introdução pessoal
st.markdown("""
### Sobre mim  
Olá! Meu nome é **Gabriel**, sou estudante de [Engenharia de software] e apaixonado por dados, tecnologia e soluções inteligentes.  
Este dashboard foi desenvolvido como parte do CP1 da disciplina de Programação para Ciência de Dados, utilizando **Python** e **Streamlit**.

""")

# Objetivo profissional
st.markdown("""
### Objetivo Profissional  
Meu objetivo é atuar na área de **Análise de Dados**, aplicando técnicas estatísticas e ferramentas de visualização para gerar insights que apoiem decisões estratégicas.  
Busco constantemente aprender novas tecnologias e aprimorar minhas habilidades em programação, modelagem e comunicação de resultados.

""")

# Apresentação do projeto
st.markdown("""
### Sobre o Projeto  
Este dashboard apresenta uma análise exploratória de um conjunto de dados fictício de colaboradores, abordando estatísticas descritivas, correlações, testes de hipótese e intervalos de confiança.  
O objetivo é demonstrar domínio técnico e capacidade analítica na construção de soluções interativas com Streamlit.

""")

# Mensagem final
st.info("Explore as abas abaixo para visualizar as análises e interpretações realizadas!")
