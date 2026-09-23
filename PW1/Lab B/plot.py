"""
PW1 Lab B -- read observed decay data and compare it to the analytical law.
Produce a 1x2 figure:  left = observed data,  right = analytical N0*exp(-lam*t),
with SHARED axes so the two shapes are directly comparable.

Complete the TODOs below. Run with:  python plot.py
"""

import numpy as np
import matplotlib.pyplot as plt

LAMBDA = 0.3     # decay constant, given

# TODO 1: read decay_observed.csv into t and observed
t, observed = np.loadtxt("decay_observed.csv", delimiter=",", skiprows=1, unpack=True)

# TODO 2: N0 = first observed value, build analytical curve

N0 = observed[0]
analytical = N0 * np.exp(-LAMBDA * t)

# TODO 3: 1x2 subplot, shared x and y axes
fig, (ax1, ax2) = plt.subplots(1, 2, sharex=True, sharey=True)

ax1.scatter(t, observed)
ax1.set_title("Observed data")
ax1.set_xlabel("time")
ax1.set_ylabel("count")

ax2.plot(t, analytical)
ax2.set_title("Analytical: N0·e^(−λt)")
ax2.set_xlabel("time")

# TODO 4: save the figure
plt.savefig("figure.png")