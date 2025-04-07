import streamlit as st

def calcular_kelly(odd_casa, odd_justa, fracao_kelly=1.0):
    b = odd_casa - 1
    p = 1 / odd_justa
    q = 1 - p

    kelly_cheia = ((b * p) - q) / b

    if kelly_cheia <= 0:
        return 0.0

    aposta = kelly_cheia * fracao_kelly
    return round(aposta * 100, 2)  # porcentagem da banca

# Interface
st.title("📈 Calculadora de Aposta - Critério de Kelly")

st.markdown("Preencha os campos abaixo para calcular a porcentagem ideal da banca com base na fórmula de Kelly.")

with st.form("formulario_kelly"):
    odd_casa = st.number_input("Odd turbinada", min_value=1.01, step=0.01)
    odd_justa = st.number_input("Odd justa", min_value=1.01, step=0.01)
    fracao_kelly = st.slider("Fração de Kelly", min_value=0.0, max_value=1.0, value=0.15, step=0.05)
    submitted = st.form_submit_button("Calcular")

if submitted:
    resultado = calcular_kelly(odd_casa, odd_justa, fracao_kelly)
    
    if resultado == 0.0:
        st.warning("⚠️ Não há valor esperado positivo. Melhor não apostar.")
    else:
        st.success(f"✅ Aposte **{resultado}% da banca** com Kelly {fracao_kelly}")
