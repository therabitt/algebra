"""
Visualizations: Polynomials  |  Phase 1 — Topic 1.9
"""
try:
    import matplotlib.pyplot as plt
    import numpy as np
except ImportError:
    print("pip install matplotlib numpy"); exit()

fig, axes = plt.subplots(1, 2, figsize=(13, 5))
fig.suptitle("1.9 Polinomial", fontsize=14, fontweight="bold")

x = np.linspace(-3, 4, 400)

# Plot 1: Polynomial with roots highlighted
ax1 = axes[0]
ax1.set_title("P(x) = (x+1)(x-1)(x-3) = x³-3x²-x+3")
p = lambda v: v**3 - 3*v**2 - v + 3
y = p(x)
ax1.plot(x, y, "b-", lw=2, label="P(x)")
ax1.axhline(0,"black",lw=0.8)
ax1.axvline(0,"black",lw=0.5)
for r in [-1, 1, 3]:
    ax1.plot(r, 0, "ro", markersize=10, zorder=5)
    ax1.text(r+0.1, 0.5, f"x={r}", fontsize=9)
ax1.set_ylim(-8, 12); ax1.grid(True,alpha=0.3); ax1.legend()

# Plot 2: End behavior comparison
ax2 = axes[1]
ax2.set_title("Perilaku Ujung: Derajat Genap vs Ganjil")
x2 = np.linspace(-2, 2, 400)
ax2.plot(x2, x2**2,   "b-",  lw=2, label="x² (genap, +): ↑↑")
ax2.plot(x2, -x2**2,  "b--", lw=2, label="-x² (genap, -): ↓↓")
ax2.plot(x2, x2**3,   "r-",  lw=2, label="x³ (ganjil, +): ↓↑")
ax2.plot(x2, -x2**3,  "r--", lw=2, label="-x³ (ganjil, -): ↑↓")
ax2.axhline(0,"black",lw=0.8); ax2.axvline(0,"black",lw=0.5)
ax2.set_ylim(-5,5); ax2.grid(True,alpha=0.3); ax2.legend(fontsize=8)

plt.tight_layout()
plt.savefig("/home/therabitt/Projects/Math/01_Algebra/14_Polynomials/polynomials.png",
            dpi=110, bbox_inches="tight")
print("Saved: polynomials.png"); plt.show()
