import pandas as pd

# Load data
df = pd.read_csv("churn.csv")

print("Data:")
print(df)

# Total customers
print("\nTotal Customers:", len(df))

# Churn count
print("\nChurn Count:")
print(df['Churn'].value_counts())
churn_percent = df['Churn'].value_counts(normalize=True) * 100
print("\nChurn Percentage:")
print(churn_percent)
plan_churn = pd.crosstab(df['Plan'], df['Churn'])
print("\nPlan vs Churn:")
print(plan_churn)
import matplotlib.pyplot as plt

df['Churn'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title("Churn Distribution")
plt.show()