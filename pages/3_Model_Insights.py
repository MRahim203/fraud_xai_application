import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

from utils.ui_style import apply_premium_light_theme, notice
from utils.prediction import model, scaler
from explainability.feature_importance import plot_feature_importance
from explainability.lime_utils import explain_with_lime
from utils.data_manager import get_uploaded_dataset

st.set_page_config(
    page_title="Model Insights",
    page_icon="",
    layout="wide"
)

apply_premium_light_theme()

st.markdown(
    """
<div class="panel">
  <div class="kicker">Interpretability</div>
  <h1 style="margin:0;">Model Insights</h1>
  <p style="margin:0.4rem 0 0 0; line-height:1.7;">
    This section explains how the fraud detection model behaves at both global and local levels.
    Global explanations show which features influence the model overall, while local explanations
    help interpret individual transaction predictions.
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

X = clean_df.drop(columns=[fraud_col])

notice("Using dataset", f"<b>{filename}</b>")

st.markdown("## Global Feature Importance")
st.caption(
    "This chart highlights the features that contribute most strongly to the Random Forest model’s decisions overall."
)
fig_global = plot_feature_importance(model, X.columns)
st.pyplot(fig_global, clear_figure=True)

st.markdown('<div class="hr"></div>', unsafe_allow_html=True)

st.markdown("## Local Explanation")
st.caption(
    "This example uses LIME to explain a single transaction prediction from the uploaded dataset."
)

fraud_df = clean_df[clean_df[fraud_col] == 1]

if fraud_df.empty:
    st.warning("No fraudulent transactions were found in the uploaded dataset.")
else:
    row_index = int(fraud_df.index[0])
    notice("Selected example", f"Transaction index: <b>{row_index}</b>")

    lime_exp = explain_with_lime(model, scaler, X, row_index)

    st.components.v1.html(
        lime_exp.as_html(),
        height=380,
        scrolling=True
    )

st.markdown('<div class="hr"></div>', unsafe_allow_html=True)

st.markdown("## Feature Distributions")
st.caption(
    "These plots compare selected high-importance features across legitimate and fraudulent transactions."
)

features_to_plot = ["V14", "V10", "V12"]
missing_features = [feature for feature in features_to_plot if feature not in clean_df.columns]

if missing_features:
    st.warning(
        f"The uploaded dataset is missing the following required feature columns for distribution plots: {', '.join(missing_features)}."
    )
else:
    plot_df = clean_df[features_to_plot + [fraud_col]].copy()
    plot_df["Class_Label"] = plot_df[fraud_col].map({0: "Legitimate", 1: "Fraud"})

    fig, axes = plt.subplots(1, 3, figsize=(18, 5), dpi=140)
    palette = {"Legitimate": "#94A3B8", "Fraud": "#7C3AED"}

    for i, feature in enumerate(features_to_plot):
        sns.violinplot(
            data=plot_df,
            x="Class_Label",
            y=feature,
            palette=palette,
            inner="quartile",
            linewidth=1,
            ax=axes[i]
        )
        axes[i].set_title(f"{feature} Distribution", fontsize=12, pad=10)
        axes[i].set_xlabel("")
        axes[i].set_ylabel("Feature Value")
        axes[i].grid(axis="y", linestyle="--", alpha=0.15)
        axes[i].spines["top"].set_visible(False)
        axes[i].spines["right"].set_visible(False)
        axes[i].spines["left"].set_alpha(0.2)
        axes[i].spines["bottom"].set_alpha(0.2)

    plt.tight_layout()
    st.pyplot(fig)

st.markdown('<div class="hr"></div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.page_link("pages/2_Predictions.py", label="← Previous: Predictions", use_container_width=True)
with col2:
    st.page_link("pages/4_About.py", label="Next: About →", use_container_width=True)