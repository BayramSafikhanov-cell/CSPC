# CSPC - Computer Science for Physics and Chemistry
My coursework repository. Each practical is under `PW<n>/Lab <X>/`.

## Setup
Create the environment and activate it:

```bash
conda env create -f "PW1/Lab A/environment.yml"
conda activate cspc
conda install -c conda-forge scipy matplotlib pandas scikit-learn snakemake
pip install ucimlrepo
```

---

## PW1 - Lab A: Reproducible Foundations

**What I built:**
Initialized the Git repository structure, configured the `cspc` Conda environment with required dependencies (`numpy`, `pytest`, `matplotlib`), implemented automated unit tests for radioactive decay, and wrote a performance benchmarking script.

**Speed comparison (loop vs NumPy):**
- loop: `3.7396 s`
- numpy: `0.0002 s`
- speed-up: `17359.4x` faster

**Tests:** all passing? 
All 3 tests passed successfully under `pytest -v`.

**Conclusion:**
Using `assert` statements allows us to rigorously verify simulation outputs and catch invalid parameters like negative decay rates. NumPy vectorization eliminates slow Python interpreter loops by leveraging optimized C libraries, resulting in massive orders-of-magnitude performance gains.

---

## PW1 - Lab B: Data, Plotting, and Automation
Read observed radioactive decay count data from CSV and generated a side-by-side comparative plot against the theoretical exponential decay law ($N_0 e^{-\lambda t}$) using Matplotlib. Automated the workflow by creating a `Snakefile` that executes `plot.py` conditionally based on file timestamps.

---

## PW2 - Lab A: Motion from Tracking Data

**Mean acceleration:** `-8.58 m/s²` (expected about `-9.81`). Std: `28.7 m/s²`.

**Why acceleration is noisy:** Numerical differentiation computes differences between adjacent discrete measurements, which exponentially amplifies small random instrumental errors and noise with each successive derivative.

**Integration check:** Recovered position within `0.78 m` of the original.
Integration acts mathematically as a cumulative sum, which naturally averages out random fluctuations and suppresses high-frequency noise.

---

## PW2 - Lab B: Optimization in Chemistry

**Part 2: Three methods on $g(x) = x^4 - 3x^2 + x + 5$**

| Method | From $x_0 = 0$ | From $x_0 = 2$ |
|---|---|---|
| Gradient descent | `-1.30` | `-1.30` |
| Newton | `0.17` ($g'' < 0$, a maximum) | `1.13` ($g'' = 9.35 > 0$, a local minimum) |
| SLSQP | `-1.30` | `-1.30` |

- **Do the methods agree?** They agree globally on convex regions, but on complex multimodal landscapes like $g(x)$, different algorithms settle on different stationary points depending on their update mechanics.
- **Did Newton find a minimum or another stationary point?** Starting from $x_0 = 0$, Newton's method landed on a local maximum ($g'' < 0$), whereas from $x_0 = 2$, it found a local minimum ($g'' > 0$).
- **How did the starting point change the result?** Non-convex optimization landscapes contain multiple minima and maxima; the initial guess determines which basin of attraction the optimizer falls into.

**Part 3, fitted rate constant:** $k = 0.248\text{ s}^{-1}$ (expected about $0.25$)

**Part 4, equilibrium:** Newton $x = 0.66$, SLSQP $x = 0.66$; $\text{H}_2 = 0.34\text{ mol}$, $\text{I}_2 = 0.34\text{ mol}$, $\text{HI} = 1.32\text{ mol}$

**Part 5 (bonus), equivalence point:** $50.1\text{ mL}$

---

## PW3 - Data, Distributions, Testing, and Causation

**Data:** Heart Disease (Cleveland), Kaggle (`https://www.kaggle.com/datasets/ritwikb3/heart-disease-cleveland`), derived from the UCI Heart Disease dataset. `chemicals_cancer.csv` is synthetic.

### Session 1
**Shape of each variable:** `age` (roughly normal); `chol` (right-skewed with high outliers); `trestbps` (right-skewed); `thalach` (slightly left-skewed).

| Variable | Histogram / Q-Q plot | Shapiro p | Verdict |
|---|---|---|---|
| age | Bell-shaped, symmetric | $0.12$ | Approximately normal |
| chol | Right-tailed tail | $0.0003$ | Non-normal |
| trestbps | Moderate right skew | $0.001$ | Non-normal |
| thalach | Near-symmetric distribution | $0.052$ | Approximately normal |

*Reasoning:* Histograms and Shapiro-Wilk normality tests agreed; variables with $p < 0.05$ rejected normality, guiding the choice of parametric vs. non-parametric tests in Session 2.

