"""
Visualizations: Systems of Equations  |  Phase 1 — Topic 1.7
"""
try:
    import matplotlib.pyplot as plt
    import numpy as np
except ImportError:
    print("pip install matplotlib numpy"); exit()

fig, axes = plt.subplots(1, 3, figsize=(15, 5))
fig.suptitle("1.7 Sistem Persamaan", fontsize=14, fontweight="bold")

x = np.linspace(-3, 7, 400)

# Plot 1: Satu solusi (intersection)
ax1 = axes[0]
ax1.set_title("Konsisten: 1 Solusi")
# x + y = 5  ->  y = 5-x
# 2x - y = 1 -> y = 2x-1
ax1.plot(x, 5-x, "b-", lw=2, label="x+y=5")
ax1.plot(x, 2*x-1, "r-", lw=2, label="2x-y=1")
ax1.plot(2, 3, "k*", markersize=15, zorder=5, label="Solusi (2,3)")
ax1.axhline(0,"black",lw=0.6); ax1.axvline(0,"black",lw=0.6)
ax1.set_ylim(-2,8); ax1.grid(True,alpha=0.3); ax1.legend()

# Plot 2: Tidak ada solusi (parallel)
ax2 = axes[1]
ax2.set_title("Inkonsisten: Tidak Ada Solusi (Paralel)")
ax2.plot(x, 5-x,   "b-", lw=2, label="x+y=5")
ax2.plot(x, 8-x,   "r--", lw=2, label="x+y=8")
ax2.axhline(0,"black",lw=0.6); ax2.axvline(0,"black",lw=0.6)
ax2.set_ylim(-2,12); ax2.grid(True,alpha=0.3); ax2.legend()

# Plot 3: Tak hingga (same line)
ax3 = axes[2]
ax3.set_title("Dependen: Tak Hingga Solusi (Garis Sama)")
ax3.plot(x, 5-x, "b-", lw=3, label="x+y=5", alpha=0.6)
ax3.plot(x, 5-x, "r--", lw=2, label="2x+2y=10 (sama!)")
ax3.axhline(0,"black",lw=0.6); ax3.axvline(0,"black",lw=0.6)
ax3.set_ylim(-2,8); ax3.grid(True,alpha=0.3); ax3.legend()

plt.tight_layout()
plt.savefig("/home/therabitt/Projects/Math/01_Algebra/08_Systems_of_Equations/systems.png",
            dpi=110, bbox_inches="tight")
print("Saved: systems.png"); plt.show()
