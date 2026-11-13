# CSPC
Needs to be updated, will be updated soon....

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



## PW3

**Data:** Heart Disease (Cleveland), from Kaggle
(https://www.kaggle.com/datasets/ritwikb3/heart-disease-cleveland), which
derives from the UCI Heart Disease dataset. The chemicals dataset is synthetic.

**Normality verdicts (histogram, Q-Q plot, Shapiro-Wilk):**

| Variable | Shape | Shapiro p | Verdict |
|---|---|---|---|
| age | [..] | [..] | [normal / not normal] |
| chol | [..] | [..] | [..] |
| trestbps | [..] | [..] | [..] |
| thalach | [..] | [..] | [..] |

[Reasoning: say where the plot and the test agree or disagree, and which you
trust.]

**Heart rate, disease vs healthy:**
- Test used: [Welch t-test or Mann-Whitney, and why, based on thalach's normality]
- Welch t = -7.86, p = 9e-14; Mann-Whitney p = 2e-13
- disease: 139.3 ± 1.9 bpm, healthy: 158.4 ± 1.5 bpm (mean ± SEM)
- Conclusion: [the groups differ, and the plot agrees]

**Age vs thalach:** Pearson r = -0.39, Spearman rho = -0.39. [One or two
sentences: older patients tend to have a lower maximum heart rate.]

**Chemical mystery:**
- Naive: cadmium r = 0.88, benzene r = 0.38, so cadmium looks like the cause.
- After holding pollution roughly fixed: [what happened to each correlation]
- Conclusion: [which chemical is the real cause, which one only looked guilty,
  and how the pollution-group analysis shows it]

**Bonus:** [entropy of `target` in bits and what it means]
