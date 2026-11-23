
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
for name in ["A", "B"]:
    d = pd.read_csv(f"data/seismogram_{name}.csv")
    print(name, d[["Z","N","E"]].mean().values, d[["Z","N","E"]].abs().max().values)

d = pd.read_csv("data/seismogram_A.csv")
t = d["time_s"].to_numpy()
Z = d["Z"].to_numpy()
N = d["N"].to_numpy()
E = d["E"].to_numpy()

fs = 1 / (t[1] - t[0])
print(fs, len(t), t[-1])  

fig, ax = plt.subplots(3, 1, sharex=True)   
ax[0].plot(t, Z * 1000)                  
ax[0].set_ylabel("Z (mm/s)")
plt.show()
ax[1].plot(t, N * 1000)
ax[1].set_ylabel("N (mm/s)")
ax[2].plot(t, E * 1000)
ax[2].set_ylabel("E (mm/s)")
ax[2].set_xlabel("Time (s)")
plt.savefig("figures/step1_channels.png", dpi=150)
ax[0].set_xlim(0, 60)
plt.savefig("figures/step1_zoom.png", dpi=150)




import os
os.makedirs("results", exist_ok=True)