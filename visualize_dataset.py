# %% Import excel to dataframe
import pandas as pd

df = pd.read_excel("Online Retail.xlsx")


# %% Show the first 10 rows
print(df.head(10))


# %% Generate descriptive statistics regardless of the datatypes
print(df.describe(include='all'))


# %% Remove all the rows with null value and generate stats again
df = df.dropna()
print(df.describe(include='all'))


# %% Remove rows with invalid Quantity (Quantity being less than 0)
df = df[df['Quantity'] >= 0]


# %% Remove rows with invalid UnitPrice (UnitPrice being less than 0)
df = df[df['UnitPrice'] >= 0]


# %% Only Retain rows with 5-digit StockCode
df = df[df['StockCode'].astype(str).str.len() == 5]


# %% Strip all description
df['Description'] = df['Description'].str.strip()


# %% Generate stats again and check the number of rows
print(df.describe(include='all'))
print(f'Number of rows: {len(df)}')


# %% Plot top 5 selling countries
import matplotlib.pyplot as plt
import seaborn as sns

top5_selling_countries = df["Country"].value_counts()[:5]
sns.barplot(x=top5_selling_countries.index, y=top5_selling_countries.values)
plt.xlabel("Country")
plt.ylabel("Amount")
plt.title("Top 5 Selling Countries")


# %% Plot top 20 selling products, drawing the bars vertically to save room for product description
top20_selling_products = df["Description"].value_counts()[:20]
sns.barplot(y=top20_selling_products.index, x=top20_selling_products.values)
plt.xlabel("Amount")
plt.ylabel("Product")
plt.title("Top 20 Selling Products")


# %% Focus on sales in UK
df_uk = df[df["Country"] == "United Kingdom