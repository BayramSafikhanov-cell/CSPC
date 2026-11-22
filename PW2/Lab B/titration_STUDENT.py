import numpy as np
import matplotlib.pyplot as plt

# TODO 1: read the data (header row, columns volume_base and pH)
data = np.loadtxt("titration.csv", delimiter=",", skiprows=1)
V, pH = data[:, 0], data[:, 1]

# TODO 2: slope of the pH curve, and where it is largest
slope = np.gradient(pH, V)
i = np.argmax(slope)
V_eq = V[i]
print("equivalence point:", V_eq, "mL")

# TODO 3: two plots side by side
fig, axes = plt.subplots(1, 2, figsize=(10, 4))

axes[0].plot(V, pH)
axes[0].axvline(V_eq, linestyle="--", color="red")
axes[0].set_xlabel("volume of base (mL)")
axes[0].set_ylabel("pH")

axes[1].plot(V, slope)
axes[1].axvline(V_eq, linestyle="--", color="red")
axes[1].set_xlabel("volume of base (mL)")
axes[1].set_ylabel("slope dpH/dV")

plt.tight_layout()
plt.savefig("titration.png")