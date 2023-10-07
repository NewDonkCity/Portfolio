# %%
import matplotlib.pyplot as plt
import pyro
import seaborn as sns
import torch
from pyro.infer.mcmc import HMC, MCMC
from sklearn.datasets import fetch_openml
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression


# Load MNIST dataset
mnist = fetch_openml("mnist_784")

x_train, x_test, y_train, y_test = train_test_split(
    mnist.data,
    mnist.target,
    test_size=0.2,
    random_state=2020,
)


# %%
# Create a DecisionTreeClassifier object and fit it with training data
clf_dt = DecisionTreeClassifier()
clf_dt.fit(x_train, y_train)


# %%
# Create a LogisticRegression object and fit it with training data
clf_lr = LogisticRegression()
clf_lr.fit(x_train, y_train)


# %%
# Get prediction label using clf_dt and print the accuracy score
y_pred_dt = clf_dt.predict(x_test)
accuracy_dt = accuracy_score(y_test, y_pred_dt)
print("DecisionTree Accuracy:", accuracy_dt)


# %%
# Get prediction label using clf_lr and print the accuracy score
y_pred_lr = clf_lr.predict(x_test)
accuracy_lr = accuracy_score(y_test, y_pred_lr)
print("LogisticRegression Accuracy:", accuracy_lr)


# %%
# Labels to be used in Monte Carlo method
y_dt = torch.Tensor(y_pred_dt == y_test)
y_lr = torch.Tensor(y_pred_lr == y_test)


# %%
def model(y_real):
    # Create a variable underlying_p for the Bernoulli distribution
    underlying_p = pyro.sample("underlying_p", pyro.distributions.Uniform(0, 1))

    # Create a hidden Bernoulli distribution with p = underlying_p
    y_hidden_dist = pyro.distributions.Bernoulli(probs=underlying_p)

    # Sample the label from the hidden Bernoulli distribution
    with pyro.plate("data", len(y_real)):
        y_real = pyro.sample("obs", y_hidden_dist, obs=y_real)
    return y_real

def monte_carlo(y):
    pyro.clear_param_store()

    # Create a Simple Hamiltonian Monte Carlo kernel with step_size of 0.1
    hmc_kernel = HMC(model=model, step_size=0.1)

    # Create a Markov Chain Monte Carlo method with:
    # the hmc_kernel, 500 samples, and 100 warmup iterations
    mcmc = MCMC(hmc_kernel, num_samples=500, warmup_steps=100)

    mcmc.run(y)

    sample_dict = mcmc.get_samples(num_samples=5000)
    plt.figure(figsize=(8, 6))
    sns.distplot(sample_dict["underlying_p"].numpy())
    plt.xlabel("Observed probability value")
    plt.ylabel("Observed frequency")
    plt.show()
    mcmc.summary(prob=0.95)

    return sample_dict


# %%
# Run the Monte Carlo method with y_dt and save the sample_dict with name simulations_dt
simulations_dt = monte_carlo(y_dt)


# %%
# Run the Monte Carlo method with y_lr and save the sample_dict with name simulations_lr
simulations_lr = monte_carlo(y_lr)


# %%
# Plot the results
plt.figure(figsize=(8, 6))
sns.distplot(
    simulations_dt["underlying_p"].numpy(),
    label="DecisionTree",
    color="red",
)
sns.distplot(
    simulations_lr["underlying_p"].numpy(),
    label="LogisticRegression",
    color="green",
)
plt.legend()
plt.show()

# LogisticRegression is better than DecisionTreeClassifier for this activity,
# as the simulation results of LogisticRegression generally have higher accuracy scores