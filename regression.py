# %% read data
import pandas as pd

train = pd.read_csv(
    "house-prices-advanced-regression-techniques/train.csv"
)
test = pd.read_csv(
    "house-prices-advanced-regression-techniques/test.csv"
)


# %% checkout out first few rows
train.head()


# %% checkout out dataframe info
train.info()


# %% describe the dataframe
train.describe(include="all")


# %% SalePrice distribution
import seaborn as sns

sns.distplot(train["SalePrice"])


# %% SalePrice distribution w.r.t CentralAir / OverallQual / BldgType / etc
import matplotlib.pyplot as plt

fig, axs = plt.subplots(2, 2, figsize=(10, 10))
sns.boxplot(x="CentralAir", y="SalePrice", data=train, ax=axs[0, 0])
sns.boxplot(x="OverallQual", y="SalePrice", data=train, ax=axs[0, 1])
sns.boxplot(x="BldgType", y="SalePrice", data=train, ax=axs[1, 0])
plt.tight_layout()


# %% SalePrice distribution w.r.t YearBuilt / Neighborhood
fig, axs = plt.subplots(1, 2, figsize=(15, 5))
sns.scatterplot(x="YearBuilt", y="SalePrice", data=train, ax=axs[0])
sns.boxplot(x="Neighborhood", y="SalePrice", data=train, ax=axs[1])
plt.xticks(rotation=90)
plt.tight_layout()


# %%
from sklearn.dummy import DummyRegressor
from sklearn.metrics import mean_squared_log_error
import numpy as np


def evaluate(reg, x, y):
    pred = reg.predict(x)
    result = np.sqrt(mean_squared_log_error(y, pred))
    return f"RMSLE score: {result:.3f}"


dummy_reg = DummyRegressor()

dummy_selected_columns = ["MSSubClass"]
dummy_train_x = train[dummy_selected_columns]
dummy_train_y = train["SalePrice"]

dummy_reg.fit(dummy_train_x, dummy_train_y)
print("Training Set Performance")
print(evaluate(dummy_reg, dummy_train_x, dummy_train_y))

truth = pd.read_csv("truth_house_prices.csv")
dummy_test_x = test[dummy_selected_columns]
dummy_test_y = truth["SalePrice"]

print("Test Set Performance")
print(evaluate(dummy_reg, dummy_test_x, dummy_test_y))

print("Can you do better than a dummy regressor?")


# %% your solution to the regression problem
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import make_pipeline
from sklearn.impute import SimpleImputer

# Preprocess the data
selected_columns = ["MSSubClass", "OverallQual", "YearBuilt"]
train_x = train[selected_columns]
train_y = train["SalePrice"]

test_x = test[selected_columns]

# Create a pipeline that imputes missing values and fits a random forest regressor
reg = make_pipeline(
    SimpleImputer(strategy="median"),
    RandomForestRegressor(random_state=2020),
)

# Fit the model on the training data
reg.fit(train_x, train_y)

# Evaluate the model on the training and test sets
print("Training Set Performance")
print(evaluate(reg, train_x, train_y))

print("Test Set Performance")
print(evaluate(reg, test_x, dummy_test_y))