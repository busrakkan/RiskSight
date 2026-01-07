# src/assets.py
import pandas as pd

def load_assets(file_path="data/assets.csv"):
    """
    Load assets and their CIA scores from CSV.
    """
    df_assets = pd.read_csv(file_path)
    return df_assets

if __name__ == "__main__":
    df = load_assets()
    print(df)
