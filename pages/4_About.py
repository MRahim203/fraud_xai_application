import streamlit as st
from utils.ui_style import apply_premium_light_theme, notice

st.set_page_config(
    page_title="About & Ethics",
    page_icon="",
    layout="wide"
)

apply_premium_light_theme()

st.markdown(
    """
<div class="panel">
  <div class="kicker">Project Context</div>
  <h1 style="margin:0;">About & Ethics</h1>
  <p style="margin:0.4rem 0 0 0; line-height:1.7;">
    This project investigates the use of Explainable Artificial Intelligence (XAI)
    for fraud detection, with a focus on transparency, interpretability, and responsible
    decision support.
  </p>
</div>
""",
    unsafe_allow_html=True
)

st.markdown('<div class="hr"></div>', unsafe_allow_html=True)

st.markdown(
    """
<div class="card">
  <div class="kicker">Project Overview</div>
  <p style="margin:0; line-height:1.75;">
    The system was developed as part of an academic dissertation exploring how machine learning
    can support fraud detection while remaining interpretable to human users.
    Instead of producing only a classification output, the application also provides explanations
    to help users understand the reasoning behind model decisions.
  </p>
</div>
""",
    unsafe_allow_html=True
)

st.markdown("")

st.markdown(
    """
<div class="card">
  <div class="kicker">Technology Stack</div>
  <ul style="margin:0.2rem 0 0 1.2rem; line-height:1.8;">
    <li>Python</li>
    <li>Streamlit</li>
    <li>Scikit-learn</li>
    <li>LIME for local explanations</li>
    <li>Feature importance for global model behaviour</li>
  </ul>
</div>
""",
    unsafe_allow_html=True
)

st.markdown("")

st.markdown(
    """
<div class="card">
  <div class="kicker">Ethical Considerations</div>
  <p style="margin:0; line-height:1.75;">
    Fraud detection systems can create false positives, which may inconvenience legitimate users,
    and false negatives, which may allow harmful activity to go undetected. For this reason, the
    model should be treated as a decision-support tool rather than a replacement for human judgement.
  </p>
  <p style="margin:0.8rem 0 0 0; line-height:1.75;">
    The quality of outputs also depends on dataset quality, class balance, and the extent to which
    the training data reflects real-world fraud patterns. Model explanations improve transparency,
    but they do not remove all limitations or risks.
  </p>
</div>
""",
    unsafe_allow_html=True
)

st.markdown("")

notice(
    "Responsible Use",
    "This application is designed for academic demonstration and decision support. "
    "Predictions and explanations should always be interpreted alongside domain knowledge, "
    "data quality checks, and human review."
)

st.markdown('<div class="hr"></div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.page_link("pages/3_Model_Insights.py", label="← Previous: Model Insights", use_container_width=True)
with col2:
    st.page_link("app.py", label="Next: Home →", use_container_width=True)