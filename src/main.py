# src/main.py
import pandas as pd
from assets import load_assets
from threats import load_stride_threats, link_threats_to_assets
from risk_calculator import calculate_risk
from controls import suggest_controls
from visualization import plot_risk_matrix

# -------------------------
# Step 1: Load assets
# -------------------------
df_assets = load_assets("data/assets.csv")

# -------------------------
# Step 2: Load STRIDE threats and link to assets
# -------------------------
stride_threats = load_stride_threats("data/STRIDE_threats.csv")
df_threats = link_threats_to_assets(df_assets, stride_threats)

# -------------------------
# Step 3: Load CAPEC feasibility
# -------------------------
df_capec = pd.read_csv("data/CAPEC.csv")

# -------------------------
# Step 4: Calculate Risk
# -------------------------
df_risk = calculate_risk(df_assets, df_threats, df_capec)

# -------------------------
# Step 5: Load ISO Controls
# -------------------------
df_controls = pd.read_csv("data/ISO_controls.csv")
df_controls_suggested = suggest_controls(df_risk, df_controls)

# -------------------------
# Step 6: Visualize Risk Matrix
# -------------------------
plot_risk_matrix(df_risk)

# -------------------------
# Step 7: Save outputs
# -------------------------
df_risk.to_csv("outputs/risk_report.csv", index=False)
df_controls_suggested.to_csv("outputs/controls_report.csv", index=False)

print("=== Risk Table ===")
print(df_risk)
print("\n=== Suggested Controls ===")
print(df_controls_suggested)
print("\nRiskSight analysis complete! Reports saved in 'outputs/' folder.")
