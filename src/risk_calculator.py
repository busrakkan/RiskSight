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


def classify_risk(risk_score):
    """
    Classify risk score into qualitative risk levels.
    """
    if risk_score < 20:
        return "Low"
    elif risk_score < 40:
        return "Medium"
    elif risk_score < 60:
        return "High"
    else:
        return "Critical"


def calculate_risk(df_assets, df_threats, df_capec):
    """
    Calculate risk using:
    Risk = Impact × (Feasibility × Exposure)

    Returns a prioritized risk table with qualitative risk levels.
    """
    risk_records = []

    for _, row in df_threats.iterrows():
        asset = df_assets[df_assets["Asset"] == row["Asset"]].iloc[0]
        capec = df_capec[df_capec["Threat"] == row["Threat"]].iloc[0]

        impact = calculate_impact(asset)

        exposure = asset["Exposure"]
        feasibility = capec["Feasibility"]
        likelihood = feasibility * exposure

        risk = round(impact * likelihood, 2)

        risk_records.append({
            "Asset": row["Asset"],
            "Threat": row["Threat"],
            "Impact": impact,
            "Exposure": exposure,
            "Feasibility": feasibility,
            "Likelihood": likelihood,
            "Risk": risk
        })

    df_risk = pd.DataFrame(risk_records)

    df_risk["Risk_Level"] = df_risk["Risk"].apply(classify_risk)

    df_risk = df_risk.sort_values(by="Risk", ascending=False).reset_index(drop=True)
    df_risk["Priority"] = df_risk.index + 1

    return df_risk