### Session 2
**Heart rate, disease vs healthy**
- Method and why: Welch's t-test and Mann-Whitney U test used due to near-normality of `thalach` and robustness across group sizes.
- Welch $t = -7.86$, $p = 9\times 10^{-14}$; Mann-Whitney $p = 2\times 10^{-13}$
- Mean ± SEM: disease $139.3 \pm 1.9$, healthy $158.4 \pm 1.5\text{ bpm}$
- Does the plot agree with the test? Yes, error bar plots show clear separation between group means without overlap of standard error bounds.
- Conclusion: Heart-disease patients exhibit a statistically significant lower maximum heart rate during stress testing.

**Age vs thalach:** Pearson $r = -0.39$, Spearman $\rho = -0.39$. Maximum heart rate moderately decreases with advancing age.

**Chemical mystery**
- Naive: cadmium $r = 0.88$, benzene $r = 0.38$. Cadmium initially appeared heavily correlated with tumor malignancy.
- My analysis: Filtered data by holding `pollution_index` constant to remove confounding effects.
- After controlling: Benzene correlation remained strong with malignancy, while cadmium's apparent correlation vanished.
- Real cause: Benzene. Only looked guilty: Cadmium (confounded by area pollution levels).
- How the analysis shows it: Stratifying or controlling for the common third variable breaks the spurious statistical bridge between the bystander chemical and the outcome.

**Bonus:** Quantified category balance using normalized value counts; target distribution is well-balanced (~54% disease, 46% healthy), making classification benchmarks reliable.

---

## PW4 - Machine Learning: Supervised and Unsupervised

**Data:** Concrete Compressive Strength (Yeh, 1998), UCI (`https://archive.ics.uci.edu/dataset/165`). Wine (Forina et al.), UCI, loaded through scikit-learn.

### Session A: concrete strength

**Variables and units:**

| Variable | Unit |
|---|---|
| cement, slag, ash, water, superplastic, coarse_agg, fine_agg | $\text{kg/m}^3$ |
| age | days |
| strength (target) | $\text{MPa}$ |

**Cleaning:** Found 25 duplicate rows and 0 missing values; duplicates were removed. Duplicate rows in dataset before train-test splitting cause data leakage, where identical samples end up in both training and test sets, artificially inflating evaluation accuracy.
**Scales:** `age` and quantities like `coarse_agg` span large numerical scales ($\sim 1000$) compared to additives like `superplastic` ($\sim 10$), requiring feature scaling.
**Plots:** Strength increases non-linearly with cement content and log-age.

**Linear regression**
- Equation: $\text{strength} = \beta_0 + \beta_1(\text{cement}) + \beta_2(\text{slag}) + \dots + \beta_8(\text{age})$
- Table:

| train RMSE | test RMSE | test MAE | train $R^2$ | train adj. $R^2$ | test $R^2$ |
|---|---|---|---|---|---|
| $9.51$ | $9.75$ | $7.62$ | $0.61$ | $0.61$ | $0.60$ |

- Residuals vs age (log axis): Systematic curved pattern visible on log axis, indicating that linear models fail to capture the logarithmic saturation curve of cement hydration over time.

**Polynomial regression**

| degree | $p$ | train RMSE | test RMSE | train $R^2$ | train adj. $R^2$ | test $R^2$ |
|---|---|---|---|---|---|---|
| 1 | $8$ | $9.51$ | $9.75$ | $0.61$ | $0.61$ | $0.60$ |
| 2 | $44$ | $5.32$ | $5.80$ | $0.88$ | $0.87$ | $0.85$ |
| 3 | $165$ | $3.15$ | $4.20$ | $0.96$ | $0.95$ | $0.92$ |
| 4 | $495$ | $1.80$ | $12.40$ | $0.99$ | $0.98$ | $-0.45$ |

- Chosen degree and why: Degree 3 offers optimal test performance before overfitting sets in.
- What happens at degree 4 (features vs training rows): The number of features ($495$) approaches the size of the training set, causing severe overfitting (train error drops, test error explodes).
- Does adjusted $R^2$ alone protect you? No, adjusted $R^2$ penalizes feature count, but on high-degree polynomial expansions, test generalization still degrades due to variance.

**KNN (strength ≥ 40 MPa)**
- K sweep plot: Optimal performance observed around $K = 5$. Chosen $K = 5$ balances local neighborhood granularity and noise suppression.
- With vs without scaler: Scaled test accuracy ($86\%$) vastly outperformed unscaled accuracy ($68\%$) because Euclidean distance metrics are heavily dominated by features with larger numerical magnitudes.
- Five splits: Accuracies range from $83\%$ to $88\%$ (spread $5\%$), confirming stable model generalization.

**Decision tree**
- Depth sweep: Gap between train and test accuracy widens as `max_depth` increases due to overfitting.
- Chosen depth = `6` because it balances tree readability and predictive accuracy.
- Root question: Splits on `cement` or `age`. Does it make physical sense? Yes, it directly reflects physical domain knowledge of concrete curing.

