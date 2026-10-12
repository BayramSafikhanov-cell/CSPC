"""
PW2 Lab B Part 3 -- fit a reaction's rate constant to measured data.

A first-order reaction decays as  C(t) = C0 * exp(-k*t).  You have noisy
concentration-vs-time measurements; find the k that best matches them.
Complete the TODOs. Run:  python kinetics.py
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# TODO 1: read kinetics.csv (columns time, concentration) into arrays t, C.
#         Set C0 = the first concentration.

# TODO 2: write total_error(k) = sum of (measured - C0*exp(-k*t))^2.
#         This is the "how bad" number: small when the model matches the data.

# TODO 3: minimise total_error with scipy.optimize.minimize (method "SLSQP",
#         bounds [(0, 5)], start x0=0.5). Print the fitted k.

# TODO 4: plot the measured data (points) and your fitted curve (line) together.
#         Save as kinetics.png.
