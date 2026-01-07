# src/main.py
from assets import generate_assets
from threats import link_threats_to_assets
from risk_calculator import calculate_risk
from controls import suggest_controls
from visualization import plot_risk_matrix
import pandas as pd

# Step 1: Generate Assets
df_assets = generate_assets()

# Step 2: Link STRIDE Threats
df_threats = link_threats_to_assets(df_assets)

# Step 3: Load CAPEC feasibility scores
df_capec = pd.DataFrame({
    "Threat": ["Spoofing","Tampering","Repudiation","Information Disclosure","Denial of Service","Elevation of Privilege"],
    "Feasibility": [3,4,2,5,3,4]
})

# Step 4: Calculate Risk
df_risk = calculate_risk(df_assets, df_threats, df_capec)

# Step 5: Load ISO Controls
df_controls = pd.DataFrame({
    "Threat":["Spoofing","Tampering","Repudiation","Information Disclosure","Denial of Service","Elevation of Privilege"],
    "ISO_Control":["ISO 27001 A.9","ISO 27001 A.12.1","ISO 27001 A.10","ISO 27001 A.13","ISO 27001 A.14","ISO 27001 A.9.4"],
    "Description":["Access control","Change management","Logging","Data encryption","DoS mitigation","Privilege management"]
})

# Step 6: Suggest Controls
df_controls_suggested = suggest_controls(df_risk, df_controls)

# Step 7: Visualize Risk Matrix
plot_risk_matrix(df_risk)

# Step 8: Save outputs
df_risk.to_csv("outputs/risk_report.csv", index=False)
df_controls_suggested.to_csv("outputs/controls_report.csv", index=False)

print("RiskSight analysis complete! Reports saved in 'outputs/' folder.")
