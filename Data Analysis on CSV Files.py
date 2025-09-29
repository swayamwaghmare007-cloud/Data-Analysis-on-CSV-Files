import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('Global_Superstore(CSV).csv', encoding='utf-8', sep=',')

# Display basic info and a sample
print(df.info())
print(df.head())

# Convert 'Order Date' to a datetime object (if available)
if 'Order Date' in df.columns:
    df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')


# Aggregate sales for target columns
cat_sales = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)
subcat_sales = df.groupby('Sub-Category')['Sales'].sum().sort_values(ascending=False)
region_sales = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)
country_sales = df.groupby('Country')['Sales'].sum().sort_values(ascending=False)
segment_sales = df.groupby('Segment')['Sales'].sum().sort_values(ascending=False)

print('Sales by Category:')
print(cat_sales)
print('Sales by Sub-Category:')
print(subcat_sales)
print('Sales by Region:')
print(region_sales)
print('Sales by Country (Top 10):')
print(country_sales.head(10))
print('Sales by Segment:')
print(segment_sales)


# Sales by Category
plt.figure(figsize=(8,4))
cat_sales.plot(kind='bar', color='skyblue')
plt.title('Total Sales by Category')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('sales_by_category.png')
plt.close()

# Sales by Sub-Category
plt.figure(figsize=(10,4))
subcat_sales.plot(kind='bar', color='teal')
plt.title('Total Sales by Sub-Category')
plt.ylabel('Sales')
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('sales_by_subcategory.png')
plt.close()

# Sales by Region
plt.figure(figsize=(8,4))
region_sales.plot(kind='bar', color='coral')
plt.title('Total Sales by Region')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('sales_by_region.png')
plt.close()