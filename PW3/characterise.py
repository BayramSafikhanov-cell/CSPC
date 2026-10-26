import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# =============== SESSION 1: characterise the data ===============
df = pd.read_csv("heart.csv")
print(df.shape)
print(df.head())

cols = ["age", "chol", "trestbps", "thalach"]
print(df[cols].describe())

# task 2: distributions
fig, axes = plt.subplots(2, 2, figsize=(10, 8))
for ax, col in zip(axes.flat, cols):
    ax.hist(df[col], bins=20)
    ax.set_title(col)
plt.tight_layout()
plt.savefig("distributions.png")

# task 3: normality (graphical + numerical)
fig, axes = plt.subplots(2, 2, figsize=(10, 8))
for ax, col in zip(axes.flat, cols):
    stats.probplot(df[col], dist="norm", plot=ax)
    ax.set_title(col)
plt.tight_layout()
plt.savefig("qqplots.png")

for col in cols:
    stat, p = stats.shapiro(df[col])
    print(f"Shapiro {col}: W={stat:.3f}, p={p:.4f}")

# =============== SESSION 2: draw conclusions ===============
# task 4: do the groups differ?
disease = df[df["target"] == 1]["thalach"]
healthy = df[df["target"] == 0]["thalach"]

t_stat, t_p = stats.ttest_ind(disease, healthy, equal_var=False)
u_stat, u_p = stats.mannwhitneyu(disease, healthy)
print(f"Welch t-test: t={t_stat:.2f}, p={t_p:.2e}")
print(f"Mann-Whitney: U={u_stat:.0f}, p={u_p:.2e}")

# mean +- standard error of the mean
means = [disease.mean(), healthy.mean()]
sems = [stats.sem(disease), stats.sem(healthy)]
print("disease: mean", means[0], "+-", sems[0])
print("healthy: mean", means[1], "+-", sems[1])

plt.figure()
plt.errorbar(["disease", "healthy"], means, yerr=sems, fmt="o", capsize=6)
plt.ylabel("mean thalach (bpm), error bar = SEM")
plt.savefig("group_means.png")

# task 5: age vs thalach
r, r_p = stats.pearsonr(df["age"], df["thalach"])
rho, rho_p = stats.spearmanr(df["age"], df["thalach"])
print(f"Pearson r={r:.3f} (p={r_p:.2e}), Spearman rho={rho:.3f}")

plt.figure()
plt.scatter(df["age"], df["thalach"], alpha=0.6)
plt.xlabel("age")
plt.ylabel("thalach")
plt.savefig("age_thalach.png")

# =============== DATASET 2: the chemicals mystery ===============
df2 = pd.read_csv("chemicals_cancer.csv")
print(df2.columns.tolist())      # check the names, then fix these five:
BENZ, CADM, POLL, AGE, MAL = "benzene", "cadmium", "pollution_index", "age", "malignancy"
# task 6: naive analysis
for chem in (BENZ, CADM):
    print("naive", chem, "vs malignancy:", df2[chem].corr(df2[MAL]))

# task 7: hold the suspected third variable (pollution) roughly fixed
df2["pollution_group"] = pd.qcut(df2[POLL], 4)
for group, sub in df2.groupby("pollution_group", observed=True):
    print(group, "| benzene:", round(sub[BENZ].corr(sub[MAL]), 3),
          "| cadmium:", round(sub[CADM].corr(sub[MAL]), 3))

# bonus: how unpredictable is a category? (entropy in bits)
p = df["target"].value_counts(normalize=True)
print(p)
print("entropy (bits):", -(p * np.log2(p)).sum(), "(max for 2 classes is 1.0)")