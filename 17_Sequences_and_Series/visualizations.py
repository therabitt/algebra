"""
Visualizations: Sequences and Series  |  Phase 1 — Topic 1.12
"""
try:
    import matplotlib.pyplot as plt
    import numpy as np
    import math
except ImportError:
    print("pip install matplotlib numpy"); exit()

fig, axes = plt.subplots(1, 3, figsize=(16, 5))
fig.suptitle("1.12 Barisan dan Deret", fontsize=14, fontweight="bold")

# Plot 1: Arithmetic vs Geometric
ax1 = axes[0]
ax1.set_title("Aritmetika vs Geometrika")
n = np.arange(1, 11)
arith = 3 + (n-1)*5
geo   = 2 * (2**(n-1))
ax1.plot(n, arith, "bo-", lw=2, label="Aritmetika: a1=3,d=5")
ax1.plot(n, geo,   "rs-", lw=2, label="Geometrika: a1=2,r=2")
ax1.set_xlabel("n"); ax1.set_ylabel("a_n")
ax1.grid(True,alpha=0.3); ax1.legend()

# Plot 2: Fibonacci spiral concept
ax2 = axes[1]
ax2.set_title("Fibonacci dan Golden Ratio")
phi = (1+math.sqrt(5))/2
fibs = [0,1]
for _ in range(15): fibs.append(fibs[-1]+fibs[-2])
ratios = [fibs[i+1]/fibs[i] for i in range(2, len(fibs)-1)]
ax2.plot(range(2, len(fibs)-1), ratios, "bo-", lw=2, label="F(n)/F(n-1)")
ax2.axhline(phi, color="red", linestyle="--", lw=2, label=f"φ = {phi:.6f}")
ax2.set_xlabel("n"); ax2.set_ylabel("Rasio")
ax2.grid(True,alpha=0.3); ax2.legend()

# Plot 3: Convergence of geometric series
ax3 = axes[2]
ax3.set_title("Konvergensi Deret Geometrika: Σ(1/2)^k")
n_vals = list(range(0, 20))
partial = [sum((0.5)**k for k in range(n+1)) for n in n_vals]
ax3.plot(n_vals, partial, "bo-", lw=2, label="Jumlah parsial")
ax3.axhline(2, color="red", linestyle="--", lw=2, label="S∞ = 2")
ax3.set_xlabel("n suku"); ax3.set_ylabel("Jumlah parsial")
ax3.grid(True,alpha=0.3); ax3.legend()

plt.tight_layout()
plt.savefig("/home/therabitt/Projects/Math/01_Algebra/17_Sequences_and_Series/sequences.png",
            dpi=110, bbox_inches="tight")
print("Saved: sequences.png"); plt.show()
