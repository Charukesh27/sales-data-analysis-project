import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("sales dataset.csv")
print(df)

df.head()

df.tail()

df['Revenue'] = df['Units Sold'] * df['Unit Price']
print('\n data with Revenue \n',df)


product_revenue = df.groupby('Product')['Revenue'].sum()
print('\nTotal Revenue by Product:\n', product_revenue)

product_units = df.groupby('Product')['Units Sold'].sum()
print("\n Total Units Sold by Product:\n",product_units)

monthly_revenue=df.groupby('Month')['Revenue'].sum()
print("\n Total Revenue per Month: \n",monthly_revenue)

plt.figure(figsize=(6,2))
product_revenue.plot(kind='bar',color='skyblue')
plt.title('Total Revenue by Product')
plt.ylabel('Revenue')
plt.show()

plt.figure(figsize=(6,4))
monthly_revenue.plot(kind='line', marker='o', color='green')
plt.title('Revenue Trend Over Monthly')
plt.ylabel('Revenue')
plt.xlabel('Month')
plt.show()

plt.figure(figsize=(6,6))
product_revenue.plot(kind='pie',autopct='%1.1f%%',startangle=90)
plt.title('Revenue share by Product')
plt.ylabel('')
plt.show()

print("\n Insights:")

top_product = product_revenue.idxmax()
top_product_revenue = product_revenue.max()
print(f" Best-selling product by revenue: {top_product} (${top_product_revenue})")

top_month = monthly_revenue.idxmax()
top_month_revenue = monthly_revenue.max()
print(f" Month with highest revenue: {top_month} (${top_month_revenue})")
