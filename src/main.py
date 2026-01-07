# src/main.py
import pandas as pd
from assets import load_assets
from threats import load_stride_threats, link_threats_to_assets
from risk_calculator import calculate_risk
from controls import suggest_controls
from visualization import plot_risk_matrix
from risk_register import generate_risk_register

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
df_risk.to_csv("outputs/risk_report.csv", index=False)

print("\n=== Risk Table ===")
print(df_risk)

# -------------------------
# Step 5: Load ISO Controls & suggest mitigations
# -------------------------
df_controls = pd.read_csv("data/ISO_controls.csv")
df_controls_suggested = suggest_controls(df_risk, df_controls)
df_controls_suggested.to_csv("outputs/controls_report.csv", index=False)

print("\n=== Suggested Controls ===")
print(df_controls_suggested)

# -------------------------
# Step 6: Visualize Risk Matrix
# -------------------------
plot_risk_matrix(df_risk)

# -------------------------
# Step 7: Generate Risk Register
# -------------------------
df_risk_register = generate_risk_register(df_risk, df_controls)
df_risk_register.to_csv("outputs/risk_register.csv", index=False)

print("\n=== Risk Register ===")
print(df_risk_register)

print("\nRiskSight analysis complete! Reports saved in 'outputs/' folder.")
