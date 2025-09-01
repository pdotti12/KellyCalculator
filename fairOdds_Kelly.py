import streamlit as st

# --- Funções auxiliares ---

def calcular_odds_sem_juice_2way(odd1, odd2):
    try:
        odd1 = float(odd1)
        odd2 = float(odd2)
    except ValueError:
        return None, None # Retorna None se a conversão falhar

    p1 = 1 / odd1
    p2 = 1 / odd2
    overround = p1 + p2
    p1_fair = p1 / overround
    p2_fair = p2 / overround
    fair_odd1 = 1 / p1_fair
    fair_odd2 = 1 / p2_fair
    return fair_odd1, fair_odd2

def calcular_odds_sem_juice_3way(odd1, odd2, odd3):
    try:
        odd1 = float(odd1)
        odd2 = float(odd2)
        odd3 = float(odd3)
    except ValueError:
        return None, None, None # Retorna None se a conversão falhar

    p1 = 1 / odd1
    p2 = 1 / odd2
    p3 = 1 / odd3
    overround = p1 + p2 + p3
    p1_fair = p1 / overround
    p2_fair = p2 / overround
    p3_fair = p3 / overround
    fair_odd1 = 1 / p1_fair
    fair_odd2 = 1 / p2_fair
    fair_odd3 = 1 / p3_fair
    return fair_odd1, fair_odd2, fair_odd3

def calcular_kelly(odd_justa, odd_casa, fracao_kelly=1.0):
    try:
        odd_justa = float(odd_justa)
        odd_casa = float(odd_casa)
    except ValueError:
        return 0.0 # Retorna 0 se a conversão falhar

    if odd_casa <= 1.0 or odd_justa <= 1.0:
        return 0.0

    b = odd_casa - 1
    p = 1 / odd_justa
    q = 1 - p
    kelly_cheia = ((b * p) - q) / b
    if kelly_cheia <= 0:
        return 0.0
    aposta = kelly_cheia * fracao_kelly
    return aposta * 100

# --- Interface principal ---

st.set_page_config(page_title="Calculadora de Fair Odds e Kelly", layout="centered")
st.title("🎯 Calculadora de Apostas Esportivas")

tab1, tab2 = st.tabs(["📊 Fair Odds (sem juice)", "📈 Kelly Criterion"])

# --- Aba 1: Fair Odds ---
with tab1:
    st.subheader("📊 Remover Juice de Odds")

    st.markdown("### 🟦 Mercado com 2 resultados (ex: Tênis, UFC)")
    with st.form("form_2way"):
        col1, col2 = st.columns(2)
        with col1:
            # st.number_input foi substituído por st.text_input
            odd1_2way = st.text_input("Odd 1 (ex: Jogador A)", value="1.925")
        with col2:
            # st.number_input foi substituído por st.text_input
            odd2_2way = st.text_input("Odd 2 (ex: Jogador B)", value="1.869")

        submitted_2way = st.form_submit_button("Calcular Fair Odds - Mercado 2 resultados")

    if submitted_2way:
        fair1, fair2 = calcular_odds_sem_juice_2way(odd1_2way, odd2_2way)
        if fair1 is None:
            st.error("Por favor, insira valores numéricos válidos.")
        else:
            st.success("Odds justas (sem juice):")
            st.write(f"✅ Odd 1 justa: **{fair1:.4f}**")
            st.write(f"✅ Odd 2 justa: **{fair2:.4f}**")

    st.markdown("---")
    st.markdown("### 🟨 Mercado com 3 resultados (ex: Futebol 1X2)")
    with st.form("form_3way"):
        col3, col4, col5 = st.columns(3)
        with col3:
            # st.number_input foi substituído por st.text_input
            odd1_3way = st.text_input("Odd 1 (Vitória Time A)", value="2.00")
        with col4:
            # st.number_input foi substituído por st.text_input
            oddX_3way = st.text_input("Odd X (Empate)", value="3.20")
        with col5:
            # st.number_input foi substituído por st.text_input
            odd2_3way = st.text_input("Odd 2 (Vitória Time B)", value="3.40")

        submitted_3way = st.form_submit_button("Calcular Fair Odds - Mercado 3 resultados")

    if submitted_3way:
        fair1, fairX, fair2 = calcular_odds_sem_juice_3way(odd1_3way, oddX_3way, odd2_3way)
        if fair1 is None:
            st.error("Por favor, insira valores numéricos válidos.")
        else:
            st.success("Odds justas (sem juice):")
            st.write(f"✅ Vitória Time A: **{fair1:.4f}**")
            st.write(f"✅ Empate: **{fairX:.4f}**")
            st.write(f"✅ Vitória Time B: **{fair2:.4f}**")

# --- Aba 2: Kelly ---
with tab2:
    st.subheader("📈 Calculadora de Aposta - Critério de Kelly")
    st.markdown("Preencha os campos abaixo para calcular a porcentagem ideal da banca com base na fórmula de Kelly.")

    with st.form("formulario_kelly"):
        # st.number_input foi substituído por st.text_input
        odd_justa = st.text_input("Odd justa (sem juice)", value="1.92")
        odd_casa = st.text_input("Odd da casa (oferecida)", value="2.05")
        fracao_kelly = st.slider("Fração de Kelly", min_value=0.0, max_value=1.0, value=0.25, step=0.05)
        submitted_kelly = st.form_submit_button("Calcular")

    if submitted_kelly:
        resultado = calcular_kelly(odd_justa, odd_casa, fracao_kelly)
        if resultado <= 0:
            st.warning("⚠️ Não há valor esperado positivo. Melhor não apostar.")
        else:
            st.success(f"✅ Aposte **{resultado:.2f}% da banca** com Kelly {fracao_kelly}")