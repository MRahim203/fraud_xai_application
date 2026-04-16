import shap
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def plot_shap_beeswarm(model, scaler, X):
    # ✅ Slice X to EXACT training shape
    X_used = X.iloc[:, :model.n_features_in_]

    # Scale using SAME scaler
    X_scaled = scaler.transform(X_used)
    X_scaled_np = np.array(X_scaled)

    # SHAP explainer
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X_scaled_np)

    # Fraud class
    shap_values_fraud = shap_values[1]

    # Static plot
    fig, ax = plt.subplots(figsize=(10, 6), dpi=150)

    shap.summary_plot(
        shap_values_fraud,
        X_used,          # ✅ MATCHING FEATURE MATRIX
        plot_type="dot",
        show=False
    )

    plt.title("SHAP Global Feature Importance (Fraud Class)")
    plt.tight_layout()

    return fig
