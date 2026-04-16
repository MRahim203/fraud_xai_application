import streamlit as st
import pandas as pd

POSSIBLE_LABELS = [
    "class", "fraud", "is_fraud", "isfraud", "label", "target", "isflaggedfraud"
]


def detect_label_column(df: pd.DataFrame):
    for col in df.columns:
        if col.lower() in POSSIBLE_LABELS:
            return col
    return None


def save_uploaded_dataset(uploaded_file):
    df = pd.read_csv(uploaded_file)
    fraud_col = detect_label_column(df)

    if fraud_col is None:
        return None, "No recognised fraud label column was found."

    if df[fraud_col].nunique() != 2:
        return None, f"The detected label column '{fraud_col}' is not binary."

    st.session_state["uploaded_df"] = df.copy()
    st.session_state["fraud_col"] = fraud_col
    st.session_state["uploaded_filename"] = uploaded_file.name

    return df.copy(), None


def get_uploaded_dataset():
    df = st.session_state.get("uploaded_df")
    fraud_col = st.session_state.get("fraud_col")
    filename = st.session_state.get("uploaded_filename")

    if df is None or fraud_col is None:
        return None, None, None

    return df.copy(), fraud_col, filename


def clear_uploaded_dataset():
    for key in ["uploaded_df", "fraud_col", "uploaded_filename"]:
        if key in st.session_state:
            del st.session_state[key]