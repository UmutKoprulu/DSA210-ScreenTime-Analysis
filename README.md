# Screen Time, Sleep & Study Time Analysis

**Author:** Umut Köprülü  
Sabancı University – Computer Science  

---

## Overview

This project analyzes the relationship between daily digital device usage, sleep duration, and study time using self-collected time-series data.  

The objective is to explore statistical correlations between behavioral variables and build regression models to predict study duration.

---

## Research Questions

- Does increased smartphone or computer usage reduce sleep duration?
- Is there a correlation between screen time and decreased study hours?
- Does insufficient sleep lead to lower study productivity?

---

## Dataset

The dataset consists of structured daily records including:

- **Phone Usage (minutes)**
- **Computer Usage (hours)**
- **Sleep Duration (hours)**
- **Study Time (hours)**

Example format:

| Date       | Phone Usage (min) | Computer Usage (hrs) | Sleep Duration (hrs) | Study Time (hrs) |
|------------|------------------|----------------------|----------------------|------------------|
| 2025-03-10 | 180              | 5                    | 6                    | 3                |
| 2025-03-11 | 220              | 3.5                  | 7.5                  | 4                |
| 2025-03-12 | 150              | 4                    | 8                    | 5                |

---

## Methodology

### 1. Data Preprocessing
- Data cleaning and formatting  
- Handling missing values  
- Feature selection  

### 2. Exploratory Data Analysis (EDA)
- Distribution analysis  
- Scatter plot relationships  
- Correlation matrix visualization  
- Time-series trend analysis  

### 3. Statistical Testing
- Pearson correlation analysis  
- Hypothesis evaluation  

---

## Machine Learning Models

To predict **Study Time**, three regression models were implemented:

- Linear Regression  
- Decision Tree Regressor  
- Random Forest Regressor  

### Model Performance

Best performing model:

- **Linear Regression (R² = 0.9996)**

---

## Tech Stack

- Python  
- pandas  
- numpy  
- scikit-learn  
- seaborn  
- matplotlib  
- statsmodels  
- Jupyter Notebook  

---

## Key Insights

- Strong statistical relationships were observed between screen time and sleep duration.  
- Sleep duration appears to mediate study productivity.  
- Regression models captured structured behavioral patterns effectively.

---

## Limitations

- Dataset is based on a single individual.  
- Limited sample size may affect generalization.  
- Study effectiveness (quality) is not directly measured.

---

## How to Run

```bash
pip install -r requirements.txt
jupyter notebook
