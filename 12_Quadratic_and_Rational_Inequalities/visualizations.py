"""
Visualizations: Quadratic & Rational Inequalities  |  Phase 1 — Topic 1.17
"""
try:
    import matplotlib.pyplot as plt
    import numpy as np
except ImportError:
    print("pip install matplotlib numpy"); exit()

fig, axes = plt.subplots(1, 3, figsize=(16, 5))
fig.suptitle("1.17 Pertidaksamaan Kuadrat & Rasional", fontsize=13, fontweight="bold")

x = np.linspace(-5, 7, 1000)

# Plot 1: Quadratic inequality with solution region
ax1 = axes[0]
ax1.set_title("x²-5x+6 > 0\nSolusi: x<2 atau x>3")
y = x**2 - 5*x + 6
ax1.plot(x, y, "b-", lw=2, label="y = x²-5x+6")
ax1.axhline(0, color="black", lw=0.8)
ax1.fill_between(x, 0, y, where=(y>0), alpha=0.25, color="green", label="y > 0 (solusi)")
ax1.fill_between(x, y, 0, where=(y<0), alpha=0.25, color="red",   label="y < 0")
ax1.plot([2,3],[0,0],"ro",markersize=10,zorder=5)
ax1.axvline(2,color="red",linestyle=":",lw=1.5)
ax1.axvline(3,color="red",linestyle=":",lw=1.5)
ax1.set_ylim(-3,8); ax1.set_xlim(-1,6)
ax1.grid(True,alpha=0.3); ax1.legend(fontsize=8)

# Plot 2: Rational inequality sign chart
ax2 = axes[1]
ax2.set_title("(x-1)/(x+2) > 0\nSolusi: x<-2 atau x>1")
x2 = np.linspace(-6, 5, 1000)
y2 = np.where(np.abs(x2+2) > 0.05, (x2-1)/(x2+2), np.nan)
ax2.plot(x2, y2, "b-", lw=2, label="(x-1)/(x+2)")
ax2.axhline(0, color="black", lw=0.8)
ax2.fill_between(x2, 0, y2, where=((y2 > 0) & np.isfinite(y2)),
                 alpha=0.25, color="green", label="y > 0 (solusi)")
ax2.fill_between(x2, y2, 0, where=((y2 < 0) & np.isfinite(y2)),
                 alpha=0.25, color="red", label="y < 0")
ax2.axvline(-2, color="red", linestyle="--", lw=2, label="VA: x=-2")
ax2.set_ylim(-5, 5); ax2.set_xlim(-6, 5)
ax2.grid(True, alpha=0.3); ax2.legend(fontsize=8)

# Plot 3: |2x-1| > x+2 solution
ax3 = axes[2]
ax3.set_title("|2x-1| > x+2\nSolusi: x<-1/3 atau x>3")
x3 = np.linspace(-3, 6, 500)
ax3.plot(x3, np.abs(2*x3-1), "b-", lw=2, label="|2x-1|")
ax3.plot(x3, x3+2, "r-", lw=2, label="x+2")
ax3.fill_between(x3, np.abs(2*x3-1), x3+2,
                 where=(np.abs(2*x3-1) > x3+2),
                 alpha=0.25, color="green", label="|2x-1|>x+2")
ax3.axvline(-1/3, color="green", linestyle=":", lw=2)
ax3.axvline(3, color="green", linestyle=":", lw=2)
ax3.axhline(0,"black",lw=0.6); ax3.set_ylim(-2,10)
ax3.grid(True, alpha=0.3); ax3.legend(fontsize=8)

plt.tight_layout()
plt.savefig("/home/therabitt/Projects/Math/01_Algebra/12_Quadratic_and_Rational_Inequalities/quadratic_rational_ineq.png",
            dpi=110, bbox_inches="tight")
print("Saved: quadratic_rational_ineq.png")
plt.show()
