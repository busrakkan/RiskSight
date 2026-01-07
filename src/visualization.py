import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st  # needed to render plots in Streamlit

def plot_risk_matrix(df_risk):
    fig, ax = plt.subplots(figsize=(8, 6))

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
        legend="brief",
        ax=ax
    )

    ax.set_title("Risk Matrix – Impact vs Likelihood")
    ax.set_xlabel("Likelihood")
    ax.set_ylabel("Impact")
    ax.grid(True)

    st.pyplot(fig)  # <-- render in Streamlit
    plt.close(fig)  # clean up

def plot_top_risks(df_risk, top_n=10):
    top_risks = df_risk.head(top_n)
    fig, ax = plt.subplots(figsize=(10, 5))

    ax.barh(
        top_risks["Asset"] + " - " + top_risks["Threat"],
        top_risks["Risk"]
    )

    ax.set_xlabel("Risk Score")
    ax.set_title(f"Top {top_n} Cyber Risks")
    ax.invert_yaxis()
    plt.tight_layout()

    st.pyplot(fig)  # <-- render in Streamlit
    plt.close(fig)
