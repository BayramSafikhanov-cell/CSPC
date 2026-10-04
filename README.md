# CSPC
TEsting branch commit

## PW1 --- Lab B

The observed decay counts closely follow the analytical curve N0·e^(−λt) with λ = 0.3 —
the scattered observed points track the smooth theoretical curve closely, with only small
deviations. The Snakemake pipeline regenerates figure.png from decay_observed.csv by
running plot.py, and only reruns when the CSV or script has changed since the last build.

## PW2 - Lab A: Motion from Tracking Data

**Mean acceleration:** -8.58 m/s² (close to -9.81; edge points in np.gradient add some skew)

**Why acceleration is noisy:** Because differentiation divides by a small time step (0.1 s), small noise in the position measurements gets magnified — and acceleration comes from two derivatives in a row, so the noise is magnified twice.

**Integration check:** recovering position by integrating the noisy acceleration back up matched the original within 0.78 m, showing integration suppresses the noise that differentiation amplified.