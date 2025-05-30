
# DSA210 Final Project Report  
**Author**: Umut Köprülü  
**Title**: The Impact of Digital Device Usage on Sleep and Study Time

---

## Introduction

This project explores the relationship between daily digital device usage (smartphone and computer), sleep duration, and study time. By analyzing personal data over a period of time, it aims to understand whether excessive screen time affects academic productivity and sleep quality.

---

## Data Source

- **Phone Usage (min)** – Collected from smartphone screen time tracking
- **Computer Usage (hrs)** – Collected from system activity log
- **Sleep Duration (hrs)** – Recorded using sleep tracking tools
- **Study Time (hrs)** – Logged manually based on study sessions

Data was recorded daily and stored in an Excel file: `ScreenSleepStudyData_Adjusted.xlsx`.

---

## Exploratory Data Analysis (EDA)

- Correlation analysis revealed strong negative relationships between screen time and study time.
- Visualizations showed that as phone/computer usage increased, study time tended to decrease.
- Time-series plots were used to track variable changes over time.

---

## Machine Learning (Phase 3)

A Linear Regression model was used to predict **Study Time** from:

- Phone Usage (min)
- Computer Usage (hrs)
- Sleep Duration (hrs)

### Metrics:
- R² Score: **0.9996**
- MAE: **0.019 hours**
- RMSE: **0.024 hours**

### Interpretation:
The model demonstrated excellent performance and aligned strongly with real data, suggesting clear linear dependencies among the variables.

---

## Results & Insights

- Higher phone and computer usage correlate with lower study duration.
- More sleep is generally associated with more study time.
- Effective screen time management could improve study outcomes.

---

## Limitations

- Data is based on a single individual, reducing generalizability.
- Study effectiveness and focus quality were not measured.
- Mood, environment, and stress levels were not included.

---

## Future Work

- Expand dataset to include multiple participants.
- Add qualitative measures (mood, attention, stress).
- Explore more complex ML models (e.g., Random Forest, SVR).

---

## AI Tools Used

- **ChatGPT** was used to structure this report, generate explanations, and format README content.
- **Python** and libraries like `pandas`, `scikit-learn`, `matplotlib`, and `statsmodels` were used in analysis.

