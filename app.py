import streamlit as st
import pandas as pd
import numpy as np

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Credit Card Fraud Detection",
    page_icon="💳",
    layout="wide"
)

# ================= PREMIUM UI CSS =================
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
}
.main-title {
    font-size: 3rem;
    font-weight: 900;
    text-align: center;
    color: #00e5ff;
}
.subtitle {
    text-align: center;
    color: #cccccc;
    margin-bottom: 2rem;
}
.card {
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(12px);
    border-radius: 20px;
    padding: 1.6rem;
    box-shadow: 0 10px 35px rgba(0,0,0,0.35);
}
.metric {
    background: linear-gradient(135deg, #00c6ff, #0072ff);
    border-radius: 18px;
    padding: 1.3rem;
    text-align: center;
    color: white;
    font-weight: 700;
}
</style>
""", unsafe_allow_html=True)

# ================= HEADER =================
st.markdown("<div class='main-title'>💳 Credit Card Fraud Detection</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Enterprise-Grade Fraud Monitoring Dashboard</div>", unsafe_allow_html=True)

# ================= SIDEBAR =================
st.sidebar.title("⚙️ Control Panel")
threshold = st.sidebar.slider("Fraud Risk Threshold", 0.1, 0.9, 0.5)
st.sidebar.info("Demo Mode (UI Focused)")

# ================= SYNTHETIC DATA =================
np.random.seed(42)
data = pd.DataFrame({
    "Amount": np.random.uniform(1, 5000, 1500),
    "Time": np.random.uniform(0, 60000, 1500),
    "Transaction_Type": np.random.randint(0, 6, 1500)
})

# ================= DASHBOARD =================
col1, col2 = st.columns([1.4, 1])

with col1:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("📊 Transaction Preview")
    st.dataframe(data.head(12), use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("📈 System Metrics")

    m1, m2, m3 = st.columns(3)
    m1.markdown("<div class='metric'>Transactions<br>1500</div>", unsafe_allow_html=True)
    m2.markdown("<div class='metric'>Model<br>Active</div>", unsafe_allow_html=True)
    m3.markdown(f"<div class='metric'>Threshold<br>{threshold}</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# ================= RISK ANALYSIS =================
st.markdown("---")
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("🤖 Risk Analysis Summary")

st.write("""
• High-value transactions are more likely to be flagged  
• Transactions occurring at unusual times raise risk  
• Certain transaction types are historically suspicious  

(This is a **UI-safe analytical summary**, no ML dependency)
""")

st.progress(65)
st.caption("Overall Fraud Risk Index")

st.markdown("</div>", unsafe_allow_html=True)

# ================= LIVE FRAUD CHECK =================
st.markdown("---")
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("🔍 Live Transaction Fraud Check")

c1, c2, c3 = st.columns(3)
amount = c1.number_input("Transaction Amount", 1.0, 5000.0)
time = c2.number_input("Transaction Time")
ttype = c3.selectbox("Transaction Type", [0, 1, 2, 3, 4, 5])

# Simulated risk score (error-free)
risk_score = (amount / 5000) * 0.6 + (ttype / 5) * 0.4

if risk_score >= threshold:
    st.error(f"🚨 FRAUD DETECTED\n\nRisk Score: {risk_score:.2f}")
else:
    st.success(f"✅ LEGIT TRANSACTION\n\nRisk Score: {risk_score:.2f}")

st.markdown("</div>", unsafe_allow_html=True)

# ================= FOOTER =================
st.markdown("---")
st.markdown(
    "<center style='color:#aaa'>🚀 Credit Card Fraud Detection • Streamlit High-End UI</center>",
    unsafe_allow_html=True
)
