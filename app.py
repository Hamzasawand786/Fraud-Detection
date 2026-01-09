import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Sentinel AI | Fraud Detection",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ================= PREMIUM NEUMORPHIC / GLASS UI CSS =================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap');

    /* Global Overrides */
    html, body, [class*="css"]  {
        font-family: 'Inter', sans-serif;
    }
    
    .stApp {
        background: radial-gradient(circle at 20% 30%, #161a25 0%, #0b0d13 100%);
    }

    /* Glassmorphic Card */
    .premium-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 24px;
        padding: 2rem;
        backdrop-filter: blur(20px);
        margin-bottom: 1.5rem;
        transition: transform 0.3s ease;
    }
    
    .premium-card:hover {
        border: 1px solid rgba(0, 229, 255, 0.3);
    }

    /* Metric Styling */
    .metric-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding: 1.5rem;
        border-radius: 20px;
        background: linear-gradient(145deg, rgba(255,255,255,0.05), rgba(255,255,255,0.01));
        border: 1px solid rgba(255,255,255,0.05);
    }
    
    .metric-value {
        font-size: 2.2rem;
        font-weight: 800;
        background: linear-gradient(to right, #00e5ff, #1200ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .metric-label {
        color: #94a3b8;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        font-size: 0.75rem;
        margin-top: 0.5rem;
    }

    /* Titles */
    .main-title {
        background: linear-gradient(90deg, #ffffff, #94a3b8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3.5rem;
        font-weight: 800;
        letter-spacing: -1px;
        margin-bottom: 0;
    }
    
    /* Hide default Streamlit elements for cleaner look */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ================= SIDEBAR =================
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/1053/1053210.png", width=80)
    st.markdown("## Sentinel AI")
    st.markdown("---")
    threshold = st.slider("Sensitivity Threshold", 0.0, 1.0, 0.75, 0.05)
    st.markdown("### System Status")
    st.success("Core Engine: Online")
    st.info("Neural Engine: V4.2")

# ================= HEADER =================
st.markdown("<h1 class='main-title'>SENTINEL <span style='color:#00e5ff'>AI</span></h1>", unsafe_allow_html=True)
st.markdown("<p style='color:#64748b; font-size:1.2rem; margin-top:-10px;'>High-Performance Financial Fraud Interception</p>", unsafe_allow_html=True)

# ================= TOP METRICS =================
m1, m2, m3, m4 = st.columns(4)

metrics = [
    ("Live Transactions", "1,842", "+12%"),
    ("Flagged High Risk", "14", "⚠️"),
    ("Accuracy Rate", "99.2%", "🎯"),
    ("Engine Latency", "24ms", "⚡")
]

for i, (col, (label, val, trend)) in enumerate(zip([m1, m2, m3, m4], metrics)):
    with col:
        st.markdown(f"""
        <div class="metric-container">
            <div class="metric-value">{val}</div>
            <div class="metric-label">{label} {trend}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ================= MAIN DASHBOARD BODY =================
col_left, col_right = st.columns([2, 1])

with col_left:
    st.markdown('<div class="premium-card">', unsafe_allow_html=True)
    st.subheader("🌐 Global Transaction Stream")
    
    # Generate fancy synthetic data
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['Retail', 'Online', 'ATM']
    ).cumsum()
    
    fig = px.area(chart_data, color_discrete_sequence=['#00e5ff', '#7000ff', '#ffffff'])
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font_color="#fff",
        margin=dict(l=0, r=0, t=20, b=0),
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.05)'),
        height=350
    )
    st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col_right:
    st.markdown('<div class="premium-card">', unsafe_allow_html=True)
    st.subheader("🛡️ Live Fraud Probe")
    
    # Elegant Input Field Styling via Streamlit native
    amt = st.number_input("Transaction Value ($)", min_value=0.0, value=1250.0)
    cat = st.selectbox("Category", ["Digital Goods", "Wire Transfer", "Retail", "Travel"])
    
    # Logic
    risk = (amt / 5000) * (0.9 if cat == "Wire Transfer" else 0.4)
    
    st.markdown(f"### Risk: {risk:.1%}")
    if risk > threshold:
        st.markdown(f"""<div style="background:rgba(255,75,75,0.2); padding:15px; border-radius:12px; border:1px solid #ff4b4b; color:#ff4b4b;">
        <b>⚠️ CRITICAL ALERT</b><br>Transaction exceeds security threshold.
        </div>""", unsafe_allow_html=True)
    else:
        st.markdown(f"""<div style="background:rgba(0,255,150,0.1); padding:15px; border-radius:12px; border:1px solid #00ff96; color:#00ff96;">
        <b>✅ SECURE</b><br>Pattern matches verified user behavior.
        </div>""", unsafe_allow_html=True)
        
    st.markdown('</div>', unsafe_allow_html=True)

# ================= BOTTOM SECTION =================
st.markdown('<div class="premium-card">', unsafe_allow_html=True)
st.subheader("📋 Advanced Forensic Log")
# Simulated data with "Risk Score" coloring
df = pd.DataFrame({
    "Timestamp": ["12:01:04", "12:01:08", "12:01:15", "12:01:22"],
    "Origin": ["London, UK", "Kiev, UA", "New York, US", "San Jose, US"],
    "Amount": ["$45.00", "$4,200.00", "$120.50", "$12.99"],
    "Risk Score": [0.12, 0.88, 0.05, 0.02]
})

def color_risk(val):
    color = '#ff4b4b' if val > 0.5 else '#00ff96'
    return f'color: {color}'

st.table(df.style.applymap(color_risk, subset=['Risk Score']))
st.markdown('</div>', unsafe_allow_html=True)
