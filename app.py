import streamlit as st
import pandas as pd
import numpy as np

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Sentinel AI | Fraud Detection",
    page_icon="🛡️",
    layout="wide"
)

# ================= THEME STATE MANAGEMENT =================
if 'theme' not in st.session_state:
    st.session_state.theme = 'dark'

def toggle_theme():
    st.session_state.theme = 'light' if st.session_state.theme == 'dark' else 'dark'

# ================= DYNAMIC PREMIUM UI CSS =================
if st.session_state.theme == 'dark':
    bg_gradient = "radial-gradient(circle at 20% 30%, #161a25 0%, #0b0d13 100%)"
    card_bg = "rgba(255, 255, 255, 0.03)"
    card_border = "rgba(255, 255, 255, 0.1)"
    text_main = "#ffffff"
    text_sub = "#94a3b8"
    metric_bg = "rgba(255, 255, 255, 0.05)"
    shadow = "0 8px 32px 0 rgba(0, 0, 0, 0.8)"
else:
    bg_gradient = "radial-gradient(circle at 20% 30%, #f0f2f6 0%, #dfe3ee 100%)"
    card_bg = "rgba(255, 255, 255, 0.7)"
    card_border = "rgba(0, 0, 0, 0.1)"
    text_main = "#1e293b"
    text_sub = "#64748b"
    metric_bg = "rgba(0, 0, 0, 0.03)"
    shadow = "0 8px 32px 0 rgba(31, 38, 135, 0.1)"

st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap');

    .stApp {{
        background: {bg_gradient};
        transition: all 0.5s ease;
    }}

    .premium-card {{
        background: {card_bg};
        border: 1px solid {card_border};
        border-radius: 20px;
        padding: 1.5rem;
        backdrop-filter: blur(15px);
        margin-bottom: 1rem;
        box-shadow: {shadow};
        color: {text_main};
    }}

    .metric-container {{
        text-align: center;
        padding: 1rem;
        border-radius: 15px;
        background: {metric_bg};
        border: 1px solid {card_border};
    }}
    
    .metric-value {{
        font-size: 1.8rem;
        font-weight: 800;
        color: #00e5ff;
    }}
    
    .metric-label {{
        color: {text_sub};
        font-size: 0.7rem;
        text-transform: uppercase;
        letter-spacing: 1px;
    }}

    .main-title {{
        color: {text_main};
        font-size: 3rem;
        font-weight: 800;
        margin-bottom: 0;
    }}

    .progress-loader {{
        width: 100%;
        background: {metric_bg};
        border-radius: 10px;
        height: 12px;
        margin: 10px 0;
    }}
    
    /* Smooth transition for theme switching */
    * {{ transition: background-color 0.5s ease, color 0.5s ease; }}
</style>
""", unsafe_allow_html=True)

# ================= SIDEBAR =================
with st.sidebar:
    st.markdown("## ⚙️ Settings")
    
    # Theme Toggle Button
    theme_label = "🌙 Dark Mode" if st.session_state.theme == 'light' else "☀️ Light Mode"
    st.button(theme_label, on_click=toggle_theme, use_container_width=True)
    
    st.markdown("---")
    threshold = st.slider("Risk Sensitivity", 0.1, 0.9, 0.6)
    st.info(f"Theme: {st.session_state.theme.capitalize()}")

# ================= HEADER =================
st.markdown(f"<h1 class='main-title'>SENTINEL <span style='color:#00e5ff'>AI</span></h1>", unsafe_allow_html=True)
st.markdown(f"<p style='color:{text_sub}; margin-top:-10px;'>Enterprise Fraud Monitoring • 2026 Edition</p>", unsafe_allow_html=True)

# ================= TOP METRICS =================
m1, m2, m3, m4 = st.columns(4)
stats = [("Live Feed", "1,842"), ("High Risk", "14"), ("Accuracy", "99.2%"), ("Latency", "24ms")]

for col, (label, val) in zip([m1, m2, m3, m4], stats):
    col.markdown(f"""
    <div class="metric-container">
        <div class="metric-value">{val}</div>
        <div class="metric-label">{label}</div>
    </div>
    """, unsafe_allow_html=True)

# ================= INPUT SECTION =================
st.markdown('<div class="premium-card">', unsafe_allow_html=True)
st.subheader("🔍 Transaction Inspector")

c1, c2, c3 = st.columns(3)
with c1:
    amount = st.number_input("Transaction Amount ($)", min_value=0.0, value=1500.0)
with c2:
    location = st.selectbox("Origin", ["Domestic", "International (Safe)", "International (High Risk)"])
with c3:
    ttype = st.selectbox("Type", ["Online", "POS", "Wire Transfer"])

# Risk Logic
loc_map = {"Domestic": 0.1, "International (Safe)": 0.3, "International (High Risk)": 0.8}
type_map = {"Online": 0.2, "POS": 0.1, "Wire Transfer": 0.6}
risk_score = min(((amount/5000) * 0.4) + loc_map[location] + type_map[ttype], 1.0)

# CSS Progress Bar
bar_color = "#ff4b4b" if risk_score >= threshold else "#00e5ff"
st.markdown(f"""
    <div style="margin-top:20px;">
        <span style="color:{text_sub}; font-size:0.9rem;">Calculated Risk Index: <b>{risk_score*100:.1f}%</b></span>
        <div class="progress-loader">
            <div style="height: 12px; border-radius: 10px; width: {risk_score*100}%; background: {bar_color};"></div>
        </div>
    </div>
""", unsafe_allow_html=True)

if risk_score >= threshold:
    st.error(f"🚨 ALERT: FRAUD PROBABILITY {risk_score*100:.1f}%")
else:
    st.success(f"✅ SECURE: TRANSACTION VERIFIED")

st.markdown('</div>', unsafe_allow_html=True)

# ================= DATA PREVIEW =================
st.markdown('<div class="premium-card">', unsafe_allow_html=True)
st.subheader("📋 Recent Forensic Logs")
data = pd.DataFrame({
    "Timestamp": ["12:05", "12:08", "12:12", "12:15"],
    "Status": ["Verified", "Verified", "Flagged", "Verified"],
    "Amount": ["$120.00", "$45.50", "$4,900.00", "$12.99"],
    "Risk": [0.1, 0.05, 0.88, 0.02]
})
st.dataframe(data, use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)
