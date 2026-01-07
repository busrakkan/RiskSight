# src/visualization.py
import matplotlib.pyplot as plt
import seaborn as sns


def plot_risk_matrix(df_risk):
    """
    Plot a risk heatmap (Impact vs Likelihood).
    """

    plt.figure(figsize=(8, 6))

    sns.scatterplot(
        data=df_risk,
        x="Likelihood",
        y="Impact",
        size="Risk",
        hue="Risk_Level",
        palette={
            "Low": "green",
            "Medium": "orange",
            "High": "red",
            "Critical": "darkred"
        },
        sizes=(100, 1000),
        legend="brief"
    )

    plt.title("Risk Matrix – Impact vs Likelihood")
    plt.xlabel("Likelihood")
    plt.ylabel("Impact")
    plt.grid(True)

    plt.tight_layout()
    plt.show()
