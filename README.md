# RiskSight – Model-Based IT Security Risk Analyzer

**RiskSight** is a **Python-based risk analysis tool** designed to help organizations identify, quantify, and mitigate cybersecurity risks in a **structured, model-driven way**. The project is inspired by **model-based security risk management frameworks** and follows best practices from standards like **STRIDE, CAPEC, and ISO/IEC controls**, making it ideal for IT governance, advisory, and digital transformation contexts.

---

## Project Overview

In modern digital environments, organizations must understand the risks to their assets ranging from IT systems to sensitive data and implement effective controls to prevent breaches or operational disruptions. **RiskSight** automates this process by:

1. Generating a **randomized list of assets** with **criticality scores** for Confidentiality, Integrity, Availability (CIA) and other security properties (organisations could use their own list of assets).
2. **Automatically linking assets to threats** using the **STRIDE framework**.
3. Retrieving **feasibility scores** for each threat from a **CAPEC-based database**.
4. Calculating **risk scores** by combining asset criticality and threat feasibility.
5. Visualizing risks via **risk matrices and heatmaps**, making it easier to prioritize mitigations.
6. Suggesting **ISO/IEC security controls** based on the threat profile to support compliance and governance.

---

## Key Features

- **Model-Based Approach**: Links assets, threats, and countermeasures systematically for full traceability.
- **Standards-Aligned**: Implements STRIDE threat modeling and CAPEC threat feasibility scoring.
- **Automated Risk Calculation**: Computes risk scores automatically based on asset criticality and threat feasibility.
- **Visualization**: Generates risk matrices and heatmaps for quick decision-making.
- **Advisory-Ready**: Outputs risk reports and recommended ISO/IEC controls for governance and compliance purposes.

---

## Use Case

RiskSight is suitable for organizations and teams looking to:

- Conduct structured **IT security risk assessments**.
- Prioritize threats based on **risk levels**.
- Align risk management with **industry standards** and best practices.
- Generate **traceable, visual reports** for decision-making and governance.

---

## Tech Stack

- **Python** – Core language for data handling and risk calculations
- **Pandas** – Asset, threat, and control data management
- **Matplotlib / Plotly** – Risk matrix and heatmap visualizations
- **CSV / JSON** – Threat and control databases
- **Optional**: Streamlit for interactive dashboards

---

## Next Steps / Extensions

- Integration with **real CAPEC API** for up-to-date threat information.
- Interactive **web dashboard** for visualization and reporting.
- Expanded **control library** covering multiple compliance standards.
- Integration with **simulated attack scenarios** for advisory use cases.

---


## Acknowledgements

- STRIDE threat modeling framework
- CAPEC threat catalog
- ISO/IEC security standards
