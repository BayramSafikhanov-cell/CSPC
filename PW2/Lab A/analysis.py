"""
PW2 Lab A -- Motion from tracking data.

Read noisy free-fall position measurements, then:
  - differentiate once  -> velocity
  - differentiate twice -> acceleration (should be ~ constant -g, but noisy!)
  - integrate the acceleration back up -> recover velocity and position

Complete the TODOs. Run:  python analysis.py
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid

# TODO 1: read freefall.csv into arrays t and y
data = np.loadtxt("freefall.csv", delimiter=",", skiprows=1)
t, y = data[:, 0], data[:, 1]

# TODO 2: compute velocity and acceleration
v = np.gradient(y, t)
a = np.gradient(v, t)

print("mean acceleration:", a.mean())
print("std acceleration:", a.std())

# TODO 3: integrate a back up to recover velocity and position
v_recovered = cumulative_trapezoid(a, t, initial=0) + v[0]
y_recovered = cumulative_trapezoid(v_recovered, t, initial=0) + y[0]

max_diff = np.max(np.abs(y - y_recovered))
print("max difference (recovered vs original position):", max_diff)

# TODO 4: three-panel plot
fig, axes = plt.subplots(3, 1, sharex=True, figsize=(8, 8))

axes[0].plot(t, y)
axes[0].set_ylabel("position (m)")

axes[1].plot(t, v)
axes[1].set_ylabel("velocity (m/s)")

axes[2].plot(t, a)
axes[2].axhline(-9.81, linestyle="--", color="red")
axes[2].set_ylabel("acceleration (m/s²)")
axes[2].set_xlabel("time (s)")

plt.tight_layout()
plt.savefig("motion.png")