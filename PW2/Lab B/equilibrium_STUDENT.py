import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton, minimize

K = 15.6
a = b = 1.0

# TODO 1: zero exactly at equilibrium
def k_imbalance(x):
    return (2 * x) ** 2 / ((a - x) * (b - x)) - K

# TODO 2: method 1, root-finding
x_newton = newton(k_imbalance, x0=0.5)

# TODO 3: method 2, minimise the squared imbalance
res = minimize(lambda x: k_imbalance(x[0]) ** 2, x0=[0.5],
               method="SLSQP", bounds=[(0, 0.999)])
x_slsqp = res.x[0]
print("newton:", x_newton, "| SLSQP:", x_slsqp)

# TODO 4: amounts and plot
x_eq = x_newton
H2, I2, HI = a - x_eq, b - x_eq, 2 * x_eq
print(f"H2 = {H2:.3f} mol, I2 = {I2:.3f} mol, HI = {HI:.3f} mol")

xs = np.linspace(0, 0.999, 200)
plt.figure()
plt.plot(xs, a - xs, label="H2")
plt.plot(xs, b - xs, "--", label="I2")
plt.plot(xs, 2 * xs, label="HI")
plt.axvline(x_eq, color="k", linestyle=":", label=f"equilibrium x = {x_eq:.3f}")
plt.xlabel("extent x (mol)")
plt.ylabel("amount (mol)")
plt.legend()
plt.savefig("equilibrium.png")