import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.metrics import confusion_matrix, classification_report, roc_auc_score

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Credit Card Fraud Detection",
    page_icon="💳",
    layout="wide"
)

# ================= HIGH-END CSS =================
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
st.markdown("<div class='subtitle'>Enterprise-Grade ML Fraud Detection Dashboard</div>", unsafe_allow_html=True)

# ================= SIDEBAR =================
st.sidebar.title("⚙️ Control Panel")
threshold = st.sidebar.slider("Fraud Threshold", 0.1, 0.9, 0.5)
upload = st.sidebar.file_uploader("📂 Upload CSV Dataset", type=["csv"])

# ================= LOAD MODEL =================
@st.cache_resource
def load_model():
    with open("fast_fraud_model.pkl", "rb") as f:
        return pickle.load(f)

model = load_model()

# ================= DATASET =================
if upload:
    data = pd.read_csv(upload)
else:
    np.random.seed(42)
    data = pd.DataFrame({
        "Amount": np.random.uniform(1, 5000, 2000),
        "Time": np.random.uniform(0, 60000, 2000),
        "Transaction_Type": np.random.randint(0, 6, 2000),
        "Fraud": np.random.randint(0, 2, 2000)
    })

# ================= DASHBOARD =================
col1, col2 = st.columns([1.4, 1])

with col1:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("📊 Dataset Preview")
    st.dataframe(data.head(10), use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("📈 Key Metrics")

    total = len(data)
    fraud = data["Fraud"].sum()
    legit = total - fraud

    m1, m2, m3 = st.columns(3)
    m1.markdown(f"<div class='metric'>Total<br>{total}</div>", unsafe_allow_html=True)
    m2.markdown(f"<div class='metric'>Fraud<br>{fraud}</div>", unsafe_allow_html=True)
    m3.markdown(f"<div class='metric'>Legit<br>{legit}</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# ================= MODEL EVALUATION =================
st.markdown("---")
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("🤖 Model Evaluation")

X = data.drop("Fraud", axis=1)
y = data["Fraud"]

probs = model.predict_proba(X)[:, 1]
y_pred = (probs >= threshold).astype(int)

st.code(classification_report(y, y_pred))

cm = confusion_matrix(y, y_pred)
st.subheader("Confusion Matrix")
st.dataframe(pd.DataFrame(cm, 
    columns=["Predicted Legit", "Predicted Fraud"],
    index=["Actual Legit", "Actual Fraud"]
))

auc_score = roc_auc_score(y, probs)
st.metric("ROC AUC Score", f"{auc_score:.3f}")

st.markdown("</div>", unsafe_allow_html=True)

# ================= LIVE PREDICTION =================
st.markdown("---")
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("🔍 Live Transaction Fraud Check")

c1, c2, c3 = st.columns(3)
amount = c1.number_input("Amount", 1.0, 5000.0)
time = c2.number_input("Time")
ttype = c3.selectbox("Transaction Type", [0,1,2,3,4,5])

sample = np.array([[amount, time, ttype]])
risk = model.predict_proba(sample)[0][1]

if risk >= threshold:
    st.error(f"🚨 FRAUD DETECTED — Risk Score: {risk:.2f}")
else:
    st.success(f"✅ Legit Transaction — Risk Score: {risk:.2f}")

st.markdown("</div>", unsafe_allow_html=True)

# ================= FOOTER =================
st.markdown("---")
st.markdown("<center style='color:#aaa'>🚀 Streamlit • Credit Card Fraud Detection System</center>", unsafe_allow_html=True)
