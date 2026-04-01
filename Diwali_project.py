import numpy as np
import pandas as pd

df = pd.read_csv(r"C:\Users\verma\Downloads\diwali_sales_sample.csv")

print(df.head())
print(df.info())

print("\nNull Values:\n", df.isnull().sum())

df.fillna(method='ffill', inplace=True)

df["Product"] = ["Car","Bike","Scooter","Car","Bike","Truck","Car","Scooter","Bike","Car"]

total_orders = df["Orders"].sum()
print("Total Numbers Of Orders :", total_orders)

total_revenue = df["Amount"].sum()
print("Total Revenue:", total_revenue)

unique_customer = df["Cust_name"].nunique()
print("Number Of Unique Customer:", unique_customer)

most_product = df["Product"].value_counts().idxmax()
print("The Most Repeat Product:", most_product)

gender_spend = df.groupby("Gender")["Amount"].sum().idxmax()
print("\nHighest Number Of Sales Spending :", gender_spend)

age_group_spends = df.groupby("Age_Group")["Amount"].sum().idxmax()
print("\nThe Age group spends the most:", age_group_spends)

occupation_highest_sales = df.groupby("Occupation")["Amount"].sum().idxmax()
print("\nThe highest total sales By Occupation :", occupation_highest_sales)

marital_status_buys = df.loc[df["Amount"].idxmax(), ["Marital_Status","Amount"]]
marital_status_buys["Marital_Status"] = "Married" if marital_status_buys["Marital_Status"] == 1 else "UnMarried"
print(marital_status_buys)

top5_customer = df.groupby("Cust_name")["Amount"].sum().sort_values(ascending=False).head(5)
print(top5_customer)

highest_sale_city = df.groupby("State")["Amount"].sum().idxmax()
print("The Highest Sales By City is:", highest_sale_city)

zone_most_revenue = df.groupby("Zone")["Amount"].sum().idxmax()
print("\nThe Most Generate Revenue Zone is:", zone_most_revenue)

top5_states_orders = df.groupby("State")["Orders"].sum().sort_values(ascending=False).head(5)
print("\nTop 5 States By Order Are:", top5_states_orders)

avg_state_order = df.groupby("State")["Amount"].mean()
print("\nThe Average Order Amount By States:")
print(avg_state_order)

most_selling_product = df.groupby("Product")["Orders"].sum().idxmax()
print("\nThe Most Selling Product Is:", most_selling_product)

highest_revenue_product = df.pivot_table(values="Amount", index="Product", aggfunc="sum").idxmax()
print("\nThe Highest Selling Product By Revenue Are:", highest_revenue_product)

avg_order = df.pivot_table(values="Orders", index="Product", aggfunc="mean")
print("\nThe Average Order Value:", avg_order)

top5_selling_product = df.pivot_table(values="Amount", index="Product", aggfunc="sum").sort_values(by="Amount", ascending=False).head(5)
print("\nThe Top 5 selling Product is:", top5_selling_product)

avg_order = int(df["Orders"].mean())
print("\nAverage number of orders per customer:", avg_order)

apper_most = df["Status"].value_counts().idxmax()
print("\nThe Most Common Status:", apper_most)

order_percent = int((df["Status"].value_counts(normalize=True)["Completed"]) * 100)
print("\nPercentage Of Orders Are Completed:", order_percent)

gender_age_spends = df.pivot_table(values="Amount", index=["Age_Group","Gender"], aggfunc="sum").idxmax()
print("\nThe Age Group And Gender Combination Spends The Most Are:", gender_age_spends)

occupation_revenue = df.groupby(["Zone","Occupation"])["Amount"].sum().groupby(level=0).idxmax()
print("\nThe Occupation Revenue By Zone:", occupation_revenue)

state_occupation_sales = df.pivot_table(values="Amount", index=["State","Occupation"], aggfunc="sum").idxmax()
print("\nThe Highest Sales By State and Occupation:", state_occupation_sales)

top10_cust_revenue = df.pivot_table(values="Amount", index="Cust_name", aggfunc="sum").sort_values(by="Amount", ascending=False).head(10)
print("\nTop 10 Customer In Our Company By Revenue Are", top10_cust_revenue)