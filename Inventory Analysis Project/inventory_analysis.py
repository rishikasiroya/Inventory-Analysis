import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

inventory = pd.read_csv('retail_store_inventory.csv')

inventory.head()

inventory.info()

#Checking for null values
inventory.isnull().sum()

inventory.describe()

#Summary of Key Metrics
print("=== Retail Store Inventory Summary ===")
print(f"Total products: {inventory['Product ID'].count()}")

print(f"Total Inventory Level: {inventory['Inventory Level'].sum()}")

print(f"Total Units Sold: {inventory['Units Sold'].sum()}")

print(f"Total Units Ordered: {inventory['Units Ordered'].sum()}")

print(f"Average Price: {inventory['Price'].mean()}")

print(f"Average Discount:{inventory['Discount'].mean()}")

#Grouping data by Category and calculating total Inventory Level for each
cate_inve = inventory.groupby('Category')['Inventory Level'].sum()
print(cate_inve)

# Bar chart for Category-wise Inventory Levels
plt.bar(cate_inve.index, cate_inve.values, color= 'skyblue', edgecolor= 'black')
plt.title("Category Wise Inventory Level")
plt.xlabel("Category")
plt.ylabel("Inventory Level")
plt.show()

#Grouping data by Category and calculating total Units Sold for each
cate_sale = inventory.groupby('Category')['Units Sold'].sum()
print(cate_sale)

#Grouping data by Category and calculating total Units Ordered for each
cate_order = inventory.groupby('Category')['Units Ordered'].sum()
print(cate_order)

#Grouping data by Region and calculating total Inventory Level for each
reg_inve = inventory.groupby('Region')['Inventory Level'].sum()
print(reg_inve)

#Grouping data by Region and calculating total Units Sold for each
reg_sale = inventory.groupby('Region')['Units Sold'].sum()
print(reg_sale)

# Pie chart for Region-wise Units Sold
plt.pie(reg_sale.values, labels= reg_sale.index, autopct='%1.1f%%', startangle=140, colors=['lightblue', 'lightgreen', 'orange', 'pink'])
plt.title("Region-Wise Units Sold")
plt.show()

#Grouping data by Region and calculating total Units Ordered for each
reg_order = inventory.groupby('Region')['Units Ordered'].sum()
print(reg_order)

#Grouping data by Seasonality and calculating total Inventory Level for each
sea_inve = inventory.groupby('Seasonality')['Inventory Level'].sum()
print(sea_inve)

#Grouping data by Seasonality and calculating total Units Sold for each
sea_sale = inventory.groupby('Seasonality')['Units Sold'].sum()
print(sea_sale)

#Grouping data by Seasonality and calculating total Units Ordered for each
sea_order = inventory.groupby('Seasonality')['Units Ordered'].sum()
print(sea_order)

#Grouping data by Store ID and calculating total Inventory Level for each
store_inve = inventory.groupby('Store ID')['Inventory Level'].sum()
print(store_inve)

#Grouping data by Store ID and calculating total Units Sold for each
store_sale = inventory.groupby('Store ID')['Units Sold'].sum()
print(store_sale)

#Grouping data by Store ID and calculating total Units Ordered for each
store_order = inventory.groupby('Store ID')['Units Ordered'].sum()
print(store_order)

#Grouping data by Category and calculating average Price for each
cate_price = inventory.groupby('Category')['Price'].mean()
print(cate_price)

#Grouping data by Category and calculating average Discount for each
cate_dis = inventory.groupby('Category')['Discount'].mean()
print(cate_dis)

#Grouping data by Category and calculating average Competitor Price for each
cate_cp = inventory.groupby('Category')['Competitor Pricing'].mean()
print(cate_cp)

#Converting date col from object to date datatype
inventory['Date'] = pd.to_datetime(inventory['Date'])

#Extracting year from date col
inventory['Year'] = inventory['Date'].dt.year

inventory.head()

#Grouping data by Year and calculating total Inventory Level for each
year_inve = inventory.groupby('Year')['Inventory Level'].sum()
print(year_inve)

# Line plot for Year-wise Inventory Levels
plt.plot(year_inve.index, year_inve.values, marker= 'o', color= 'blue')
plt.title("Year-wise Inventory Levels")
plt.xlabel("Year")
plt.ylabel("Inventory Level")
plt.grid(linestyle= '--')
plt.show()

#Grouping data by Year and calculating total Units Sold for each
year_sale = inventory.groupby('Year')['Units Sold'].sum()
print(year_sale)

#Grouping data by Year and calculating total Units Ordered for each
year_order = inventory.groupby('Year')['Units Ordered'].sum()
print(year_order)

#Correlation between Price, Units Sold and Discount
correlation = inventory[['Price', 'Units Sold', 'Discount']].corr()
print(correlation)

# Box Plot for Units Sold
plt.boxplot(inventory['Units Sold'])
plt.title("Outlier Analysis - Units Sold")
plt.show()

# Box Plot for Inventory Level
plt.boxplot(inventory['Inventory Level'])
plt.title("Outlier Analysis - Inventory Level")
plt.show()

#Creating Revenue Column
inventory['Revenue'] = inventory['Units Sold'] * inventory['Price']
inventory.head()

#Revenue Calculations
print("Total revenue:", inventory['Revenue'].sum())

#Grouping data by Category and calculating average revenue for each
cate_rev = inventory.groupby('Category')['Revenue'].mean()
print(cate_rev)

#Grouping data by Store ID and calculating average revenue for each
str_rev = inventory.groupby('Store ID')['Revenue'].mean()
print(str_rev)

#Grouping data by Region and calculating average revenue for each
reg_rev = inventory.groupby('Region')['Revenue'].mean()
print(reg_rev)

#Grouping data by Seasonality and calculating average revenue for each
sea_rev = inventory.groupby('Seasonality')['Revenue'].mean()
print(sea_rev)

#Grouping data by Year and calculating average revenue for each
year_rev = inventory.groupby('Year')['Revenue'].mean()
print(year_rev)