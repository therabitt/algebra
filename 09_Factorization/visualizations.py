"""
Visualizations: Factorization  |  Phase 1 — Topic 1.10
"""
try:
    import matplotlib.pyplot as plt
    import numpy as np
except ImportError:
    print("pip install matplotlib numpy"); exit()

fig, axes = plt.subplots(1, 2, figsize=(13, 5))
fig.suptitle("1.10 Faktorisasi", fontsize=14, fontweight="bold")

x = np.linspace(-5, 5, 500)

ax1 = axes[0]
ax1.set_title("Hubungan Faktor dan Akar")
ax1.plot(x, x**2-5*x+6, "b-", lw=2, label="x²-5x+6 = (x-2)(x-3)")
ax1.axhline(0,"black",lw=0.8)
for r in [2,3]:
    ax1.plot(r, 0, "ro", markersize=12, zorder=5)
    ax1.text(r+0.1, 0.5, f"x={r}", fontsize=10)
ax1.set_ylim(-3,8); ax1.grid(True,alpha=0.3); ax1.legend()

ax2 = axes[1]
ax2.set_title("Selisih Kuadrat: x²-a² = (x+a)(x-a)")
a = 2
ax2.plot(x, x**2-a**2,  "b-",  lw=2, label=f"x²-{a**2}")
ax2.plot(x, (x+a),      "r--", lw=1.5, label=f"(x+{a})")
ax2.plot(x, (x-a),      "g--", lw=1.5, label=f"(x-{a})")
ax2.axhline(0,"black",lw=0.8)
ax2.set_ylim(-6,10); ax2.grid(True,alpha=0.3); ax2.legend()

plt.tight_layout()
plt.savefig("/home/therabitt/Projects/Math/01_Algebra/09_Factorization/factorization.png",
            dpi=110, bbox_inches="tight")
print("Saved: factorization.png"); plt.show()
