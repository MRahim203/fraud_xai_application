import streamlit as st
import pandas as pd
import plotly.express as px

from utils.ui_style import apply_premium_light_theme, notice
from utils.data_manager import save_uploaded_dataset, get_uploaded_dataset, clear_uploaded_dataset

st.set_page_config(
    page_title="Fraud Overview Dashboard",
    page_icon="",
    layout="wide"
)
apply_premium_light_theme()


def style_plotly(fig):
    fig.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(
            family="Arial",
            size=14,
            color="#111827"
        ),
        margin=dict(l=20, r=20, t=20, b=20),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
            title=None
        )
    )
    fig.update_xaxes(showgrid=False, zeroline=False)
    fig.update_yaxes(showgrid=True, gridcolor="rgba(17,24,39,0.08)", zeroline=False)
    return fig


st.markdown(
    """
<div class="panel">
  <div class="kicker">Analytics</div>
  <h1 style="margin:0;">Fraud Overview Dashboard</h1>
  <p style="margin:0.4rem 0 0 0; line-height:1.7;">
    Upload a labelled fraud dataset (CSV). The dataset will then be used across the
    Dashboard, Predictions, and Model Insights pages.
  </p>
</div>
""",
    unsafe_allow_html=True
)

st.markdown('<div class="hr"></div>', unsafe_allow_html=True)

uploaded_file = st.file_uploader("Upload dataset (CSV)", type=["csv"])

if uploaded_file is not None:
    df_saved, error = save_uploaded_dataset(uploaded_file)
    if error:
        st.error(error)
        st.stop()

df, fraud_col, filename = get_uploaded_dataset()

if df is None:
    notice(
        "Upload required",
        "Please upload a labelled fraud dataset to continue. Supported label columns include: "
        "<b>Class</b>, <b>fraud</b>, <b>is_fraud</b>, <b>label</b>, <b>target</b>."
    )
    st.stop()

top_left, top_right = st.columns([4, 1])
with top_left:
    notice(
        "Dataset loaded",
        f"File: <b>{filename}</b><br>"
        f"Rows: <b>{df.shape[0]:,}</b> • Columns: <b>{df.shape[1]:,}</b><br>"
        f"Detected label: <b>{fraud_col}</b>"
    )
with top_right:
    if st.button("Clear dataset", use_container_width=True):
        clear_uploaded_dataset()
        st.rerun()

st.markdown("### Preview")
st.dataframe(df.head(), use_container_width=True)

st.markdown('<div class="hr"></div>', unsafe_allow_html=True)

numeric_cols = df.select_dtypes(include="number").columns.tolist()
numeric_cols = [c for c in numeric_cols if c != fraud_col]

if not numeric_cols:
    notice(
        "No numeric features found",
        "This dataset does not contain numeric columns suitable for analysis."
    )
    st.stop()

if "amount" in [c.lower() for c in numeric_cols]:
    amount_col = [c for c in numeric_cols if c.lower() == "amount"][0]
else:
    amount_col = numeric_cols[0]

chart_df = df.copy()
chart_df["Class_Label"] = chart_df[fraud_col].map({0: "Legitimate", 1: "Fraud"})

class_counts = chart_df["Class_Label"].value_counts().reset_index()
class_counts.columns = ["Class", "Count"]

st.markdown("## Summary")

c1, c2, c3 = st.columns(3)
with c1:
    st.metric("Total Transactions", f"{len(df):,}")
with c2:
    st.metric("Fraud Cases", f"{int(df[fraud_col].sum()):,}")
with c3:
    st.metric("Fraud Rate", f"{(df[fraud_col].mean() * 100):.2f}%")

st.caption(
    "The dataset is highly imbalanced if the fraud rate is very low, which makes fraud detection more challenging."
)

st.markdown('<div class="hr"></div>', unsafe_allow_html=True)

left, right = st.columns([1, 1])

with left:
    st.markdown("## Transaction Class Distribution")
    st.caption("Shows the proportion of legitimate and fraudulent transactions in the uploaded dataset.")

    pie_fig = px.pie(
        class_counts,
        names="Class",
        values="Count",
        hole=0.62,
        color="Class",
        color_discrete_map={
            "Legitimate": "#94A3B8",
            "Fraud": "#7C3AED"
        }
    )
    pie_fig.update_traces(
        textposition="inside",
        textinfo="percent+label",
        marker=dict(line=dict(color="white", width=2))
    )
    st.plotly_chart(style_plotly(pie_fig), use_container_width=True)

with right:
    st.markdown("## Transaction Amount by Class")
    st.caption("Compares the spread of transaction amounts between legitimate and fraudulent transactions.")

    box_fig = px.box(
        chart_df,
        x="Class_Label",
        y=amount_col,
        color="Class_Label",
        labels={"Class_Label": "Transaction Class", amount_col: "Transaction Amount"},
        color_discrete_map={
            "Legitimate": "#94A3B8",
            "Fraud": "#7C3AED"
        }
    )
    st.plotly_chart(style_plotly(box_fig), use_container_width=True)

st.markdown('<div class="hr"></div>', unsafe_allow_html=True)

st.markdown("## Transaction Amount Distribution")
st.caption("Displays how transaction values are distributed across legitimate and fraudulent classes.")

hist_fig = px.histogram(
    chart_df,
    x=amount_col,
    color="Class_Label",
    nbins=50,
    log_y=True,
    labels={amount_col: "Transaction Amount"},
    color_discrete_map={
        "Legitimate": "#94A3B8",
        "Fraud": "#7C3AED"
    },
    opacity=0.78
)
st.plotly_chart(style_plotly(hist_fig), use_container_width=True)

st.markdown('<div class="hr"></div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.page_link("app.py", label="← Previous: Home", use_container_width=True)
with col2:
    st.page_link("pages/2_Predictions.py", label="Next: Predictions →", use_container_width=True)

st.markdown('<div class="hr"></div>', unsafe_allow_html=True)

notice(
    "Disclaimer",
    "This dashboard adapts to the uploaded dataset. Outputs depend on the dataset’s structure and quality."
)