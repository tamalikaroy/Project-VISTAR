# 🇮🇳 Project VISTAR
### **Vital Indicator of Socio-economic Trends from Aadhaar Records**

![Project-VISTAR](https://img.shields.io/badge/Project-VISTAR-crimson.svg?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.10+-blue.svg?style=for-the-badge)
![Data Analysis](https://img.shields.io/badge/Focus-Statistical_Analysis-orange.svg?style=for-the-badge)

## 📖 Executive Summary
**Project VISTAR** is a data intelligence initiative that bypasses traditional 10-year Census lags by utilizing real-time **UIDAI (Aadhaar)** administrative footprints. By analyzing the ratio of **Child Enrolments (0-5 years)** to **Adult Workforce Updates (18+)**, this project establishes the **Migration Pressure Index (MPI)** to map economic "Gravity Wells" across 250+ districts in 5 major Indian states.

## 🛠️ Tech Stack & Methodology
* **Data Wrangling:** `Pandas` & `Regex` for "Nuclear Cleaning" (resolving administrative district renaming anomalies like Hoshangabad ➔ Narmadapuram).
* **Statistical Analysis:** Used descriptive statistics and custom indexing to identify "Source" vs "Sink" districts.
* **Geospatial Visualization:** `Plotly` & `Scipy` for 3D Topographic Surface Mapping of economic intensity.
* **Comparative Analytics:** `Seaborn` for Swarm Plot distribution to visualize the "State Average Paradox."

## 📂 Repository Structure
* **`data/raw/`**: 10 CSV datasets covering Enrolment and Update logs across UP, MH, KT, MP, and Bihar.
* **`notebooks/`**: Chronological analysis notebooks for individual states and the final synthesis.

## 🚀 Key Insights
1. **The State Average Paradox:** Discovered that state-level metrics often hide internal inequality; Karnataka's high-tech core contrasts sharply with its high-dependency rural districts.
2. **The 500x Gap:** Identified an exponential disparity in migration pressure between industrial magnets like **Bengaluru South** and labor-exporting districts like **Pashchim Champaran**.
3. **Ghost Data Resolution:** Successfully salvaged 15% of "lost" data by mapping renamed administrative districts to maintain longitudinal accuracy.

---
## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
