# %% import dataframe from pickle file
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules
import seaborn as sns
import matplotlib.pyplot as plt

# Read the pickle file UK.pkl into a dataframe
df = pd.read_pickle("UK.pkl")
df.head()

# %% convert dataframe to invoice-based transactional format
# Group the dataframe by invoice number
df_grouped = df.groupby('InvoiceNo')['Description'].apply(list)

# Use TransactionEncoder to transform the data into transactional format
te = TransactionEncoder()
te_ary = te.fit(df_grouped).transform(df_grouped)
df_trans = pd.DataFrame(te_ary, columns=te.columns_)

# %% apply apriori algorithm to find frequent items and association rules
# Generate frequent itemsets using the Apriori algorithm
frequent_itemsets = apriori(df_trans, min_support=0.02, use_colnames=True)
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=0.1)

# %% count of frequent itemsets that have more then 1/2/3 items,
# and the frequent itemsets that has the most items
# Examine the frequent itemsets and determine how many itemsets contain over 1/2/3 items
print(frequent_itemsets['itemsets'].apply(lambda x: len(x)).value_counts())

# Extract the frequent itemsets with the most items
max_items = max(frequent_itemsets['itemsets'].apply(lambda x: len(x)))
frequent_itemsets_max = frequent_itemsets[frequent_itemsets['itemsets'].apply(lambda x: len(x)) == max_items]

# %% top 10 lift association rules
# Extract the frequent itemsets with the most items
rules = rules.sort_values('lift', ascending=False)
top_10_rules = rules.head(10)

# %% scatterplot support vs confidence
# Visualize the relationship between support and confidence using a seaborn scatterplot
sns.scatterplot(x=rules["support"], y=rules["confidence"], alpha=0.5)
plt.xlabel("Support")
plt.ylabel("Confidence")
plt.title("Support vs Confidence")

# %% scatterplot support vs lift
# Visualize the relationship between support and lift
sns.scatterplot(x=rules["support"], y=rules["lift"], alpha=0.5)
plt.xlabel("Support")
plt.ylabel("Lift")
plt.title("Support vs Lift")
