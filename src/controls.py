# src/controls.py
import pandas as pd

def suggest_controls(df_risk, df_controls):
    """
    Suggest ISO controls for each threat in the risk dataframe.
    """
    controls_list = []
    for _, row in df_risk.iterrows():
        control_entries = df_controls[df_controls["Threat"] == row["Threat"]]
        if not control_entries.empty:
            for _, c in control_entries.iterrows():
                controls_list.append({
                    "Asset": row["Asset"],
                    "Threat": row["Threat"],
                    "Risk": row["Risk"],
                    "ISO_Control": c["ISO_Control"],
                    "Description": c["Description"]
                })
        else:
            controls_list.append({
                "Asset": row["Asset"],
                "Threat": row["Threat"],
                "Risk": row["Risk"],
                "ISO_Control": "N/A",
                "Description": "No control found"
            })
    df_controls_suggested = pd.DataFrame(controls_list)
    return df_controls_suggested

if __name__ == "__main__":
    df_risk = pd.DataFrame({
        "Asset":["ERP System"], "Threat":["Tampering"], "Risk":[12]
    })
    df_controls = pd.DataFrame({
        "Threat":["Tampering"],
        "ISO_Control":["ISO 27001 A.12.1"],
        "Description":["Implement change management and access control"]
    })
    
    df_suggested = suggest_controls(df_risk, df_controls)
    print(df_suggested)
