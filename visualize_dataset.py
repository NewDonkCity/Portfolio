# %% Import excel to dataframe
import pandas as pd

# Read the data from the "Online Retail.xlsx" Excel file into a DataFrame named 'df'
df = pd.read_excel("Online Retail.xlsx")

# %%  Show the first 10 rows
# Display the first 10 rows of the DataFrame 'df'
print(df.head(10))

# %% Generate descriptive statistics regardless the datatypes
# Display descriptive statistics for all columns in the DataFrame 'df', including categorical data
print(df.describe(include='all'))

# %% Remove all the rows with null value and generate stats again
# Drop rows with any missing values (NaN) from the DataFrame 'df'
df = df.dropna()

# Display descriptive statistics for all columns in the updated DataFrame 'df'
print(df.describe(include='all'))

# %% Remove rows with invalid Quantity (Quantity being less than 0)
# Filter the DataFrame 'df' to only keep rows where Quantity is greater than or equal to 0
df = df[df['Quantity'] >= 0]

# %% Remove rows with invalid UnitPrice (UnitPrice being less than 0)
# Filter the DataFrame 'df' to only keep rows where UnitPrice is greater than or equal to 0
df = df[df['UnitPrice'] >= 0]

# %% Only Retain rows with 5-digit StockCode
# Filter the DataFrame 'df' to only keep rows where StockCode is a 5-digit number
df = df[df['StockCode'].astype(str).str.len() == 5]

# %% strip all description
# Remove leading and trailing whitespaces from the 'Description' column in the DataFrame 'df'
df['Description'] = df['Description'].str.strip()

# %% Generate stats again and check the number of rows
# Display descriptive statistics for all columns in the updated DataFrame 'df'
print(df.describe(include='all'))

# Print the number of rows in the updated DataFrame 'df'
print(f'Number of rows: {len(df)}')

# %% Plot top 5 selling countries
import matplotlib.pyplot as plt
import seaborn as sns

top5_selling_countries = df["Country"].value_counts()[:5]
sns.barplot(x=top5_selling_countries.index, y=top5_selling_countries.values)
plt.xlabel("Country")
plt.ylabel("Amount")
plt.title("Top 5 Selling Countries")
plt.show()

# %% Plot top 20 selling products, drawing the bars vertically to save room for product description
# Group the data by product description and count the number of unique InvoiceNo's (sales)
# Select the top 20 products based on the highest number of unique InvoiceNo's
top_products = df.groupby('Description')['InvoiceNo'].nunique().sort_values(ascending=False).head(20)

# Plot a bar chart to show the top 20 selling products and their sales count
sns.barplot(y=top_products.index, x=top_products.values)
plt.title('Top 20 Selling Products')
plt.show()

# %% Focus on sales in UK
# Create a new DataFrame 'df_uk' containing only the rows with 'Country' as 'United Kingdom'
df_uk = df[df['Country'] == 'United Kingdom']

#%% Show gross revenue by year-month
from datetime import datetime
# Extract the year and month from the 'InvoiceDate' column and store it as 'YearMonth'
df_uk["YearMonth"] = df_uk["InvoiceDate"].apply(
    lambda dt: datetime(year=dt.year, month=dt.month, day=1)
)

# Calculate the gross revenue by summing the 'UnitPrice' for each year-month group
gross_revenue = df_uk.groupby('YearMonth')['UnitPrice'].sum()

# Plot a line chart to show the gross revenue trends over time
sns.lineplot(data=gross_revenue.reset_index(), x='YearMonth', y='UnitPrice')
plt.title('Gross Revenue by Year-Month')
plt.show()

# %% Save the 'df_uk' DataFrame in pickle format with the name "UK.pkl"
# Only retain the 'InvoiceNo', 'StockCode', and 'Description' columns
df_uk.to_pickle('UK.pkl')
df_uk = df_uk[['InvoiceNo', 'StockCode', 'Description']]
# %%
