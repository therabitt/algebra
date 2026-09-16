"""
Visualizations: Binomial Theorem  |  Phase 1 — Topic 1.19
"""
try:
    import matplotlib.pyplot as plt
    import matplotlib.colors as mcolors
    import numpy as np
    import math
except ImportError:
    print("pip install matplotlib numpy"); exit()

def C(n,k):
    if k<0 or k>n: return 0
    k=min(k,n-k); r=1
    for i in range(k): r=r*(n-i)//(i+1)
    return r

fig, axes = plt.subplots(1, 3, figsize=(16, 5))
fig.suptitle("1.19 Teorema Binomial", fontsize=14, fontweight="bold")

# Plot 1: Pascal Triangle Heatmap
ax1 = axes[0]
ax1.set_title("Segitiga Pascal (log scale)")
n_rows = 12
data = [[C(n,k) if k<=n else 0 for k in range(n_rows)] for n in range(n_rows)]
grid = np.array(data, dtype=float)
grid[grid==0] = np.nan
im = ax1.imshow(np.log1p(grid), cmap="YlOrRd", aspect="auto")
for n in range(n_rows):
    for k in range(n+1):
        ax1.text(k, n, str(C(n,k)), ha="center", va="center",
                 fontsize=7 if C(n,k) < 100 else 5)
ax1.set_xlabel("k"); ax1.set_ylabel("n")

# Plot 2: Binomial distribution P(X=k) for various p
ax2 = axes[1]
ax2.set_title("Distribusi Binomial n=20")
n = 20
ks = list(range(n+1))
for p, col in [(0.3,"blue"),(0.5,"green"),(0.7,"red")]:
    probs = [C(n,k)*(p**k)*((1-p)**(n-k)) for k in ks]
    ax2.bar([x + (0.3 if p==0.3 else 0.6 if p==0.5 else 0.9) for x in ks],
            probs, width=0.28, alpha=0.7, color=col, label=f"p={p}")
ax2.set_xlabel("k"); ax2.set_ylabel("P(X=k)")
ax2.legend(); ax2.grid(True, alpha=0.3)

# Plot 3: Binomial approximation accuracy
ax3 = axes[2]
ax3.set_title("Akurasi Aproksimasi (1+x)^10")
x_range = np.linspace(-0.3, 0.3, 200)
exact = (1 + x_range)**10
approx1 = 1 + 10*x_range
approx2 = 1 + 10*x_range + C(10,2)*x_range**2
approx3 = approx2 + C(10,3)*x_range**3
ax3.plot(x_range, exact, "k-", lw=2.5, label="Exact (1+x)^10")
ax3.plot(x_range, approx1, "r--", lw=1.8, label="Orde 1: 1+10x")
ax3.plot(x_range, approx2, "g--", lw=1.8, label="Orde 2")
ax3.plot(x_range, approx3, "b--", lw=1.8, label="Orde 3")
ax3.set_xlabel("x"); ax3.set_ylabel("(1+x)^10")
ax3.legend(fontsize=8); ax3.grid(True,alpha=0.3)

plt.tight_layout()
plt.savefig("/home/therabitt/Projects/Math/Algebra/19_Binomial_Theorem/binomial.png",
            dpi=110, bbox_inches="tight")
print("Saved: binomial.png")
plt.show()
