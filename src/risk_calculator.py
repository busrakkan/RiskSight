# src/risk_calculator.py
import pandas as pd

CIA_WEIGHTS = {
    "Confidentiality": 0.4,
    "Integrity": 0.3,
    "Availability": 0.3
}

def calculate_impact(asset_row):
    """
    Calculate weighted CIA impact.
    """
    impact = (
        asset_row["Confidentiality"] * CIA_WEIGHTS["Confidentiality"] +
        asset_row["Integrity"] * CIA_WEIGHTS["Integrity"] +
        asset_row["Availability"] * CIA_WEIGHTS["Availability"]
    )
    return round(impact, 2)

def calculate_risk(df_assets, df_threats, df_capec):
    """
    Calculate risk using:
    Impact × (Feasibility × Exposure)
    """
    risk_records = []

    for _, row in df_threats.iterrows():
        asset = df_assets[df_assets["Asset"] == row["Asset"]].iloc[0]
        capec = df_capec[df_capec["Threat"] == row["Threat"]].iloc[0]

        impact = calculate_impact(asset)
        likelihood = capec["Feasibility"] * asset["Exposure"]
        risk = impact * likelihood

        risk_records.append({
            "Asset": row["Asset"],
            "Threat": row["Threat"],
            "Impact": impact,
            "Exposure": asset["Exposure"],
            "Feasibility": capec["Feasibility"],
            "Likelihood": likelihood,
            "Risk": round(risk, 2)
        })

    return pd.DataFrame(risk_records)
