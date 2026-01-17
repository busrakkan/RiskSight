import streamlit as st
import pandas as pd

from assets import load_assets
from threats import load_stride_threats, link_threats_to_assets
from risk_calculator import calculate_risk
from controls import suggest_controls
from visualization import plot_risk_matrix, plot_top_risks

st.set_page_config(
    page_title="RiskSight – Cyber Risk Analysis",
    layout="wide"
)

st.title("RiskSight – Cyber Risk Analysis Dashboard")

st.markdown("""
RiskSight is a lightweight cyber risk assessment tool that helps organizations
identify, prioritize, and mitigate security risks using structured methodologies
(STRIDE, CAPEC, ISO/IEC 27001).
""")


# Load Data
df_assets = load_assets("data/assets.csv")
stride_threats = load_stride_threats("data/STRIDE_threats.csv")
df_threats = link_threats_to_assets(df_assets, stride_threats)
df_capec = pd.read_csv("data/CAPEC.csv")
df_controls = pd.read_csv("data/ISO_controls.csv")

# Calculate Risk
df_risk = calculate_risk(df_assets, df_threats, df_capec)
df_controls_suggested = suggest_controls(df_risk, df_controls)

# Sidebar Filters
st.sidebar.header("Filters")

risk_level_filter = st.sidebar.multiselect(
    "Risk Level",
    options=df_risk["Risk_Level"].unique(),
    default=df_risk["Risk_Level"].unique()
)

df_risk_filtered = df_risk[df_risk["Risk_Level"].isin(risk_level_filter)]


# Tabs
tab1, tab2, tab3 = st.tabs(["Risk Table", "Risk Visualization", "Controls"])

with tab1:
    st.subheader("Risk Table")
    st.dataframe(df_risk_filtered, use_container_width=True)

with tab2:
    st.subheader("Risk Matrix")
    plot_risk_matrix(df_risk_filtered)

    st.subheader("Top Risks")
    plot_top_risks(df_risk_filtered)

with tab3:
    st.subheader("Suggested ISO Controls")
    st.dataframe(df_controls_suggested, use_container_width=True)


# Downloads
st.sidebar.header("Downloads")

st.sidebar.download_button(
    label="Download Risk Report",
    data=df_risk.to_csv(index=False),
    file_name="risk_report.csv",
    mime="text/csv"
)

st.sidebar.download_button(
    label="Download Controls Report",
    data=df_controls_suggested.to_csv(index=False),
    file_name="controls_report.csv",
    mime="text/csv"
)
