"""
Visualizations: Complex Numbers  |  Phase 1 — Topic 1.18
"""
try:
    import matplotlib.pyplot as plt
    import numpy as np
    import cmath, math
except ImportError:
    print("pip install matplotlib numpy"); exit()

fig, axes = plt.subplots(1, 3, figsize=(16, 5))
fig.suptitle("1.18 Bilangan Kompleks", fontsize=14, fontweight="bold")

# Plot 1: Complex plane with several numbers
ax1 = axes[0]
ax1.set_title("Bidang Kompleks (Argand Plane)")
ax1.set_aspect("equal")
points = [(3,4),(−2,2),(0,−3),(−1,−1),(2,0),(0,3)]
colors = ["blue","red","green","purple","orange","brown"]
for (a,b),col in zip(points,colors):
    ax1.annotate("", xy=(a,b), xytext=(0,0),
                 arrowprops=dict(arrowstyle="->", color=col, lw=2))
    ax1.plot(a, b, "o", color=col, markersize=8)
    ax1.text(a+0.1, b+0.1, f"{a}+{b}i" if b>=0 else f"{a}{b}i", fontsize=8, color=col)
ax1.axhline(0,"black",lw=0.8); ax1.axvline(0,"black",lw=0.8)
ax1.set_xlabel("Re"); ax1.set_ylabel("Im")
ax1.grid(True,alpha=0.3)

# Plot 2: Roots of unity (n-th roots of 1)
ax2 = axes[1]
ax2.set_title("Akar-6 dari 1: z^6=1")
ax2.set_aspect("equal")
n = 6
theta_circ = np.linspace(0, 2*np.pi, 300)
ax2.plot(np.cos(theta_circ), np.sin(theta_circ), "k--", lw=1, alpha=0.5)
roots = [cmath.exp(2j*math.pi*k/n) for k in range(n)]
for k, r in enumerate(roots):
    ax2.plot(r.real, r.imag, "ro", markersize=12, zorder=5)
    ax2.annotate("", xy=(r.real, r.imag), xytext=(0,0),
                 arrowprops=dict(arrowstyle="->", color="blue", lw=1.5, alpha=0.6))
    ax2.text(r.real*1.15, r.imag*1.15, f"k={k}", fontsize=8, ha="center")
ax2.set_xlim(-1.5,1.5); ax2.set_ylim(-1.5,1.5)
ax2.axhline(0,"black",lw=0.6); ax2.axvline(0,"black",lw=0.6)
ax2.grid(True,alpha=0.3)

# Plot 3: Mandelbrot set (simplified)
ax3 = axes[2]
ax3.set_title("Himpunan Mandelbrot\n(iterasi z²+c)")
res = 200
x = np.linspace(-2.5, 1, res)
y = np.linspace(-1.2, 1.2, res)
X, Y = np.meshgrid(x, y)
C = X + 1j*Y
Z = np.zeros_like(C)
M = np.zeros(C.shape, dtype=int)
for i in range(50):
    mask = np.abs(Z) <= 2
    Z[mask] = Z[mask]**2 + C[mask]
    M[mask] += 1
ax3.imshow(M, extent=[-2.5,1,-1.2,1.2], cmap="inferno", origin="lower", aspect="auto")
ax3.set_xlabel("Re(c)"); ax3.set_ylabel("Im(c)")

plt.tight_layout()
plt.savefig("/home/therabitt/Projects/Math/01_Algebra/11_Complex_Numbers/complex_numbers.png",
            dpi=110, bbox_inches="tight")
print("Saved: complex_numbers.png")
plt.show()
