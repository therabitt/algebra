"""
Visualizations: Rational Expressions  |  Phase 1 — Topic 1.16
"""
try:
    import matplotlib.pyplot as plt
    import numpy as np
except ImportError:
    print("pip install matplotlib numpy"); exit()

fig, axes = plt.subplots(1, 2, figsize=(13, 5))
fig.suptitle("1.16 Pecahan Aljabar (Rational Expressions)", fontsize=14, fontweight="bold")

# Plot 1: Rational function with asymptotes
ax1 = axes[0]
ax1.set_title("f(x) = (2x+3)/(x-1) — Asymptotes")
x1 = np.linspace(-5, 0.95, 300)
x2 = np.linspace(1.05, 6, 300)
def f(x): return (2*x+3)/(x-1)
ax1.plot(x1, f(x1), "b-", lw=2)
ax1.plot(x2, f(x2), "b-", lw=2, label="f(x)=(2x+3)/(x-1)")
ax1.axvline(1, color="red", linestyle="--", lw=2, label="VA: x=1")
ax1.axhline(2, color="green", linestyle="--", lw=2, label="HA: y=2")
ax1.set_ylim(-15, 15); ax1.set_xlim(-5, 6)
ax1.axhline(0,"black",lw=0.6); ax1.axvline(0,"black",lw=0.6)
ax1.grid(True, alpha=0.3); ax1.legend(fontsize=9)

# Plot 2: Simplified vs original (show hole)
ax2 = axes[1]
ax2.set_title("Lubang (Hole) di x=2:\n(x^2-4)/(x-2) = x+2, x≠2")
x = np.linspace(-2, 5, 500)
y_original = np.where(np.abs(x-2) > 0.05, (x**2-4)/(x-2), np.nan)
y_simplified = x + 2
ax2.plot(x, y_simplified, "g--", lw=2, label="x+2 (simplified)", alpha=0.6)
ax2.plot(x, y_original, "b-", lw=2.5, label="(x^2-4)/(x-2)")
ax2.plot(2, 4, "ro", markersize=10, markerfacecolor="white",
         markeredgecolor="red", markeredgewidth=2.5, label="Hole di (2,4)")
ax2.axhline(0,"black",lw=0.6); ax2.axvline(0,"black",lw=0.6)
ax2.grid(True, alpha=0.3); ax2.legend(fontsize=9)

plt.tight_layout()
plt.savefig("/home/therabitt/Projects/Math/01_Algebra/15_Rational_Expressions/rational_expr.png",
            dpi=110, bbox_inches="tight")
print("Saved: rational_expr.png")
plt.show()
