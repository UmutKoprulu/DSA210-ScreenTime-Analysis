# The Impact of Digital Device Usage on Sleep and Study Time  
**Author:** Umut Köprülü 
## **Project Overview**  
In this project, I aim to examine the relationship between daily digital device usage, sleep duration, and study time. The increasing reliance on smartphones and computers raises important questions about their effects on daily routines, particularly sleep quality and study efficiency. By tracking my own device usage patterns, sleep duration, and study hours, I will analyze potential correlations and trends in my habits over time.  

## **Motivation**  
With the growing integration of technology into our daily lives, many students find themselves spending extended hours on digital devices. This raises concerns about how screen time impacts sleep and academic performance. The primary goal of this project is to understand whether excessive device usage affects the amount of sleep I get and the time I dedicate to studying. Key research questions include:  

- Does increased smartphone or computer usage reduce sleep duration?  
- Is there a correlation between screen time and decreased study hours?  
- Does insufficient sleep lead to lower study productivity?  

By analyzing my own data, I hope to gain insights into how screen time management can contribute to better academic performance and overall well-being.  

## **Hypotheses**  
1. **First Hypothesis:** There is no significant relationship between digital device usage and sleep or study duration.  
2. **Second Hypothesis:** Increased screen time negatively impacts both sleep duration and study time.  

## **Data Collection**  
The dataset for this project consists of daily records collected over a specific period. Data will be gathered manually from device tracking tools and personal logs. The key variables include:  

- **Smartphone Usage (minutes):** Collected via **iOS Screen Time / Android Digital Wellbeing**  
- **Computer Usage (hours):** Retrieved from **Mac Screen Time / Windows Activity Monitor**  
- **Sleep Duration (hours):** Measured using **Apple Health / Samsung Health or manual logging**  
- **Study Time (hours):** Recorded manually based on daily study sessions (e.g., Pomodoro method, task completion logs)  

### **Data Format**  
All data will be recorded in a structured format and stored in a CSV file for analysis. An example of the dataset format is as follows:  

| Date       | Phone Usage (min) | Computer Usage (hrs) | Sleep Duration (hrs) | Study Time (hrs) |
|------------|------------------|----------------------|----------------------|------------------|
| 2025-03-10 | 180              | 5                    | 6                    | 3                |
| 2025-03-11 | 220              | 3.5                  | 7.5                  | 4                |
| 2025-03-12 | 150              | 4                    | 8                    | 5                |

This structured approach ensures consistency and enables effective data analysis.  

## **Methodology**  
The project will involve several stages of analysis:  

1. **Data Cleaning & Preparation:**  
   - Handling missing values and ensuring consistency in data formatting.  

2. **Exploratory Data Analysis (EDA):**  
   - Visualizing distributions of device usage, sleep, and study time.  
   - Creating scatter plots to examine relationships between screen time, sleep, and study hours.  
   - Generating correlation matrices to quantify potential dependencies between variables.  

3. **Statistical Testing:**  
   - **Pearson correlation test** to determine relationships between screen time and other variables.  
   - **T-tests or ANOVA** to compare study and sleep differences across screen time levels.  

4. **Insights & Interpretation:**  
   - Identifying trends and patterns in the dataset.  
   - Evaluating whether excessive screen time impacts sleep and study efficiency.  

## **Expected Outcomes**  
- A potential negative correlation between excessive phone/computer usage and sleep duration.  
- A possible reduction in study time when screen time increases.  
- Evidence that sleep duration might mediate the impact of screen time on study hours.  

## **Limitations & Future Considerations**  
- The dataset is limited to a single individual, which may reduce generalizability.  
- Subjective factors, such as study effectiveness, are not directly measured.  
- Additional variables, such as blue light filter usage or nighttime device activity, could be incorporated in future studies.  

## **Conclusion**  
This project aims to provide data-driven insights into the relationship between digital device usage, sleep patterns, and academic productivity. The findings may help optimize screen time management strategies for improved study efficiency and overall well-being.  


## Machine Learning Models Used

To predict **Study Time**, three different machine learning models were trained and compared using features like:

- Phone Usage (min)  
- Computer Usage (hrs)  
- Sleep Duration (hrs)

### Models:
- **Linear Regression**
- **Decision Tree Regressor**
- **Random Forest Regressor**

The Linear Regression model gave the best performance (R²: 0.9996), but all three models were evaluated to ensure robustness.
## AI Tools & Support

- **ChatGPT** was used to structure the project report, summarize insights, generate this README file, and assist with data explanations.
- **Python** libraries such as `pandas`, `scikit-learn`, `seaborn`, `matplotlib`, and `statsmodels` were used in the implementation.


---
