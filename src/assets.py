# src/assets.py
import pandas as pd
import random

def generate_assets():
    """
    Generate a list of assets with random CIA (Confidentiality, Integrity, Availability) scores.
    """
    asset_names = [
        "Customer Database", "ERP System", "Internal Network",
        "Email Server", "HR Records", "Payment Gateway",
        "IoT Sensor Network", "Document Management System"
    ]
    
    assets = []
    for asset in asset_names:
        assets.append({
            "Asset": asset,
            "Confidentiality": random.randint(1, 5),
            "Integrity": random.randint(1, 5),
            "Availability": random.randint(1, 5)
        })
    
    df_assets = pd.DataFrame(assets)
    return df_assets

if __name__ == "__main__":
    df = generate_assets()
    print(df)
