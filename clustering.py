# %% read data
import pandas as pd

df = pd.read_csv("seeds_dataset.txt", sep="\t+", header=None)
# 1 area A,
# 2 perimeter P,
# 3 compactness C = 4*pi*A/P^2,
# 4 length of kernel,
# 5 width of kernel,
# 6 asymmetry coefficient
# 7 length of kernel groove.
# 8 target
df.columns = [
    "area",
    "perimeter",
    "compactness",
    "length_kernel",
    "width_kernel",
    "asymmetry_coefficient",
    "length_kernel_groove",
    "target",
]


# %%
df.describe()


#%%
import seaborn as sns


sns.scatterplot(
    x="area",
    y="asymmetry_coefficient",
    data=df,
    hue="target",
    legend="full",
)


# %% also try lmplot and pairplot
sns.lmplot(
    x="area",
    y="asymmetry_coefficient",
    data=df,
    hue="target"
)

sns.pairplot(df, hue="target")

# %% determine the best numbmer of clusters
from sklearn.cluster import KMeans
from sklearn.metrics import homogeneity_score


x = df.drop("target", axis=1)
y = df["target"]
inertia = {}
homogeneity = {}

# use kmeans to loop over candidate number of clusters 
# store inertia and homogeneity score in each iteration
for k in range(1, 11):  # Trying 1 to 10 clusters
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(x)
    inertia[k] = kmeans.inertia_
    homogeneity[k] = homogeneity_score(y, kmeans.labels_)

# %% 

ax = sns.lineplot(
    x=list(inertia.keys()),
    y=list(inertia.values()),
    color="blue",
    label="inertia",
    legend=None,
)
ax.set_ylabel("inertia")
ax.twinx()
ax = sns.lineplot(
    x=list(homogeneity.keys()),
    y=list(homogeneity.values()),
    color="red",
    label="homogeneity",
    legend=None,
)
ax.set_ylabel("homogeneity")
ax.figure.legend()
