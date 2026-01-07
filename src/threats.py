# src/threats.py
import pandas as pd
import random

STRIDE_CATEGORIES = [
    "Spoofing", "Tampering", "Repudiation", 
    "Information Disclosure", "Denial of Service", "Elevation of Privilege"
]

def link_threats_to_assets(df_assets):
    """
    For each asset, assign 1-3 random STRIDE threats.
    """
    asset_threats = []
    for _, row in df_assets.iterrows():
        threats = random.sample(STRIDE_CATEGORIES, k=random.randint(1,3))
        for threat in threats:
            asset_threats.append({
                "Asset": row["Asset"],
                "Threat": threat
            })
    
    df_threats = pd.DataFrame(asset_threats)
    return df_threats

if __name__ == "__main__":
    from assets import generate_assets
    df_assets = generate_assets()
    df_threats = link_threats_to_assets(df_assets)
    print(df_threats)
