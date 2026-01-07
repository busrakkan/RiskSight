# src/threats.py
import pandas as pd
import random

def load_stride_threats(file_path="data/STRIDE_threats.csv"):
    """
    Load STRIDE threats from CSV.
    """
    df_threats = pd.read_csv(file_path)
    return df_threats["Threat"].tolist()

def link_threats_to_assets(df_assets, stride_threats, threats_per_asset=(1,3)):
    """
    Randomly assign 1-3 STRIDE threats to each asset.
    """
    asset_threats = []
    for _, asset in df_assets.iterrows():
        num_threats = random.randint(threats_per_asset[0], threats_per_asset[1])
        selected_threats = random.sample(stride_threats, num_threats)
        for threat in selected_threats:
            asset_threats.append({"Asset": asset["Asset"], "Threat": threat})
    return pd.DataFrame(asset_threats)

if __name__ == "__main__":
    from assets import load_assets
    df_assets = load_assets()
    stride_threats = load_stride_threats()
    df_asset_threats = link_threats_to_assets(df_assets, stride_threats)
    print(df_asset_threats)
