import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, roc_curve, auc

# ================= Page Config =================
st.set_page_config(
    page_title="Credit Card Fraud Detection",
    page_icon="💳",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ================= Custom CSS (High-End) =================
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
}
.main-title {
    font-size: 3.2rem;
    font-weight: 900;
    color: #00e5ff;
    text-align: center;
}
.subtitle {
    text-align: center;
    font-size: 1.2rem;
    color: #cccccc;
    margin-bottom: 2rem;
}
.card {
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(12px);
    border-radius: 22px;
    padding: 1.6rem;
    box-shadow: 0 10px 40px rgba(0,0,0,0.35);
}
.metric-card {
    background: linear-gradient(135deg, #00c6ff, #0072ff);
    border-radius: 18px;
    padding: 1.4rem;
    text-align: center;
    color: white;
    font-weight: 700;
    box-shadow: 0 10px 30px rgba(0,0,0,0.4);
}
</style>
""", unsafe_allow_html=True)

# ================= Header =================
st.markdown("<div class='main-title'>💳 Credit Card Fraud Detection</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Enterprise-Grade ML Dashboard for Fraud Analysis</div>", unsafe_allow_html=True)

# ================= Sidebar =================
st.sidebar.title("⚙️ Control Center")
model_choice = st.sidebar.selectbox("ML Model", ["Random Forest", "Logistic Regression"])
test_size = st.sidebar.slider("Test Size", 0.1, 0.4, 0.25)
threshold = st.sidebar.slider("Fraud Threshold", 0.1, 0.9, 0.5)
upload = st.sidebar.file_uploader("📂 Upload CSV Dataset", type=["csv"])
train_btn = st.sidebar.button("🚀 Train Model")

# ================= Dataset =================
if upload:
    data = pd.read_csv(upload)
else:
    np.random.seed(42)
    data = pd.DataFrame({
        "Amount": np.random.uniform(1, 2000, 2000),
        "Time": np.random.uniform(0, 60000, 2000),
        "Transaction_Type": np.random.randint(0, 6, 2000),
        "Fraud": np.random.randint(0, 2, 2000)
    })

# ================= Dashboard =================
col1, col2 = st.columns([1.3, 1])

with col1:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("📊 Dataset Overview")
    st.dataframe(data.head(15), use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("📈 Key Metrics")

    total = len(data)
    fraud = data['Fraud'].sum()
    legit = total - fraud

    m1, m2, m3 = st.columns(3)
    with m1:
        st.markdown(f"<div class='metric-card'>Total<br>{total}</div>", unsafe_allow_html=True)
    with m2:
        st.markdown(f"<div class='metric-card'>Fraud<br>{fraud}</div>", unsafe_allow_html=True)
    with m3:
        st.markdown(f"<div class='metric-card'>Legit<br>{legit}</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# ================= Model Training =================
st.markdown("---")
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("🤖 Model Evaluation")

if train_btn:
    X = data.drop("Fraud", axis=1)
    y = data["Fraud"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)

    # Load Pretrained PKL Model instead of training
    import pickle
    with open('fast_fraud_model.pkl', 'rb') as f:
        model = pickle.load(f)

    model.fit(X_train, y_train)
    probs = model.predict_proba(X_test)[:, 1]
    y_pred = (probs >= threshold).astype(int)

    st.success("Model Trained Successfully")
    st.code(classification_report(y_test, y_pred))

    # Confusion Matrix
    cm = confusion_matrix(y_test, y_pred)
    fig, ax = plt.subplots()
    ax.imshow(cm)
    ax.set_title("Confusion Matrix")
    st.pyplot(fig)

    # ROC Curve
    fpr, tpr, _ = roc_curve(y_test, probs)
    roc_auc = auc(fpr, tpr)
    fig2, ax2 = plt.subplots()
    ax2.plot(fpr, tpr, label=f"AUC = {roc_auc:.2f}")
    ax2.plot([0,1],[0,1], linestyle='--')
    ax2.legend()
    ax2.set_title("ROC Curve")
    st.pyplot(fig2)
else:
    st.info("Click Train Model to begin analysis")

st.markdown("</div>", unsafe_allow_html=True)

# ================= Live Prediction =================
st.markdown("---")
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("🔍 Live Transaction Fraud Check")

c1, c2, c3 = st.columns(3)
amount = c1.number_input("Amount", 1.0, 5000.0)
time = c2.number_input("Time")
ttype = c3.selectbox("Transaction Type", [0,1,2,3,4,5])

if train_btn:
    sample = np.array([[amount, time, ttype]])
    prob = model.predict_proba(sample)[0][1]
    if prob >= threshold:
        st.error(f"🚨 FRAUD DETECTED (Risk: {prob:.2f})")
    else:
        st.success(f"✅ Legit Transaction (Risk: {prob:.2f})")

st.markdown("</div>", unsafe_allow_html=True)

# ================= Footer =================
st.markdown("---")
st.markdown("<center>🚀 FinTech‑Grade Fraud Detection System | Streamlit + ML</center>", unsafe_allow_html=True)
