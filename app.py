import streamlit as st
from streamlit_navigation_bar import st_navbar
import os
from pathlib import Path

st.set_page_config(initial_sidebar_state="collapsed")

st.markdown(
    """
    <style>
        div[data-testid="stHeading"] {
            text-align: center !important;
        }

        div[data-testid="stHeading"] h1 {
            width: 100% !important;
            text-align: center !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

with open(Path(__file__).parent / "style.css") as f:
    navbar_css = f.read()

# Define as páginas do menu
pages = ["📊 Submeter Dados", "📈 Sala de Situação Alimentar"]

# Caminho para sua logo (precisa ser .svg)
logo_path = Path(__file__).parent / "assets" / "logo.svg"  

styles = {
    "nav": {
        "background-color": "#2C3A6B",
        "height": "70px",
        "display": "flex",
        "align-items": "center",
        "justify-content": "center",
        "padding-left": "2rem",
        "padding-right": "20rem",
    },
    "div": {
        "max-width": "none",
        "width": "100%",
        "display": "flex",
        "align-items": "center",
    },
    "ul": {
        "width": "100%",
        "display": "flex",
        "align-items": "center",
        "gap": "32px",
    },
    "li": {
        "display": "flex",
        "align-items": "center",
    },
    "a": {
        "text-decoration": "none",
    },
    "span": {
        "color": "white",
        "font-size": "16px",
        "padding": "14px",
        "background": "rgba(255,255,255,0.05)",
        "border-radius": "15px",
        "transition": "all 0.3s ease",
        "text-decoration": "none",
        "display": "inline-block",
    },
    "hover": {
        "color": "white",
        "background-color": "rgba(255,255,255,0.12)",
    },
    "active": {
        "color": "#2C3A6B",
        "background": "#F2C94C",
        "transform": "translateY(-1px)",
        "letter-spacing": ".5px",
    },
    "img": {
        "height": "60px",
    },
}

st.markdown("""
<style>
div.stButton > button {
    width: 100%;
    height: 100px;
    font-size: 18px;
    border-radius: 12px;
    background-color: #2C3A6B;
    color: white;
}
div.stButton > button:hover {
    background-color: #F2C94C;
    color: #2C3A6B;
    transform: translateY(-1px);
    letter-spacing: .5px;
}
</style>
""", unsafe_allow_html=True)

# Cria a navbar
try:
    page = st_navbar(
        pages=pages,
        logo_path=str(logo_path) if logo_path else None,  # Logo fica na esquerda
        styles=styles,
        css=navbar_css,
        selected="📊 Submeter Dados"  # Página inicial selecionada
    )
except TypeError:
    # Fallback se o parâmetro pages não funcionar
    page = st_navbar(
        pages,
        logo_path=logo_path,
        styles=styles,
        css=navbar_css,
    )

col3, col4, col5= st.columns([2,1,2])
with col4:
    st.image("./assets/logo.png", width=300)
    
st.title("PET-Saúde")
st.subheader("GT 6: Vigilância Alimentar e Nutricional")
st.write("O GT 6 foca na capacitação de profissionais da Atenção Básica para o uso adequado de marcadores alimentares no SUS, integrando a transformação digital à saúde pública")
st.divider()
# BOTÕES CENTRALIZADOS
col1, col2, col3, col4 = st.columns([2,1,1,2])

with col2:
    btn1 = st.button("Submeter Dados")

with col3:
    btn2 = st.button("Sala de Situação Alimentar")

# AÇÕES
if btn1:
    st.write("Dashboard clicado")

if btn2:
    st.write("Relatórios clicado")

st.divider()

st.title("Equipe GT-6")
st.header("Integrantes")
st.subheader("Gestão")
st.write("**Patrícia de Fragas** - Coordenadora")
st.write("**David Francisco** - Coordenador Adjunto")
st.write("**Rafaela Garcia** - Gestora Júnior")
st.write("**Raynara Ferreira** - Gestor Júnior")

st.subheader("Equipe de Comunicação")
st.write("**Eduarda Nascimento** - Comunicação e Design")
st.write("**Yasmin Fagundes** - Comunicação e Design")

st.subheader("Equipe de TI")
st.write("**Cauã Nicolas** - TI")
st.write("**Pedro Augusto** - TI")
st.write("**Jean Carlos** - TI")

st.subheader("Equipe de Pesquisa")
st.write("**Débora Beatriz** - Pesquisa")
st.write("**Kelly Cristina** - Pesquisa")    
st.write("**Taís Nazário** - Pesquisa")
st.write("**Tainá Ribeiro** - Pesquisa")
st.write("**Talitha de Souza** - Pesquisa")

st.subheader("Preceptores")
st.write("**Ana Paula Loschi** - Preceptora - UBS Jardins Mangueiral")
st.write("**Leniela Afra** - Preceptora - DIRAPS")
st.write("**Vanessa Araújo** - Preceptora - UBS Gama")

st.divider()

st.write(f"Página atual: {page}")

col1, col2 = st.columns(2)
with col1:
    st.image("./assets/logounb.jpg", width=80)
with col2:
    st.image("./assets/logo.png", width=80)