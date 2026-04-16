import streamlit as st

st.set_page_config(
    page_title="Explainable Fraud Risk Assessment",
    page_icon="",
    layout="wide"
)

# ---------------- PREMIUM LIGHT THEME ----------------
st.markdown(
    """
<style>
:root{
  --bg:#f6f7fb;
  --card:#ffffff;
  --muted:#5b6475;
  --text:#111827;
  --border:rgba(17,24,39,0.10);
  --shadow: 0 14px 35px rgba(17,24,39,0.08);
  --shadow2: 0 8px 20px rgba(17,24,39,0.06);
  --accent:#5b6cff;         /* subtle blue-violet */
  --accent2:#8b5cf6;        /* soft purple */
}

/* Background */
.stApp{
  background:
    radial-gradient(900px 600px at 15% 10%, rgba(91,108,255,0.16), transparent 60%),
    radial-gradient(800px 520px at 85% 18%, rgba(139,92,246,0.12), transparent 55%),
    radial-gradient(700px 500px at 50% 95%, rgba(15,118,110,0.06), transparent 55%),
    var(--bg);
  color: var(--text);
}

/* Typography */
html, body, [class*="css"]{
  font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Arial;
}
h1,h2,h3{
  letter-spacing:-0.03em;
  color: var(--text);
}
p, li, span, label{
  color: var(--muted);
}

/* Container padding */
.block-container{
  padding-top: 2.2rem;
  padding-bottom: 2.2rem;
  max-width: 1200px;
}

/* Sidebar polish */
section[data-testid="stSidebar"]{
  background: rgba(255,255,255,0.7);
  backdrop-filter: blur(10px);
  border-right: 1px solid var(--border);
}

/* Panels / cards */
.panel{
  background: rgba(255,255,255,0.72);
  backdrop-filter: blur(10px);
  border: 1px solid var(--border);
  border-radius: 22px;
  padding: 1.6rem 1.6rem;
  box-shadow: var(--shadow2);
}

.card{
  background: rgba(255,255,255,0.82);
  backdrop-filter: blur(10px);
  border: 1px solid var(--border);
  border-radius: 20px;
  padding: 1.25rem 1.25rem;
  box-shadow: var(--shadow2);
  transition: transform .18s ease, box-shadow .18s ease;
}
.card:hover{
  transform: translateY(-4px);
  box-shadow: var(--shadow);
}

.kicker{
  color: var(--muted);
  font-size: 0.95rem;
  margin-bottom: 0.4rem;
}

.title{
  font-size: 2.6rem;
  margin: 0;
  line-height: 1.1;
}

.subtitle{
  color: var(--muted);
  font-size: 1.05rem;
  margin-top: 0.55rem;
  line-height: 1.55;
}

/* Accent underline */
.accent-line{
  height: 2px;
  width: 76px;
  border-radius: 999px;
  background: linear-gradient(90deg, var(--accent), var(--accent2));
  margin-top: 0.9rem;
}

/* Divider */
.hr{
  height: 1px;
  background: rgba(17,24,39,0.08);
  margin: 1.4rem 0 1.8rem 0;
}

/* Buttons */
.stButton > button{
  border-radius: 14px;
  border: 1px solid rgba(17,24,39,0.14);
  padding: 0.65rem 1rem;
  background: rgba(255,255,255,0.9);
}
.stButton > button:hover{
  border: 1px solid rgba(91,108,255,0.35);
}

/* Make headers look less “Streamlit default” */
[data-testid="stMarkdownContainer"] h2{
  margin-top: 0.2rem;
}

/* Remove extra top padding of Streamlit header area */
header[data-testid="stHeader"]{
  background: transparent;
}
</style>
""",
    unsafe_allow_html=True
)

