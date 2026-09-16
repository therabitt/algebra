"""
Visualizations: Linear Inequalities  |  Phase 1 — Topic 1.5
"""
try:
    import matplotlib.pyplot as plt
    import matplotlib.patches as patches
    import numpy as np
except ImportError:
    print("pip install matplotlib numpy"); exit()

fig, axes = plt.subplots(1, 2, figsize=(13, 5))
fig.suptitle("1.5 Pertidaksamaan Linear", fontsize=14, fontweight="bold")

# Plot 1: Number line solutions
ax1 = axes[0]
ax1.set_title("Solusi pada Garis Bilangan")
ax1.set_xlim(-6, 8); ax1.set_ylim(-0.5, 4.5)
ax1.axhline(0, color="black", lw=0.5)

ineqs = [
    (1.0, r"x > 2",         2, None,  False, True,  "blue"),
    (2.0, r"x ≤ 4",         None, 4,  True, True,   "red"),
    (3.0, r"-1 < x < 5",   -1, 5,    False, False,  "green"),
    (4.0, r"|x| ≤ 3: -3≤x≤3", -3, 3, True, True,  "purple"),
]
for y, label, lo, hi, lc, rc, color in ineqs:
    ax1.axhline(y, color="gray", lw=0.5, linestyle=":")
    ax1.text(-5.8, y, label, fontsize=9, va="center", color=color)
    if lo is not None and hi is not None:
        ax1.hlines(y, lo, hi, color=color, lw=4, alpha=0.8)
        ax1.plot(lo, y, "o" if lc else "o", color=color, markersize=10,
                 markerfacecolor=color if lc else "white", markeredgecolor=color, markeredgewidth=2)
        ax1.plot(hi, y, "o", color=color, markersize=10,
                 markerfacecolor=color if rc else "white", markeredgecolor=color, markeredgewidth=2)
    elif lo is None:
        ax1.annotate("", xy=(-5.5, y), xytext=(hi, y),
                     arrowprops=dict(arrowstyle="<-", color=color, lw=2))
        ax1.plot(hi, y, "o", color=color, markersize=10,
                 markerfacecolor=color if rc else "white", markeredgecolor=color, markeredgewidth=2)
    else:
        ax1.annotate("", xy=(7.5, y), xytext=(lo, y),
                     arrowprops=dict(arrowstyle="->", color=color, lw=2))
        ax1.plot(lo, y, "o", color=color, markersize=10,
                 markerfacecolor=color if lc else "white", markeredgecolor=color, markeredgewidth=2)
ax1.set_xticks(range(-5, 8)); ax1.set_yticks([])

# Plot 2: 2-variable inequality region
ax2 = axes[1]
ax2.set_title("Pertidaksamaan 2 Variabel: 2x + 3y ≤ 12")
x = np.linspace(-1, 8, 400)
y_line = (12 - 2*x) / 3
ax2.plot(x, y_line, "b-", lw=2, label="2x+3y = 12 (batas)")
ax2.fill_between(x, -1, y_line, where=y_line >= -1, alpha=0.25, color="blue", label="2x+3y ≤ 12")
ax2.axhline(0, color="black", lw=0.8); ax2.axvline(0, color="black", lw=0.8)
ax2.set_xlim(-1, 8); ax2.set_ylim(-1, 6)
ax2.set_xlabel("x"); ax2.set_ylabel("y")
ax2.grid(True, alpha=0.3); ax2.legend()
for px,py,col in [(0,0,"green"),(3,2,"green"),(5,1,"red"),(1,3,"green")]:
    inside = 2*px+3*py <= 12
    ax2.plot(px, py, "o", color="green" if inside else "red", markersize=10)
    ax2.text(px+0.1, py+0.1, f"({px},{py})", fontsize=8)

plt.tight_layout()
plt.savefig("/home/therabitt/Projects/Math/Algebra/05_Linear_Inequalities/linear_ineq.png",
            dpi=110, bbox_inches="tight")
print("Saved: linear_ineq.png"); plt.show()
