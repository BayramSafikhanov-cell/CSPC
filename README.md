# CSPC
TEsting branch commit

## PW1 - Lab B: Data, Plotting, and Automation

The observed decay counts closely follow the analytical curve N0·e^(−λt) with λ = 0.3 —
the scattered observed points track the smooth theoretical curve closely, with only small
deviations. The Snakemake pipeline regenerates figure.png from decay_observed.csv by
running plot.py, and only reruns when the CSV or script has changed since the last build.

## PW2 - Lab A: Motion from Tracking Data

**Mean acceleration:** -8.58 m/s² (close to -9.81; edge points in np.gradient add some skew)

**Why acceleration is noisy:** Because differentiation divides by a small time step (0.1 s), small noise in the position measurements gets magnified — and acceleration comes from two derivatives in a row, so the noise is magnified twice.

**Integration check:** recovering position by integrating the noisy acceleration back up matched the original within 0.78 m, showing integration suppresses the noise that differentiation amplified.


## PW2 - Lab B: Optimization in Chemistry
| Method | Result | Where on the W |
|---|---|---|
| Gradient descent | -1.30 | bottom of the left valley |
| SLSQP | -1.30 | bottom of the left valley |
| Newton | 0.17 | top of the hill (a maximum) |

Newton doesn’t look for “downhill”. It looks for any spot where the slope is zero, and the nearest one to x = 0 is the top of the hill. The first step shows it:

At x = 0 the slope is +1, meaning g is rising as x increases. Gradient descent and SLSQP only care about going down, so they move left into the valley.