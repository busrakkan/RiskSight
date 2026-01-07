# src/visualization.py
import matplotlib.pyplot as plt

def plot_risk_matrix(df_risk):
    """
    Create a scatter plot of Risk vs Impact and Feasibility.
    """
    plt.figure(figsize=(8,6))
    scatter = plt.scatter(df_risk["Feasibility"], df_risk["Impact"], 
                          c=df_risk["Risk"], cmap="Reds", s=100)
    plt.colorbar(scatter, label="Risk Score")
    plt.xlabel("Feasibility")
    plt.ylabel("Impact (CIA Sum)")
    plt.title("RiskSight: Risk Matrix")
    for i, row in df_risk.iterrows():
        plt.text(row["Feasibility"]+0.05, row["Impact"]+0.05, row["Asset"], fontsize=8)
    plt.grid(True)
    plt.show()
