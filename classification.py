# %% read data
import pandas as pd

train = pd.read_csv("titanic/train.csv")
test = pd.read_csv("titanic/test.csv")


# %% checkout out first few rows
train.head()


# %% checkout out dataframe info
train.info()


# %% describe the dataframe
train.describe(include="all")


# %% visualize the dataset, starting with the Survied distribution
import seaborn as sns

sns.countplot(x="Survived", data=train)


# %% Survived w.r.t Pclass / Sex / Embarked ?
sns.catplot(x="Pclass", y="Survived", kind="bar", data=train)
sns.catplot(x="Sex", y="Survived", kind="bar", data=train)
sns.catplot(x="Embarked", y="Survived", kind="bar", data=train)

# %% Age distribution ?
sns.displot(train["Age"].dropna())

# %% Survived w.r.t Age distribution ?
sns.displot(train, x="Age", hue="Survived")

# %% SibSp / Parch distribution ?
sns.countplot(x="SibSp", data=train)
sns.countplot(x="Parch", data=train)

# %% Survived w.r.t SibSp / Parch  ?
sns.catplot(x="SibSp", y="Survived", kind="bar", data=train)
sns.catplot(x="Parch", y="Survived", kind="bar", data=train)

# %% Dummy Classifier
from sklearn.dummy import DummyClassifier
from sklearn.metrics import f1_score


def evaluate(clf, x, y):
    pred = clf.predict(x)
    result = f1_score(y, pred)
    return f"F1 score: {result:.3f}"


dummy_clf = DummyClassifier(random_state=2020)

dummy_selected_columns = ["Pclass"]
dummy_train_x = train[dummy_selected_columns]
dummy_train_y = train["Survived"]

dummy_clf.fit(dummy_train_x, dummy_train_y)
print("Training Set Performance")
print(evaluate(dummy_clf, dummy_train_x, dummy_train_y))

truth = pd.read_csv("truth_titanic.csv")
dummy_test_x = test[dummy_selected_columns]
dummy_test_y = truth["Survived"]

print("Test Set Performance")
print(evaluate(dummy_clf, dummy_test_x, dummy_test_y))

print("Can you do better than a dummy classifier?")


# %% Your solution to this classification problem
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.impute import SimpleImputer

# Preprocess the data
selected_columns = ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare"]
train_x = train[selected_columns]
train_x = pd.get_dummies(train_x, columns=["Sex"])
train_y = train["Survived"]

test_x = test[selected_columns]
test_x = pd.get_dummies(test_x, columns=["Sex"])

# Create a pipeline that imputes missing values, scales the data, and fits a logistic regression model
clf = make_pipeline(
    SimpleImputer(strategy="median"),
    StandardScaler(),
    LogisticRegression(random_state=2020),
)

# Fit the model on the training data
clf.fit(train_x, train_y)

# Evaluate the model on the training and test sets
print("Training Set Performance")
print(evaluate(clf, train_x, train_y))

print("Test Set Performance")
print(evaluate(clf, test_x, dummy_test_y))

