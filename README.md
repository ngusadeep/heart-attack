# 🫀 Heart Attack EDA

Exploratory Data Analysis (EDA) on a cardiovascular health dataset to uncover patterns, correlations, and possible risk factors for heart attacks.  
This analysis focuses on patient vitals and lab results, identifying trends that differentiate **positive** and **negative** heart attack cases.

---

## 📌 Project Overview

Heart attacks remain one of the leading causes of death worldwide.  
Through data analysis, we can identify health factors that significantly impact heart attack risk.  
In this project, we:

- Clean and prepare the dataset for analysis
- Explore relationships between health metrics and heart attack outcomes
- Visualize data for better understanding
- Generate statistical insights to aid early detection

---

## 📂 Dataset

| Column            | Description                                            |
| ----------------- | ------------------------------------------------------ |
| **age**           | Age of the patient (years)                             |
| **gender**        | Gender (1 = male, 0 = female)                          |
| **impluse**       | Pulse / heart rate (beats per minute)                  |
| **pressurehight** | Systolic blood pressure (mmHg)                         |
| **pressurelow**   | Diastolic blood pressure (mmHg)                        |
| **glucose**       | Blood sugar level (mg/dL)                              |
| **kcm**           | Potassium concentration in the blood (mmol/L)          |
| **troponin**      | Troponin level (ng/mL) – a key marker for heart damage |
| **class**         | Heart attack outcome (`positive` or `negative`)        |

**Sample Record:**
| age | gender | impluse | pressurehight | pressurelow | glucose | kcm | troponin | class |
|-----|--------|---------|---------------|-------------|---------|-----|----------|--------|
| 64 | 1 | 66 | 160 | 83 | 160 | 1.8 | 0.012 | negative |

---

## 🛠 Tools & Libraries

- Python 3.x
- Pandas – Data manipulation
- NumPy – Numerical computations
- Matplotlib / Seaborn – Visualization
- Plotly – Interactive graphs (optional)

---

## 📊 EDA Process

1. **Data Loading** – Import dataset into Pandas
2. **Data Cleaning** – Fix column names, handle missing values, correct outliers
3. **Univariate Analysis** – Distributions of age, glucose, blood pressure, troponin, etc.
4. **Bivariate Analysis** – Compare medical metrics between positive and negative cases
5. **Correlation Analysis** – Heatmaps to find relationships between features
6. **Feature Insights** – Identify most important indicators for heart attack detection

---

## 🔍 Key Insights (examples)

- Elevated **troponin** levels are strongly associated with heart attacks
- Patients with **high systolic blood pressure** (>140 mmHg) and age above 50 show higher risk
- **Pulse rate** anomalies may correlate with increased probability of a positive case
- **Glucose and potassium** imbalance could be a secondary risk factor

---

## 🚀 How to Run

```bash
# Clone the repository
git clone https://github.com/ngusadeep/heart-attack.git
```
