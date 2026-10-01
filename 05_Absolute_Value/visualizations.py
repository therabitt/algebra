"""
Visualizations: Absolute Value  |  Phase 1 — Topic 1.15
"""
try:
    import matplotlib.pyplot as plt
    import numpy as np
except ImportError:
    print("pip install matplotlib numpy"); exit()

fig, axes = plt.subplots(1, 3, figsize=(16, 5))
fig.suptitle("1.15 Nilai Mutlak (Absolute Value)", fontsize=14, fontweight="bold")

x = np.linspace(-5, 5, 500)

# Plot 1: Transformations of |x|
ax1 = axes[0]
ax1.set_title("Transformasi f(x) = a|x-h| + k")
ax1.plot(x, np.abs(x),         "b-",  lw=2, label="|x|")
ax1.plot(x, np.abs(x-2),       "r-",  lw=2, label="|x-2| (geser kanan)")
ax1.plot(x, np.abs(x)+2,       "g-",  lw=2, label="|x|+2 (geser atas)")
ax1.plot(x, 2*np.abs(x),       "m--", lw=2, label="2|x| (stretch)")
ax1.plot(x, -np.abs(x),        "k--", lw=2, label="-|x| (refleksi)")
ax1.axhline(0,"black",lw=0.6); ax1.axvline(0,"black",lw=0.6)
ax1.set_ylim(-4,7); ax1.grid(True,alpha=0.3); ax1.legend(fontsize=8)

# Plot 2: Absolute value equations and inequalities
ax2 = axes[1]
ax2.set_title("Solusi |x-2| < 3  →  -1 < x < 5")
ax2.plot(x, np.abs(x-2), "b-", lw=2, label="|x-2|")
ax2.axhline(3, color="red", linestyle="--", lw=2, label="y=3")
ax2.fill_between(x, 0, np.abs(x-2), where=np.abs(x-2)<3,
                 alpha=0.2, color="green", label="Daerah |x-2|<3")
ax2.axvline(-1, color="green", linestyle=":", lw=2)
ax2.axvline(5,  color="green", linestyle=":", lw=2)
ax2.plot(-1, 3, "ro", markersize=10); ax2.plot(5, 3, "ro", markersize=10)
ax2.text(-1, -0.5, "x=-1", ha="center", fontsize=9)
ax2.text(5,  -0.5, "x=5",  ha="center", fontsize=9)
ax2.axhline(0,"black",lw=0.6); ax2.axvline(0,"black",lw=0.6)
ax2.set_ylim(-1,7); ax2.grid(True,alpha=0.3); ax2.legend(fontsize=8)

# Plot 3: L1 vs L2 norm circles (unit circles)
ax3 = axes[2]
ax3.set_title("Unit Circle: L1 (♦), L2 (○), L∞ (□)")
t = np.linspace(0, 2*np.pi, 400)

# L2 (Euclidean) circle: x²+y²=1
ax3.plot(np.cos(t), np.sin(t), "b-", lw=2.5, label="L2: x²+y²=1")

# L1 (taxicab) diamond: |x|+|y|=1
L1_x = np.array([1,0,-1,0,1]); L1_y = np.array([0,1,0,-1,0])
ax3.plot(L1_x, L1_y, "r-", lw=2.5, label="L1: |x|+|y|=1")

# L∞ square: max(|x|,|y|)=1
Linf_x = np.array([1,1,-1,-1,1]); Linf_y = np.array([1,-1,-1,1,1])
ax3.plot(Linf_x, Linf_y, "g-", lw=2.5, label="L∞: max(|x|,|y|)=1")

ax3.axhline(0,"black",lw=0.8); ax3.axvline(0,"black",lw=0.8)
ax3.set_xlim(-1.5,1.5); ax3.set_ylim(-1.5,1.5); ax3.set_aspect("equal")
ax3.grid(True,alpha=0.3); ax3.legend(fontsize=9)

plt.tight_layout()
plt.savefig("/home/therabitt/Projects/Math/01_Algebra/05_Absolute_Value/absolute_value.png",
            dpi=110, bbox_inches="tight")
print("Saved: absolute_value.png"); plt.show()
