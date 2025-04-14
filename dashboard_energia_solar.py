# dashboard_energia_solar.py

import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta
import random

# Simulando dados dos últimos 30 dias
dias = [datetime.now() - timedelta(days=i) for i in range(29, -1, -1)]
energia_gerada = [round(random.uniform(8.0, 15.0), 2) for _ in dias]
energia_consumida = [round(gerada * random.uniform(0.6, 1.1), 2) for gerada in energia_gerada]

df = pd.DataFrame({
    "Data": dias,
    "Energia Gerada (kWh)": energia_gerada,
    "Energia Consumida (kWh)": energia_consumida
})

# Layout do Streamlit
st.set_page_config(page_title="Dashboard de Energia Solar", layout="wide")

st.title("☀️ Dashboard de Energia Solar Residencial")

# Métricas principais (dia atual)
energia_hoje = df.iloc[-1]
st.subheader("Resumo de Hoje")
col1, col2 = st.columns(2)
col1.metric("🔋 Energia Gerada", f"{energia_hoje['Energia Gerada (kWh)']} kWh")
col2.metric("⚡ Energia Consumida", f"{energia_hoje['Energia Consumida (kWh)']} kWh")

# Gráfico de linha
st.subheader("📈 Histórico de Energia (Últimos 30 dias)")
fig = px.line(df, x="Data", y=["Energia Gerada (kWh)", "Energia Consumida (kWh)"],
              labels={"value": "Energia (kWh)", "variable": "Tipo"},
              title="Geração vs Consumo de Energia")
st.plotly_chart(fig, use_container_width=True)

# Sugestões práticas
st.subheader("💡 Dicas de Otimização")
if energia_hoje['Energia Consumida (kWh)'] > energia_hoje['Energia Gerada (kWh)']:
    st.warning("Você consumiu mais do que gerou hoje. Considere reduzir o uso de equipamentos pesados no horário de menor geração solar.")
else:
    st.success("Bom trabalho! Hoje você gerou mais energia do que consumiu.")

st.markdown("---")
st.caption("Protótipo desenvolvido para o projeto UPX-III - Grupo 13")
