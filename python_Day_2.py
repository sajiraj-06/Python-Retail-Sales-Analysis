import pandas as pd
import matplotlib.pyplot as plt

print("Python Portfolio Project")
print("Libraries imported successfully!")

import pandas as pd

df = pd.read_csv(r"C:\Users\ASUS\OneDrive\Documents\Data -analytics-portpolio\Data set\Retail_Sales_Data csv.csv")

print(df.head())
print("Total Records:", len(df))
# Monthly Sales Analysis

df["Order_Date"] = pd.to_datetime(df["Order_Date"])

df["Month"] = df["Order_Date"].dt.to_period("M")

monthly_sales = df.groupby("Month").agg({
    "Revenue_LKR": "sum",
    "Profit_LKR": "sum"
})

print("\n--- MONTHLY SALES ANALYSIS ---")
print(monthly_sales)
# Data Visualization

import matplotlib.pyplot as plt

product_revenue = df.groupby("Product")["Revenue_LKR"].sum()

plt.figure(figsize=(10, 6))
product_revenue.plot(kind="bar")

plt.title("Product-wise Revenue Analysis")
plt.xlabel("Product")
plt.ylabel("Revenue (LKR)")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("Product_Revenue_Chart.png")
plt.show()

# BUSINESS INSIGHTS

print("\n========== BUSINESS INSIGHTS ==========")

# 1. Total Business Performance
print("Total Revenue:", df["Revenue_LKR"].sum())
print("Total Profit:", df["Profit_LKR"].sum())

# 2. Best Revenue Product
best_revenue_product = (
    df.groupby("Product")["Revenue_LKR"].sum().idxmax()
)

print("Best Revenue Product:", best_revenue_product)

# 3. Best Profit Product
best_profit_product = (
    df.groupby("Product")["Profit_LKR"].sum().idxmax()
)

print("Best Profit Product:", best_profit_product)

# 4. Top Customer
top_customer = (
    df.groupby("Customer_ID")["Revenue_LKR"].sum().idxmax()
)

print("Top Customer:", top_customer)

# 5. Average Profit
print("Average Profit:", df["Profit_LKR"].mean())

print("\n========== ANALYSIS COMPLETED ==========")

# BUSINESS RECOMMENDATIONS

print("\n========== BUSINESS RECOMMENDATIONS ==========")

print("\n1. Customer Retention:")
print("Provide loyalty rewards and special discounts to top customers.")

print("\n2. Product Promotion:")
print("Promote high-revenue and high-profit products.")

print("\n3. Profit Improvement:")
print("Review low-profit products and control operating costs.")

print("\n4. Inventory Management:")
print("Maintain sufficient stock of products with high sales demand.")

print("\n5. Sales Growth:")
print("Analyze monthly sales trends and create seasonal promotions.")

print("\n========== RECOMMENDATIONS COMPLETED ==========")