import streamlit as st
import pandas as pd

from utils.prediction import predict_transaction, model, scaler
from utils.ui_style import apply_premium_light_theme, notice
from explainability.lime_utils import explain_input_with_lime
from utils.data_manager import get_uploaded_dataset

st.set_page_config(
    page_title="Transaction Risk Assessment",
    page_icon="",
    layout="wide"
)
apply_premium_light_theme()

st.markdown(
    """
<div class="panel">
  <div class="kicker">Scoring</div>
  <h1 style="margin:0;">Transaction Risk Assessment</h1>
  <p style="margin:0.4rem 0 0 0; line-height:1.7;">
    Submit a transaction to generate a fraud risk estimate and an explanation of the model’s decision.
  </p>
</div>
""",
    unsafe_allow_html=True
)

st.markdown('<div class="hr"></div>', unsafe_allow_html=True)

df, fraud_col, filename = get_uploaded_dataset()

if df is None:
    st.info("Please upload a labelled fraud dataset on the Dashboard page first.")
    st.stop()

if model is None or scaler is None:
    st.warning("Model is not available in this environment because the model files are not loaded.")
    st.stop()

clean_df = df.copy()
if "Class_Label" in clean_df.columns:
    clean_df = clean_df.drop(columns=["Class_Label"])

required_cols = ["Time"] + [f"V{i}" for i in range(1, 29)] + ["Amount"]
missing_cols = [col for col in required_cols if col not in clean_df.columns]

if missing_cols:
    st.warning(
        "This dataset is not compatible with the trained fraud detection model. "
        "Required features: Time, V1–V28, Amount."
    )
    st.stop()

X_train = clean_df.drop(columns=[fraud_col])
fraud_examples = clean_df[clean_df[fraud_col] == 1].drop(columns=[fraud_col])

notice("Using dataset", f"<b>{filename}</b>")

st.markdown("### Inputs")
st.caption(
    "For manual entry, anonymised PCA features (V1–V28) are set to 0 as a simplified baseline. "
    "A real fraud example can also be loaded for a more realistic demonstration."
)

c1, c2 = st.columns(2)
with c1:
    amount = st.number_input("Transaction Amount (£)", min_value=0.0, value=100.0)
with c2:
    time = st.number_input("Transaction Time (seconds since first transaction)", min_value=0.0, value=0.0)

manual_input = {"Time": time}
for i in range(1, 29):
    manual_input[f"V{i}"] = 0.0
manual_input["Amount"] = amount

manual_df = pd.DataFrame([manual_input])

st.markdown("")

b1, b2 = st.columns(2)
with b1:
    run_manual = st.button("Run Risk Assessment", use_container_width=True)
with b2:
    load_example = st.button("Use Example Fraud Transaction", use_container_width=True)

st.markdown('<div class="hr"></div>', unsafe_allow_html=True)
st.markdown("### Result")


def render_result(prediction, probability, title_text):
    if probability >= 0.80:
        risk = "High"
        rec = "Manual review required"
    elif probability >= 0.50:
        risk = "Medium"
        rec = "Review recommended"
    else:
        risk = "Low"
        rec = "Approve with monitoring"

    notice(
        title_text,
        f"Fraud probability: <b>{probability:.2%}</b><br>"
        f"Risk level: <b>{risk}</b><br>"
        f"Recommendation: <b>{rec}</b>"
    )


if run_manual:
    prediction, probability = predict_transaction(manual_df)
    render_result(prediction, probability, "Risk Assessment Output")

    st.caption(
        "This result is based on a simplified input profile. Since V1–V28 are fixed to zero, "
        "the prediction is primarily influenced by amount and time."
    )

    st.markdown('<div class="hr"></div>', unsafe_allow_html=True)
    st.markdown("## Why this prediction was made")

    lime_exp = explain_input_with_lime(model, scaler, X_train, manual_df, num_features=8)
    st.components.v1.html(lime_exp.as_html(), height=420, scrolling=True)

if load_example:
    if fraud_examples.empty:
        st.warning("No fraudulent transactions were found in the uploaded dataset.")
    else:
        example_row = fraud_examples.iloc[[0]].copy()

        prediction, probability = predict_transaction(example_row)
        render_result(prediction, probability, "Example Fraud Transaction")

        with st.expander("View example transaction values"):
            st.dataframe(example_row, use_container_width=True)

        st.markdown('<div class="hr"></div>', unsafe_allow_html=True)
        st.markdown("## Why this prediction was made")

        lime_exp = explain_input_with_lime(model, scaler, X_train, example_row, num_features=8)
        st.components.v1.html(lime_exp.as_html(), height=420, scrolling=True)

st.markdown('<div class="hr"></div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.page_link("pages/1_Dashboard.py", label="← Previous: Dashboard", use_container_width=True)
with col2:
    st.page_link("pages/3_Model_Insights.py", label="Next: Model Insights →", use_container_width=True)