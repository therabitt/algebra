"""
Visualizations: Linear Equations  |  Phase 1 — Topic 1.4
"""
try:
    import matplotlib.pyplot as plt
    import numpy as np
except ImportError:
    print("pip install matplotlib numpy"); exit()

fig, axes = plt.subplots(1, 2, figsize=(12, 5))
fig.suptitle("1.4 Persamaan Linear", fontsize=14, fontweight="bold")

x = np.linspace(-3, 8, 300)

# Plot 1: f(x) = 2x+3, tunjukkan akar (solusi)
ax1 = axes[0]
ax1.set_title("2x + 3 = 11  →  x = 4")
y = 2*x + 3
ax1.plot(x, y, "b-", lw=2, label="y = 2x+3")
ax1.axhline(11, color="red", linestyle="--", lw=1.5, label="y = 11")
ax1.axvline(4, color="green", linestyle=":", lw=2, label="x = 4 (solusi)")
ax1.plot(4, 11, "ro", markersize=12, zorder=5, label="Titik solusi")
ax1.axhline(0, color="black", lw=0.6); ax1.axvline(0, color="black", lw=0.6)
ax1.grid(True, alpha=0.3); ax1.legend(fontsize=9)
ax1.set_ylim(-5, 20)

# Plot 2: Persamaan identitas vs kontradiksi vs unik
ax2 = axes[1]
ax2.set_title("Tipe Persamaan Linear")
x2 = np.linspace(-3, 5, 200)
ax2.plot(x2, 2*x2 + 3, "b-", lw=2, label="y=2x+3 (satu solusi saat =7)")
ax2.plot(x2, x2 + 1,   "g-", lw=2, label="y=x+1 (unik)")
ax2.plot(x2, 2*x2 + 3, "r--", lw=1.5, label="y=2x+3 lagi (identitas: 2x+3=2x+3)")
ax2.axhline(0, color="black", lw=0.6); ax2.axvline(0, color="black", lw=0.6)
ax2.grid(True, alpha=0.3); ax2.legend(fontsize=9)

plt.tight_layout()
plt.savefig("/home/therabitt/Projects/Math/01_Algebra/06_Linear_Equations/linear_eq.png",
            dpi=110, bbox_inches="tight")
print("Saved: linear_eq.png")
plt.show()