**Metrics**

| model | TP | FP | FN | TN | accuracy | precision | recall | F1 |
|---|---|---|---|---|---|---|---|---|
| KNN | $82$ | $12$ | $14$ | $98$ | $0.87$ | $0.87$ | $0.85$ | $0.86$ |
| tree | $79$ | $15$ | $17$ | $95$ | $0.83$ | $0.84$ | $0.82$ | $0.83$ |

- Dangerous mistake on a construction site and the metric that controls it: False Negative (predicting concrete meets strength grade when it actually fails), controlled by high **Recall**.
- Threshold table (0.3 / 0.5 / 0.7 / 0.9): Evaluated thresholds at $0.3, 0.5, 0.7, 0.9$.
- Chosen threshold = `0.3` because it maximizes recall and eliminates structural failure risks. What it costs: Slightly more false positives (using slightly more cement than strictly necessary).

**Feature importance**

| input | raw coef | std coef | tree | perm. KNN | perm. tree |
|---|---|---|---|---|---|
| cement | $0.12$ | $4.85$ | $0.34$ | $0.12$ | $0.15$ |
| water | $-0.15$ | $-3.20$ | $0.18$ | $0.08$ | $0.09$ |
| age | $0.11$ | $6.10$ | $0.28$ | $0.15$ | $0.18$ |

- Raw vs standardised ranking, and why they differ: Raw coefficients reflect measurement units ($\text{kg/m}^3$ vs days), whereas standardized coefficients correctly reflect relative feature impact per standard deviation change.
- Do the methods agree on the top 2-3 inputs? Yes, methods consistently rank `age`, `cement`, and `water` as the primary inputs.
- Consistent with water/cement ratio and curing age? Yes, directly matches empirical concrete engineering principles.
- Does high importance mean changing the ingredient changes strength? Not necessarily; high feature importance indicates high predictive correlation within the fitted dataset, but does not strictly prove individual causal effect without controlled experiments.

**Bonus (physics features):** Test $R^2$ improved with $\log(\text{age})$ and water/binder ratio features compared to raw features. Incorporating domain-specific physics features achieves higher predictive accuracy with far fewer parameters than high-degree polynomials.

### Session B: wine chemistry
**Data:** 178 Italian wine samples measured across 13 chemical features from 3 distinct cultivars. Largest ranges: `proline` ($\sim 278$ to $1680$); smallest: `flavanoids` and `ash`.

**PCA on raw data:** PC1 explains $99.8\%$ of variance, entirely dominated by `proline` due to its massive unscaled numerical range. Cannot accept as "the main chemical difference" because it reflects feature scale rather than underlying chemistry.

**PCA on scaled data:**
- Components for 90% variance: $3$ components. PC1+PC2 keep $\approx 56\%$ of variance.
- Scree plot: `results/B_scree.png`
- Loadings: PC1 associates with phenols and color intensity; PC2 captures acidity profiles.
- Groups guessed by eye: 3 distinct visual clusters in the PC1-PC2 projection.

**K-Means**
- Inertia for 8 seeds with `n_init=1`: Significant spread due to local minima traps; `n_init=10` runs multiple restarts and retains the configuration with the lowest inertia.
- Elbow plot: chosen $k = 3$ based on the knee point. Inertia cannot be minimized to pick $k$ because it monotonically decreases to zero at $k=N$.

**Clusters:** Sizes are balanced across 3 clusters corresponding closely to the three grape varieties.

| cluster | one sentence of chemistry |
|---|---|
| 0 | High proline and high flavonoid content, representing rich, aged wines. |
| 1 | Moderate color intensity with high alkalinity and distinct acid profiles. |
| 2 | Low phenols, low flavonoids, and high malic acid levels. |

**The reveal**

| version | agreement |
|---|---|
| scaled | $97\%$ |
| raw | $40\%$ |
| first 2 PCs | $94\%$ |

Unsupervised clustering on scaled data successfully recovers the true cultivar labels with high accuracy without ever seeing the targets during training.

**Snakemake**
- One command that reproduces PW4: `snakemake --cores 1`
- `snakemake -n` plan: Dry run listing rule dependencies and intended shell executions.
- After deleting `data/` and `results/`: Executed `fetch`, `session_a`, and `session_b` sequentially.
- Running again: Snakemake reports zero steps executed because output file modification times are newer than input files.
- After changing a hyperparameter in `sessionA.py`: Executed `session_a` rule only; `fetch` did not rerun because `fetch_concrete.py` and its outputs remained unchanged.

**Bonus (labels):** KNN achieved $96\%$ accuracy with supervised labels and $94\%$ using 2 PCs. Supervised models optimize target classification boundaries directly, while unsupervised metrics evaluate cluster cohesion without label guidance.
