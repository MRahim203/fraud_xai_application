import matplotlib.pyplot as plt
import pandas as pd


def plot_feature_importance(model, feature_names, top_n=10):
    importances = model.feature_importances_
    feature_names = list(feature_names)

    min_len = min(len(feature_names), len(importances))
    feature_names = feature_names[:min_len]
    importances = importances[:min_len]

    fi_df = pd.DataFrame({
        "Feature": feature_names,
        "Importance": importances
    }).sort_values("Importance", ascending=False).head(top_n)

    fig, ax = plt.subplots(figsize=(9, 5), dpi=150)

    bars = ax.barh(
        fi_df["Feature"][::-1],
        fi_df["Importance"][::-1],
        color="#7C3AED",
        alpha=0.9
    )

    ax.set_title("Global Feature Importance", fontsize=14, pad=12)
    ax.set_xlabel("Importance Score")
    ax.set_ylabel("")

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.grid(axis="x", linestyle="--", alpha=0.2)

    for bar in bars:
        width = bar.get_width()
        ax.text(
            width + 0.001,
            bar.get_y() + bar.get_height() / 2,
            f"{width:.3f}",
            va="center",
            fontsize=9
        )

    plt.tight_layout()
    return fig