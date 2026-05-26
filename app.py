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
    
st.title("PET-Saúde")
st.subheader("GT 6: Vigilância Alimentar e Nutricional")
st.write("O GT 6 foca na capacitação de profissionais da Atenção Básica para o uso adequado de marcadores alimentares no SUS, integrando a transformação digital à saúde pública")

st.write(f"Página atual: {page}")
col1, col2 = st.columns(2)
with col1:
    st.image("./assets/logounb.jpg", width=80)
with col2:
    st.image("./assets/logo.png", width=80)