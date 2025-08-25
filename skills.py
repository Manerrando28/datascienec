import streamlit as st

# Configuração da página
st.set_page_config(page_title="Skills Técnicas e Comportamentais", layout="wide")

# Título da seção
st.header("🧠 Skills Técnicas e Comportamentais")

# Tecnologias
st.subheader("💻 Tecnologias e Ferramentas")
st.markdown("""
Abaixo estão algumas das principais ferramentas que domino, com nível de proficiência estimado em ordem de porcentagem:
""")

st.write("**Python**")
st.progress(80)

st.write("**Java Script**")
st.progress(70)

st.write("**SQL**")
st.progress(60)

st.write("**Power BI**")
st.progress(50)

# Soft Skills
st.subheader("🤝 Soft Skills")
st.markdown("""
Além das habilidades técnicas, valorizo competências comportamentais que fazem a diferença em ambientes colaborativos e dinâmicos:
- 🗣️ **Comunicação eficaz**: Clareza na troca de ideias e escuta ativa  
- 👥 **Trabalho em equipe**: Colaboração, empatia e foco em resultados coletivos  
- 🧩 **Resolução de problemas**: Pensamento crítico e criatividade para superar desafios
""")

# Mensagem final
st.info("Essas habilidades refletem meu compromisso com o desenvolvimento contínuo e com a entrega de soluções inteligentes.")