import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# -----------------------------
# 1. SETUP & LOAD DATASET
# -----------------------------
# Resolve paths relative to this script
base_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(base_dir, "plots")
data_path = os.path.join(base_dir, "data.csv")

# Create plots directory
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    print(f"Created directory: {output_dir}")

# Handle path
if os.path.exists(data_path):
    df = pd.read_csv(data_path)
else:
    print(f"Warning: {data_path} not found, generating synthetic data.")
    np.random.seed(42)
    n = 500
    df = pd.DataFrame({
        'RM': np.random.normal(6, 0.7, n),
        'DIS': np.random.exponential(4, n) + 1,
        'LSTAT': np.random.uniform(2, 35, n)
    })
    df['MEDV'] = 10 + 5 * df['RM'] - 0.5 * df['DIS'] - 0.5 * df['LSTAT'] + np.random.normal(0, 3, n)
    df['MEDV'] = np.maximum(0, df['MEDV'])

RM = df["RM"]
DIS = df["DIS"]
LSTAT = df["LSTAT"]
MEDV = df["MEDV"]

df_sorted = df.sort_values(by="RM")
RM_sorted = df_sorted["RM"]

print("Generating plots...")

# -----------------------------
# PLOT 1: RM SCATTER
# -----------------------------
plt.figure(figsize=(10, 6))
plt.scatter(RM, MEDV, alpha=0.6, edgecolors='w')
plt.xlabel("RM (Average number of rooms)")
plt.ylabel("MEDV (House price $1000s)")
plt.title("Relation entre RM et MEDV (Scatter)")
plt.grid(True, linestyle='--', alpha=0.5)
filename = os.path.join(output_dir, "01_RM_vs_MEDV.png")
plt.savefig(filename)
plt.close()
print(f"Saved {filename}")

# -----------------------------
# PLOT 2: DIS SCATTER
# -----------------------------
plt.figure(figsize=(10, 6))
plt.scatter(DIS, MEDV, color='green', alpha=0.6, edgecolors='w')
plt.xlabel("DIS (Distance au centre-ville)")
plt.ylabel("MEDV (House price $1000s)")
plt.title("Relation entre DIS et MEDV (Scatter)")
plt.grid(True)
filename = os.path.join(output_dir, "02_DIS_vs_MEDV.png")
plt.savefig(filename)
plt.close()
print(f"Saved {filename}")

# -----------------------------
# PLOT 3: LSTAT SCATTER
# -----------------------------
plt.figure(figsize=(10, 6))
plt.scatter(LSTAT, MEDV, color='purple', alpha=0.6, edgecolors='w')
plt.xlabel("% LSTAT (Population à faible revenu)")
plt.ylabel("MEDV (House price $1000s)")
plt.title("Relation entre LSTAT et MEDV")
plt.grid(True)
filename = os.path.join(output_dir, "03_LSTAT_vs_MEDV.png")
plt.savefig(filename)
plt.close()
print(f"Saved {filename}")

# -----------------------------
# PLOT 4: SIMPLE LINE SUBPLOT
# -----------------------------
fig, axes = plt.subplots(figsize=(8, 6))
axes.scatter(RM, MEDV, c='r', alpha=0.5, label='Data Points')
axes.set_xlabel("RM")
axes.set_ylabel("MEDV")
axes.set_title("Prix des maisons en fonction du nombre de pièces")
axes.legend()
axes.grid(True)
filename = os.path.join(output_dir, "04_RM_vs_MEDV_Subplot.png")
plt.savefig(filename)
plt.close()
print(f"Saved {filename}")

# -----------------------------
# PLOT 5: SIDE BY SIDE
# -----------------------------
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 5))

axes[0].scatter(LSTAT, MEDV, alpha=0.5)
axes[0].set_title("MEDV vs LSTAT")
axes[0].set_xlabel("LSTAT")
axes[0].set_ylabel("MEDV")
axes[0].grid(True)

axes[1].scatter(DIS, MEDV, color='orange', alpha=0.5)
axes[1].set_title("MEDV vs DIS")
axes[1].set_xlabel("DIS")
axes[1].set_ylabel("MEDV")
axes[1].grid(True)

plt.tight_layout()
filename = os.path.join(output_dir, "05_SideBySide.png")
plt.savefig(filename)
plt.close()
print(f"Saved {filename}")

# -----------------------------
# PLOT 6: 2x2 GRID
# -----------------------------
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 10))

axes[0][0].scatter(RM, MEDV, s=10)
axes[0][0].set_title("RM vs MEDV")

axes[0][1].scatter(LSTAT, MEDV, color='g', s=10)
axes[0][1].set_title("LSTAT vs MEDV")

axes[1][0].scatter(DIS, MEDV, color='r', s=10)
axes[1][0].set_title("DIS vs MEDV")

axes[1][1].plot(df.index, MEDV, alpha=0.5)
axes[1][1].set_title("MEDV par Index")

plt.tight_layout()
filename = os.path.join(output_dir, "06_Grid_2x2.png")
plt.savefig(filename)
plt.close()
print(f"Saved {filename}")

# -----------------------------
# PLOT 7: MATH CURVES (SORTED)
# -----------------------------
fig = plt.figure(figsize=(8, 6))
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax.plot(RM_sorted, RM_sorted**2, label="RM^2", linewidth=2)
ax.plot(RM_sorted, RM_sorted**3, label="RM^3", linewidth=2)
ax.set_xlabel("RM (Sorted)")
ax.set_ylabel("Valeurs transformées")
ax.set_title("Fonctions mathématiques")
ax.legend()
ax.grid(True)
filename = os.path.join(output_dir, "07_Math_Curves.png")
plt.savefig(filename)
plt.close()
print(f"Saved {filename}")

# -----------------------------
# PLOT 8: TREND COMPARISON
# -----------------------------
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(RM, MEDV, c='blue', alpha=0.3, label="Original Data")
ax.plot(RM_sorted, RM_sorted * 5, 'g--', label="Linear Trend", linewidth=2)
ax.plot(RM_sorted, RM_sorted * 4 + 10, color="#FF8C00", label="Offset Trend", linewidth=2)
ax.set_title("Comparaison de tendances")
ax.legend()
filename = os.path.join(output_dir, "08_Trend_Comparison.png")
plt.savefig(filename)
plt.close()
print(f"Saved {filename}")

# -----------------------------
# PLOT 9: MIXED TYPES
# -----------------------------
indices = np.arange(len(MEDV))
sorted_medv = np.sort(MEDV)

fig, axes = plt.subplots(1, 4, figsize=(16, 4))

axes[0].scatter(RM, MEDV, alpha=0.5)
axes[0].set_title("Scatter")

axes[1].step(indices, sorted_medv, lw=1)
axes[1].set_title("Step (Sorted)")

axes[2].bar(indices[:15], MEDV[:15], color='skyblue', edgecolor='black')
axes[2].set_title("Bar (First 15)")

axes[3].plot(RM_sorted, RM_sorted*4, color='black', alpha=0.3)
axes[3].fill_between(RM_sorted, RM_sorted*4 - 5, RM_sorted*4 + 5, color="green", alpha=0.3)
axes[3].set_title("Fill Area")

plt.tight_layout()
filename = os.path.join(output_dir, "09_Mixed_Types.png")
plt.savefig(filename)
plt.close()
print(f"Saved {filename}")

print(f"Done. Check the '{output_dir}' directory.")
