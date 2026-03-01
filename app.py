import streamlit as st
import plotly.graph_objects as go
import numpy as np
import time
from src.inference import MechGPTInference

# --- PAGE CONFIG ---
st.set_page_config(page_title="Mech-GPT | Axiom Lab", layout="wide")

# Custom CSS for the "Project Drishti" Industrial Look
st.markdown("""
    <style>
    .main { background-color: #0E1117; color: white; }
    .stMetric { background-color: #161B22; border: 1px solid #30363D; padding: 15px; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛠️ Mech-GPT: Acoustic Edge Intelligence")
st.write("### Team Axiom Lab | Powered by AMD Ryzen™ AI")

# --- HARDWARE STATUS ---
st.sidebar.header("Hardware Monitor")
st.sidebar.success("NPU State: Vitis AI Execution Provider ACTIVE")
st.sidebar.info("Architecture: AMD XDNA™")

# --- TOP LEVEL METRICS ---
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Machine Health", "98%", delta="Stable")
with col2:
    st.metric("NPU Latency", "1.12 ms", delta="-94% vs CPU", delta_color="inverse")
with col3:
    st.metric("Est. Savings", "₹1,25,800", delta="Live Calculation")

# --- LIVE SPECTROGRAM MOCKUP ---
st.subheader("Live Acoustic Spectrogram (AMD NPU Processed)")
chart_placeholder = st.empty()

# Simulate live data for the demo video
for i in range(15):
    # Simulated Mel-Spectrogram data
    z_data = np.random.standard_normal((20, 50))
    fig = go.Figure(data=go.Heatmap(z=z_data, colorscale='Viridis'))
    fig.update_layout(template="plotly_dark", height=400, margin=dict(l=10, r=10, t=10, b=10))
    chart_placeholder.plotly_chart(fig, use_container_width=True)
    time.sleep(0.3)

# --- ANOMALY LOGS ---
st.subheader("Predictive Maintenance Alerts")
st.warning("⚠️ Warning: Minor high-frequency spike detected in Bearing B-12. Lead time to failure: 28 Hours.")
if st.button("Order Spare Parts (Local Logistics)"):
    st.success("Logistics Request Sent: Estimated delivery 48 hours.")
