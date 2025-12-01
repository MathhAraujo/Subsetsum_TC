from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

BASE_DIR = Path(__file__).resolve().parent
results_path = BASE_DIR.parent / "Results" / "results.xlsx"
output_dir = BASE_DIR.parent / "Results"

df = pd.read_excel(results_path)

df["sample_size"] = pd.cut(
    df["input_size"],
    bins=[4, 10, 19, 25],
    labels=["Pequeno", "Médio", "Grande"]
)

stats = df.groupby(["language", "sample_size"])["execution_time"].mean().unstack()

fig, ax = plt.subplots(figsize=(10, 6))
x = np.arange(len(stats.columns))
bar_width = 0.35

ax.bar(x - bar_width / 2, stats.loc["Python"], width=bar_width, label="Python", color="green")
ax.bar(x + bar_width / 2, stats.loc["Java"], width=bar_width, label="Java", color="red")

ticks = [0.01, 0.1, 1, 5, 10, 50, 100, 500, 1000, 1500]
ax.set_yscale("log")
ax.set_yticks(ticks)
ax.set_yticklabels([str(t) for t in ticks])

ax.set_xticks(x)
ax.set_xticklabels(stats.columns)
ax.set_title("Comparação de Desempenho: Python vs Java")
ax.legend()

fig.tight_layout()
fig.savefig(output_dir / "grafico_python_java_barras.png", dpi=300)
plt.close(fig)

stats_py = df[df["language"] == "Python"].groupby("sample_size")["execution_time"].mean()

fig, ax = plt.subplots(figsize=(10, 6))
green = "#4CAF50"

ax.plot(stats_py.index, stats_py.values, linewidth=4, color=green)
ax.fill_between(stats_py.index, stats_py.values, alpha=0.25, color=green)
ax.scatter(stats_py.index, stats_py.values, color=green, s=80)

ax.set_title("Python")
ax.grid(color="#cccccc", linestyle="--", linewidth=0.6, alpha=0.7)

fig.tight_layout()
fig.savefig(output_dir / "grafico_python_area.png", dpi=300)
plt.close(fig)

stats_java = df[df["language"] == "Java"].groupby("sample_size")["execution_time"].mean()

fig, ax = plt.subplots(figsize=(10, 6))
red = "#E53935"

ax.plot(stats_java.index, stats_java.values, linewidth=4, color=red)
ax.fill_between(stats_java.index, stats_java.values, alpha=0.25, color=red)
ax.scatter(stats_java.index, stats_java.values, color=red, s=80)

ax.set_title("Java")
ax.grid(color="#cccccc", linestyle="--", linewidth=0.6, alpha=0.7)

fig.tight_layout()
fig.savefig(output_dir / "grafico_java_area.png", dpi=300)
plt.close(fig)
