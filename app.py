import streamlit as st
import pandas as pd
import numpy as np
import pickle

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Credit Card Fraud Detection",
    page_icon="💳",
    layout="wide"
)

# ================= PREMIUM CSS =================
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
    padding: 1.5rem;
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
st.markdown("<div class='subtitle'>Production-Grade Fraud Detection System</div>", unsafe_allow_html=True)

# ================= SIDEBAR =================
st.sidebar.title("⚙️ Control Panel")
threshold = st.sidebar.slider("Fraud Threshold", 0.1, 0.9, 0.5)

# ================= LOAD PKL MODEL =================
@st.cache_resource
def load_model():
    with open("fast_fraud_model.pkl", "rb") as f:
        return pickle.load(f)

model = load_model()

# ================= DASHBOARD DATA =================
np.random.seed(42)
data = pd.DataFrame({
    "Amount": np.random.uniform(1, 5000, 1000),
    "Time": np.random.uniform(0, 60000, 1000),
    "Transaction_Type": np.random.randint(0, 6, 1000)
})

# ================= METRICS =================
col1, col2, col3 = st.columns(3)
col1.markdown("<div class='metric'>Transactions<br>1000</div>", unsafe_allow_html=True)
col2.markdown("<div class='metric'>Model<br>Pretrained</div>", unsafe_allow_html=True)
col3.markdown("<div class='metric'>Threshold<br>{}</div>".format(threshold), unsafe_allow_html=True)

# ================= DATA PREVIEW =================
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("📊 Sample Transactions")
st.dataframe(data.head(10), use_container_width=True)
st.markdown("</div>", unsafe_allow_html=True)

# ================= LIVE FRAUD PREDICTION =================
st.markdown("---")
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("🔍 Live Transaction Fraud Check")

c1, c2, c3 = st.columns(3)
amount = c1.number_input("Amount", 1.0, 5000.0)
time = c2.number_input("Time")
ttype = c3.selectbox("Transaction Type", [0,1,2,3,4,5])

sample = np.array([[amount, time, ttype]])
risk = float(model.predict_proba(sample)[0][1])

if risk >= threshold:
    st.error(f"🚨 FRAUD DETECTED\n\nRisk Score: {risk:.2f}")
else:
    st.success(f"✅ LEGIT TRANSACTION\n\nRisk Score: {risk:.2f}")

st.markdown("</div>", unsafe_allow_html=True)

# ================= FOOTER =================
st.markdown("---")
st.markdown("<center style='color:#aaa'>🚀 Credit Card Fraud Detection • Streamlit</center>", unsafe_allow_html=True)
