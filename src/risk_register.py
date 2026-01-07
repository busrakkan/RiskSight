# src/risk_register.py
import pandas as pd

def generate_risk_register(df_risk, df_controls):
    """
    Generate a consulting-style risk register by merging:
    - Risk analysis results
    - ISO control recommendations
    """

    # Merge risk table with ISO controls
    df_register = df_risk.merge(
        df_controls,
        on="Threat",
        how="left"
    )

    # Generate Risk IDs
    df_register.insert(
        0,
        "Risk_ID",
        ["RISK-" + str(i+1).zfill(3) for i in range(len(df_register))]
    )

    # Add consulting fields
    df_register["Risk_Owner"] = "IT Security"
    df_register["Risk_Status"] = "Open"

    # Reorder columns for readability
    columns_order = [
        "Risk_ID",
        "Priority",
        "Asset",
        "Threat",
        "Impact",
        "Likelihood",
        "Risk",
        "Risk_Level",
        "ISO_Control",
        "Description",
        "Risk_Owner",
        "Risk_Status"
    ]

    return df_register[columns_order]