# ---------------- HERO ----------------
st.markdown(
    """
<div class="panel">
  <div class="kicker">Explainable AI • Decision Support</div>
  <h1 class="title">Fraud Risk Assessment</h1>
  <div class="subtitle">
    A clean, analyst-friendly interface for fraud prediction and interpretability. Built to support decision-making,
    with transparent reasoning rather than black-box outputs.
  </div>
  <div class="accent-line"></div>
</div>
""",
    unsafe_allow_html=True
)

st.markdown('<div class="hr"></div>', unsafe_allow_html=True)

# ---------------- SYSTEM SUMMARY ----------------
st.markdown(
    """
<div class="panel">
  <p style="font-size:1.08rem; line-height:1.75; margin:0;">
    This system demonstrates how machine learning can be applied to detect potentially fraudulent financial transactions
    while maintaining <b>transparency</b> and <b>interpretability</b>. It integrates explainability techniques
    (such as feature importance and local explanations) to help users understand <b>why</b> a transaction may be flagged,
    not only whether it is flagged.
  </p>
</div>
""",
    unsafe_allow_html=True
)

st.markdown('<div class="hr"></div>', unsafe_allow_html=True)

# ---------------- CAPABILITIES ----------------
st.markdown("## System Modules")
st.caption("Select a module to explore analytics, scoring, and explainability.")

c1, c2 = st.columns(2)
c3, c4 = st.columns(2)

with c1:
    st.markdown(
        """
        <div class="card">
          <div class="kicker">Analytics</div>
          <h3 style="margin:0 0 .4rem 0;">Dashboard</h3>
          <p style="margin:0;">Explore dataset statistics, fraud rate, and transaction patterns using charts and summaries.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with c2:
    st.markdown(
        """
        <div class="card">
          <div class="kicker">Scoring</div>
          <h3 style="margin:0 0 .4rem 0;">Predictions</h3>
          <p style="margin:0;">Run risk assessments on individual transactions using the trained model.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with c3:
    st.markdown(
        """
        <div class="card">
          <div class="kicker">Interpretability</div>
          <h3 style="margin:0 0 .4rem 0;">Model Insights</h3>
          <p style="margin:0;">Review feature importance and local explanations to understand model decisions.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with c4:
    st.markdown(
        """
        <div class="card">
          <div class="kicker">Governance</div>
          <h3 style="margin:0 0 .4rem 0;">Dataset & Ethics</h3>
          <p style="margin:0;">Understand data limitations, risks, and responsible use considerations.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown('<div class="hr"></div>', unsafe_allow_html=True)

# ---------------- NAVIGATION ----------------
st.markdown("## Navigate")

n1, n2 = st.columns(2)
n3, n4 = st.columns(2)

with n1:
    st.markdown("### Dashboard")
    st.write("View overall statistics and fraud trends.")
    if st.button("Open Dashboard", use_container_width=True):
        st.switch_page("pages/1_Dashboard.py")

with n2:
    st.markdown("### Predictions")
    st.write("Assess transaction risk using the trained model.")
    if st.button("Open Predictions", use_container_width=True):
        st.switch_page("pages/2_Predictions.py")

with n3:
    st.markdown("### Model Insights")
    st.write("Understand how the model reaches decisions.")
    if st.button("Open Model Insights", use_container_width=True):
        st.switch_page("pages/3_Model_Insights.py")

with n4:
    st.markdown("### Dataset & Ethics")
    st.write("Learn about dataset constraints and ethical considerations.")
    if st.button("Open Dataset & Ethics", use_container_width=True):
        st.switch_page("pages/4_About.py")

st.markdown('<div class="hr"></div>', unsafe_allow_html=True)

# ---------------- NOTICE ----------------
st.markdown(
    """
<div class="panel">
  <div class="kicker">Notice</div>
  <p style="margin:0; line-height:1.75;">
    The <b>Predictions</b> and <b>Model Insights</b> modules require a compatible transaction dataset and trained model artifacts.
    This system is intended as decision support; outputs should be reviewed alongside additional context.
  </p>
</div>
""",
    unsafe_allow_html=True
)
