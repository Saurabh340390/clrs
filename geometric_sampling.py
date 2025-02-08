# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt

# probability of success is 0.3 (30%)
p = 0.3

# number of samples
num_samples = 1000000

# simulation based 
def sample_gemoteric_rv_simulation(p):
    n=0
    while np.random.uniform(0,1) >= p:
        n += 1
    return n + 1

# lograthim based
def sample_geometric_rv_logarithm(p):
    return int(np.log(np.random.uniform(0,1)) / np.log(1-p)) + 1

# generate sample
simulation_samples = [sample_gemoteric_rv_simulation(p) for _ in range(num_samples)]
logarithm_samples = [sample_geometric_rv_logarithm(p) for _ in range(num_samples)]

#plot histogram

plt.figure(figsize=(10,5))
plt.hist(simulation_samples, bins=range(1,20), alpha=0.5, label="Simulation-Based", density=True)
plt.hist(logarithm_samples, bins=range(1,20), alpha=0.5, label="lograthim-Based", density=True)
plt.xlabel("Number of Trials (n)")
plt.ylabel("probability Density")
plt.title("comparision of geometric sampling method")
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
