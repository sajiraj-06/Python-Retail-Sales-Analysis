import pandas as pd
import matplotlib.pyplot as plt

print("Python Portfolio Project")
print("Libraries imported successfully!")

import pandas as pd

df = pd.read_csv(r"C:\Users\ASUS\OneDrive\Documents\Data -analytics-portpolio\Data set\Retail_Sales_Data csv.csv")

print(df.head())
print("Total Records:", len(df))

#Dataset Information

print("\nDataset Information:")
print(df.info())

print("\nDataset Statistics:")
print(df.describe())

print("\nColumn Names:")
print(df.columns.tolist()) 

#Data Quality Check

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Records:")
print(df.duplicated().sum())

print("\nTotal Rows and Columns:")
print(df.shape)

#Basic Business Analysis
total_revenue = df["Revenue_LKR"].sum()
total_cost = df["Cost_LKR"].sum()
total_profit = df["Profit_LKR"].sum()

average_revenue = df["Revenue_LKR"].mean()
average_profit = df["Profit_LKR"].mean()

print("\n--- BUSINESS PERFORMANCE ---")

print("Total Revenue:", total_revenue)
print("Total Cost:", total_cost)
print("Total Profit:", total_profit)
print("Average Revenue:", average_revenue)
print("Average Profit:", average_profit)

# Product-wise Analysis

product_analysis = df.groupby("Product").agg({
    "Quantity": "sum",
    "Revenue_LKR": "sum",
    "Profit_LKR": "sum"
})

product_analysis = product_analysis.sort_values(
    by="Profit_LKR",
    ascending=False
)

print("\n--- PRODUCT PERFORMANCE ---")
print(product_analysis)
# Top 5 Customers Analysis

customer_analysis = df.groupby("Customer_ID").agg({
    "Revenue_LKR": "sum",
    "Profit_LKR": "sum"
})

top_customers = customer_analysis.sort_values(
    by="Revenue_LKR",
    ascending=False
).head(5)

print("\n--- TOP 5 CUSTOMERS ---")
print(top_customers)
