import streamlit as st

def show():
     st.header("Pagina2")
     st.write("conteudo da pagina 2")

# Configuração da página
st.set_page_config(page_title="Formação e Experiência", layout="wide")

# Título da seção
st.header("🎓 Formação e 💼 Experiência Profissional")

# Formação acadêmica
st.subheader("📚 Formação Acadêmica")
st.markdown("""
- **Curso:** Análise e Desenvolvimento de Sistemas  
- **Instituição:** [Fiap]  
- **Período:** [2024] – [2027]
""")

# Certificações
st.subheader("📜 nanos courses de blockchain criptomoeda, design software , pyton, java script entre outros")
st.markdown("""
- **Python para Análise de Dados** – [fiap]  
- **SQL para Banco de Dados** – [fiap]  
- **Power BI: Dashboards Interativos** – [alura]
- **Java Script: Dashboards Interativos** – [alura]
""")

# Experiência profissional
st.subheader("💼 Experiência Profissional")
st.markdown("""
- **Empresa:** XYZ  
- **Cargo:** Estagiário em Análise de Dados  
- **Período:** [ainda em processo] – [ainda em processo]  
- **Atividades:**  
  - Coleta e limpeza de dados  
  - Criação de dashboards com Power BI  
  - Apoio em análises estatísticas e relatórios gerenciais
""")

# Mensagem final
st.info("Essa página apresenta minha trajetória acadêmica e profissional, destacando habilidades técnicas e experiências relevantes.")