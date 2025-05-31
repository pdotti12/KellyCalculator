import streamlit as st

# --- Funções auxiliares ---

def calcular_odds_sem_juice_2way(odd1, odd2):
    p1 = 1 / odd1
    p2 = 1 / odd2
    overround = p1 + p2
    p1_fair = p1 / overround
    p2_fair = p2 / overround
    fair_odd1 = 1 / p1_fair
    fair_odd2 = 1 / p2_fair
    return round(fair_odd1, 3), round(fair_odd2, 3)

def calcular_odds_sem_juice_3way(odd1, odd2, odd3):
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
    return round(fair_odd1, 3), round(fair_odd2, 3), round(fair_odd3, 3)

def calcular_kelly(odd_justa, odd_casa, fracao_kelly=1.0):
    b = odd_casa - 1
    p = 1 / odd_justa
    q = 1 - p
    kelly_cheia = ((b * p) - q) / b
    if kelly_cheia <= 0:
        return 0.0
    aposta = kelly_cheia * fracao_kelly
    return round(aposta * 100, 2)

# --- Interface principal ---

st.set_page_config(page_title="Calculadora de Fair Odds e Kelly", layout="centered")
st.title("🎯 Calculadora de Apostas Esportivas")

tab1, tab2 = st.tabs(["📊 Fair Odds (sem juice)", "📈 Kelly Criterion"])

# --- Aba 1: Fair Odds ---
with tab1:
    st.subheader("📊 Remover Juice de Odds")

    st.markdown("### 🟦 Mercado com 2 resultados (ex: Tênis, UFC)")
    col1, col2 = st.columns(2)
    with col1:
        odd1_2way = st.number_input("Odd 1 (ex: Jogador A)", min_value=1.000, value=1.925, step=0.001, format="%.3f", key="odd1_2way")
    with col2:
        odd2_2way = st.number_input("Odd 2 (ex: Jogador B)", min_value=1.000, value=1.869, step=0.001, format="%.3f", key="odd2_2way")

    if st.button("Calcular Fair Odds - Mercado 2 resultados"):
        fair1, fair2 = calcular_odds_sem_juice_2way(odd1_2way, odd2_2way)
        st.success("Odds justas (sem juice):")
        st.write(f"✅ Odd 1 justa: **{fair1:.3f}**")
        st.write(f"✅ Odd 2 justa: **{fair2:.3f}**")

    st.markdown("---")
    st.markdown("### 🟨 Mercado com 3 resultados (ex: Futebol 1X2)")
    col3, col4, col5 = st.columns(3)
    with col3:
        odd1_3way = st.number_input("Odd 1 (Vitória Time A)", min_value=1.000, step=0.001, format="%.3f", key="odd1_3way")
    with col4:
        oddX_3way = st.number_input("Odd X (Empate)", min_value=1.000, step=0.001, format="%.3f", key="oddX_3way")
    with col5:
        odd2_3way = st.number_input("Odd 2 (Vitória Time B)", min_value=1.000, step=0.001, format="%.3f", key="odd2_3way")

    if st.button("Calcular Fair Odds - Mercado 3 resultados"):
        fair1, fairX, fair2 = calcular_odds_sem_juice_3way(odd1_3way, oddX_3way, odd2_3way)
        st.success("Odds justas (sem juice):")
        st.write(f"✅ Vitória Time A: **{fair1:.3f}**")
        st.write(f"✅ Empate: **{fairX:.3f}**")
        st.write(f"✅ Vitória Time B: **{fair2:.3f}**")

# --- Aba 2: Kelly ---
with tab2:
    st.subheader("📈 Calculadora de Aposta - Critério de Kelly")
    st.markdown("Preencha os campos abaixo para calcular a porcentagem ideal da banca com base na fórmula de Kelly.")

    with st.form("formulario_kelly"):
        odd_justa = st.number_input("Odd justa (sem juice)", min_value=1.01, step=0.01, format="%.3f")
        odd_casa = st.number_input("Odd da casa (oferecida)", min_value=1.01, step=0.01, format="%.3f")
        fracao_kelly = st.slider("Fração de Kelly", min_value=0.0, max_value=1.0, value=0.25, step=0.05)
        submitted = st.form_submit_button("Calcular")

    if submitted:
        resultado = calcular_kelly(odd_justa, odd_casa, fracao_kelly)
        if resultado == 0.0:
            st.warning("⚠️ Não há valor esperado positivo. Melhor não apostar.")
        else:
            st.success(f"✅ Aposte **{resultado}% da banca** com Kelly {fracao_kelly}")
