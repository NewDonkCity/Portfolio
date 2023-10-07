# %%
from collections import Counter

import pyro
import torch
from tqdm import tqdm


# %%
def coin_toss(n):
    faces = Counter()
    total = 0
    for _ in tqdm(range(n)):
        # create a sample of Bernoulli distribution for fair (50/50) coin
        # The size of the sample is 1
        sample = pyro.sample("coin_toss", pyro.distributions.Bernoulli(0.5))

        # convert the Bernoulli distribution into meaning
        # what does 1/0 stands for ?
        face = "head" if sample.item() == 1.0 else "tail"

        # gain 2 if head is tossed, otherwise lose 2
        reward = {"head": 2, "tail": -2}[face]

        # update the faces Counter
        faces[face] += 1
        total += reward

    return faces, total


def coin_toss_tensor(n):
    # create a sample of Bernoulli distribution for fair (50/50) coin
    # The size of the sample is n
    samples = pyro.sample("coin_toss", pyro.distributions.Bernoulli(0.5).expand([n]))

    # return Counter object to summarize the counts of head/tail, and total rewards
    faces = Counter({"head": (samples == 1).sum().item(), "tail": (samples == 0).sum().item()})
    total = faces["head"] * 2 + faces["tail"] * -2

    return faces, total


def simulation(n, simulation_func):
    faces, total = simulation_func(n)

    print(f"\nRan {n} simulation{'s' if n >1 else ''}")
    print(f"Total Reward = {total}")
    print(faces)


# %%
for n in [1, 1000, 1000000]:
    simulation(n, coin_toss)


# %%
for n in [1, 1000, 1000000]:
    simulation(n, coin_toss_tensor)

# After running both, coin_toss_tensor is a lot faster than coin_toss