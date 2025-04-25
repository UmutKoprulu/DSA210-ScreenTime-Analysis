import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr
import statsmodels.api as sm

# 1. Load Data (Excel)
data = pd.read_excel("ScreenSleepStudyData_Adjusted.xlsx", 
                     sheet_name=0,
                     parse_dates=["Date"])

# 2. Data Cleaning
for col in ["Phone Usage (min)", "Computer Usage (hrs)",
            "Sleep Duration (hrs)", "Study Time (hrs)"]:
    data[col] = pd.to_numeric(data[col], errors="coerce")

print("Missing values per column:\n", data.isnull().sum(), "\n")

# Drop rows with any missing values in key columns
data.dropna(subset=["Phone Usage (min)", "Computer Usage (hrs)",
                    "Sleep Duration (hrs)", "Study Time (hrs)"], inplace=True)

# 3. Correlation Matrix & Heatmap
corr = data[["Phone Usage (min)", "Computer Usage (hrs)",
             "Sleep Duration (hrs)", "Study Time (hrs)"]].corr()
plt.figure(figsize=(8,6))
sns.heatmap(corr, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
plt.title("Correlation Matrix")
plt.tight_layout()
plt.show()

# 4. Scatter Plots
pairs = [
    ("Phone Usage (min)", "Sleep Duration (hrs)"),
    ("Phone Usage (min)", "Study Time (hrs)"),
    ("Computer Usage (hrs)", "Sleep Duration (hrs)"),
    ("Computer Usage (hrs)", "Study Time (hrs)")
]

for x, y in pairs:
    plt.figure(figsize=(6,4))
    sns.scatterplot(x=x, y=y, data=data)
    plt.title(f"{x} vs {y}")
    plt.tight_layout()
    plt.show()

# 5. Time-Series Plot
plt.figure(figsize=(10,4))
for col, fmt in [("Phone Usage (min)", "o--"), 
                 ("Computer Usage (hrs)", "s-"), 
                 ("Sleep Duration (hrs)", "^-"), 
                 ("Study Time (hrs)", "d-")]:
    plt.plot(data["Date"], data[col], fmt, label=col)
plt.legend()
plt.title("Time-Series of All Variables")
plt.xlabel("Date")
plt.ylabel("Value")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 6. Hypothesis Testing (Pearson)
print("Pearson Correlations & p-values:")
for x, y in pairs:
    r, p = pearsonr(data[x], data[y])
    sig = "✓" if p < 0.05 else "✗"
    print(f" {x} vs {y}: r = {r:.2f}, p = {p:.3f} {sig}")
print()

# 7. Regression Analysis
# Predict Sleep Duration from Phone Usage
X = sm.add_constant(data["Phone Usage (min)"])
model1 = sm.OLS(data["Sleep Duration (hrs)"], X).fit()
print(model1.summary(), "\n")

# Predict Study Time from Phone Usage
X2 = sm.add_constant(data["Phone Usage (min)"])
model2 = sm.OLS(data["Study Time (hrs)"], X2).fit()
print(model2.summary())
