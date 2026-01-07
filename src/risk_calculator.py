# src/risk_calculator.py
import pandas as pd

def calculate_risk(df_assets, df_threats, df_capec):
    """
    Calculate risk for each asset-threat pair.
    Risk = (Sum of CIA scores) * Feasibility
    """
    risk_data = []
    
    for _, threat_row in df_threats.iterrows():
        asset_row = df_assets[df_assets["Asset"] == threat_row["Asset"]].iloc[0]
        # Sum CIA scores as a simple impact measure
        impact = asset_row["Confidentiality"] + asset_row["Integrity"] + asset_row["Availability"]
        
        # Get feasibility from CAPEC.csv
        capec_entry = df_capec[df_capec["Threat"] == threat_row["Threat"]]
        if not capec_entry.empty:
            feasibility = int(capec_entry.iloc[0]["Feasibility"])
        else:
            feasibility = 3  # default if not found
        
        risk_score = impact * feasibility
        risk_data.append({
            "Asset": threat_row["Asset"],
            "Threat": threat_row["Threat"],
            "Impact": impact,
            "Feasibility": feasibility,
            "Risk": risk_score
        })
    
    df_risk = pd.DataFrame(risk_data)
    return df_risk

if __name__ == "__main__":
    from assets import generate_assets
    from threats import link_threats_to_assets
    
    df_assets = generate_assets()
    df_threats = link_threats_to_assets(df_assets)
    
    # Example CAPEC CSV structure
    df_capec = pd.DataFrame({
        "Threat": ["Spoofing","Tampering","Repudiation","Information Disclosure","Denial of Service","Elevation of Privilege"],
        "Feasibility": [3,4,2,5,3,4]
    })
    
    df_risk = calculate_risk(df_assets, df_threats, df_capec)
    print(df_risk)
