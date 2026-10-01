"""
Visualizations: Algebraic Expressions  |  Phase 1 — Topic 1.3
"""
try:
    import matplotlib.pyplot as plt
    import numpy as np
except ImportError:
    print("pip install matplotlib numpy"); exit()

fig, axes = plt.subplots(1, 2, figsize=(12, 5))
fig.suptitle("1.3 Ekspresi Aljabar", fontsize=14, fontweight="bold")

x = np.linspace(-4, 4, 400)

ax1 = axes[0]
ax1.set_title("Evaluasi Beberapa Ekspresi")
ax1.plot(x, 3*x**2 - 5*x + 2, label="3x²−5x+2", color="blue", lw=2)
ax1.plot(x, 2*x + 1, label="2x+1", color="red", lw=2)
ax1.plot(x, x**3 - 2*x, label="x³−2x", color="green", lw=2)
ax1.axhline(0, color="black", lw=0.8); ax1.axvline(0, color="black", lw=0.8)
ax1.grid(True, alpha=0.3); ax1.legend(); ax1.set_ylim(-10, 15)

ax2 = axes[1]
ax2.set_title("Produk Khusus: (a+b)² vs a²+b²")
a_vals = np.linspace(0, 4, 50)
b = 2
ax2.plot(a_vals, (a_vals+b)**2, label="(a+b)²", color="blue", lw=2)
ax2.plot(a_vals, a_vals**2+b**2, label="a²+b²", color="red", lw=2, linestyle="--")
ax2.fill_between(a_vals, (a_vals+b)**2, a_vals**2+b**2,
                 alpha=0.2, label="selisih = 2ab", color="purple")
ax2.set_xlabel("a"); ax2.grid(True, alpha=0.3); ax2.legend()

plt.tight_layout()
plt.savefig("/home/therabitt/Projects/Math/01_Algebra/04_Algebraic_Expressions/algebraic_expr.png",
            dpi=110, bbox_inches="tight")
print("Saved: algebraic_expr.png")
plt.show()
