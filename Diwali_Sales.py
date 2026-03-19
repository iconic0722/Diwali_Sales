import numpy as np
import pandas as pd

df = pd.read_csv(r"C:\Users\verma\Downloads\diwali_sales_sample.csv")
print(df)

df.info()
print("\nNull Value In Table\n",df.isnull().sum())

df["Product"] = ["Car","Bike","Scooter","Car","Bike","Truck","Car","Scooter","Bike","Car"]
print(df)
Total_orders = df["Orders"].sum()
print("Total Numbers Of Orders :", Total_orders)

Total_Revenue =  df["Amount"].sum()
print("Total Revenue:", Total_Revenue)

Unique_Customer = df["Cust_name"].nunique()
print("Number Of Unique Customer:", Unique_Customer)

Most_Product = df["Product"].value_counts().idxmax()
print("The Most Repeat Product:", Most_Product)

Gender_Spend = df.groupby("Gender")["Amount"].sum().idxmax()
print("\nHighest Number Of Sales Spending :")
print(Gender_Spend)

# Gender = df.pivot_table(values="Amount",index="Gender",aggfunc="sum").idxmax()
# print(Gender) (Other Option to do this)

Age_group_spends = df.groupby("Age_Group")["Amount"].sum().idxmax()
print("\nThe Age group spends the most:", Age_group_spends) 

Occupation_highest_sales = df.groupby("Occupation")["Amount"].sum().idxmax()
print("\nThe the highest total sales By Occupation :", Occupation_highest_sales)

Marital_status_buys = df.loc[df["Amount"].idxmax(),["Marital_Status","Amount"]]
Marital_status_buys["Marital_Status"] = "Married" if Marital_status_buys["Marital_Status"] == 1 else "UnMarried"
print(Marital_status_buys)    

top5_customer = df.groupby("Cust_name")["Amount"].sum().sort_values(ascending=False).head(5)
print(top5_customer)

# top_customer = df.nlargest(5,"Amount")[["Cust_name","Amount"]]
# print(top_customer)(Other option to do this)

highest_sale_city = df.groupby("State")["Amount"].sum().idxmax()
print("The Highest Sales By City is:",highest_sale_city)

zone_most_revenue = df.groupby("Zone")["Amount"].sum().idxmax()
print("\nThe Most Generate Revenue Zone is: ", zone_most_revenue)

top5_states_orders = df.groupby("State")["Orders"].sum().sort_values(ascending=False).head(5)
print("\nTop 5 States By Order Are :", top5_states_orders)

Avg_state_order = df.groupby("State")["Amount"].mean()
print("\nThe Average Order Amount By States:")
print(Avg_state_order)

most_selling_product = df.groupby("Product")["Orders"].sum().idxmax()
print("\nThe Most Selling Product Is :", most_selling_product)

highest_revenue_product = df.pivot_table(values="Amount",index="Product",aggfunc="sum").idxmax()

# highest_revenue_product = df.pivot_table(values="Amount",index="Product",aggfunc="sum").sort_values(by="Amount",ascending=False).head(1)
# # We use this when we want value as well..
print("\nThe Highest Selling Product By Revenue Are:", highest_revenue_product)

avg_order = df.pivot_table(values="Orders",index="Product",aggfunc="mean")
print("\nThe Average Order Value:",avg_order)

Top5_selling_product = df.pivot_table(values="Amount",index="Product",aggfunc="sum").sort_values(by="Amount",ascending=False).head(5)
print("\nThe Top 5 selling Product is :", Top5_selling_product)

avg_order= int(df["Orders"].mean())
print("\nAverage number of orders per customer:",avg_order)

apper_most = df["Status"].value_counts().idxmax()
print("\nThe Most Common Status:", apper_most)

order_percent = int((df["Status"].value_counts(normalize=True)["Completed"]) *100)
print("\nPercentage Of Orders Are Completed:",order_percent)

gender_age_spends = df.pivot_table(values="Amount",index=["Age_Group","Gender"],aggfunc="sum").idxmax()
print("\nThe Age Group And Gender Combination Spends The Most Are :",gender_age_spends)

occupation_revenue = df.groupby(["Zone","Occupation"])["Amount"].sum().groupby(level=0).idxmax()
print("\nThe Occupation Revenue By Zone:", occupation_revenue)

state_occupation_sales = df.pivot_table(values="Amount",index=["State","Occupation"],aggfunc="sum").idxmax()
print("\nThe Highest Sales By State and Occupation:",state_occupation_sales)

Top10_cust_revenue = df.pivot_table(values="Amount",index="Cust_name",aggfunc="sum").sort_values(by="Amount",ascending=False).head(10)
print("\nTop 10 Customer In Our Company By Revenue Are",Top10_cust_revenue)

