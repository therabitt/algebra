"""
Visualizations: Functions and Relations  |  Phase 1 — Topic 1.8
"""
try:
    import matplotlib.pyplot as plt
    import numpy as np
    import math
except ImportError:
    print("pip install matplotlib numpy"); exit()

fig, axes = plt.subplots(2, 2, figsize=(13, 10))
fig.suptitle("1.8 Fungsi dan Relasi", fontsize=14, fontweight="bold")

x = np.linspace(-4, 4, 400)

# Plot 1: Berbagai fungsi
ax1 = axes[0,0]
ax1.set_title("Berbagai Jenis Fungsi")
ax1.plot(x, x,        "b-",  lw=2, label="f(x)=x (linear)")
ax1.plot(x, x**2,     "r-",  lw=2, label="g(x)=x² (kuadrat)")
ax1.plot(x, x**3/10,  "g-",  lw=2, label="h(x)=x³/10 (kubik)")
ax1.plot(x[x>0], np.sqrt(x[x>0]), "m-", lw=2, label="k(x)=√x")
ax1.axhline(0,"black",lw=0.6); ax1.axvline(0,"black",lw=0.6)
ax1.set_ylim(-5, 8); ax1.grid(True, alpha=0.3); ax1.legend(fontsize=8)

# Plot 2: Fungsi dan inversnya
ax2 = axes[0,1]
ax2.set_title("Fungsi dan Invers: f(x)=2x+3, f⁻¹(x)=(x-3)/2")
ax2.plot(x, 2*x+3, "b-", lw=2, label="f(x)=2x+3")
ax2.plot(x, (x-3)/2, "r-", lw=2, label="f⁻¹(x)=(x-3)/2")
ax2.plot(x, x, "k--", lw=1, alpha=0.5, label="y=x (cermin)")
ax2.axhline(0,"black",lw=0.6); ax2.axvline(0,"black",lw=0.6)
ax2.set_ylim(-5, 8); ax2.set_xlim(-4,4)
ax2.grid(True, alpha=0.3); ax2.legend(fontsize=8)

# Plot 3: Komposisi
ax3 = axes[1,0]
ax3.set_title("Komposisi: f(x)=2x+3, g(x)=x²-1")
f_vals = 2*x + 3
g_vals = x**2 - 1
fog = 2*(x**2-1)+3  # f(g(x))
gof = (2*x+3)**2-1  # g(f(x))
ax3.plot(x, fog, "b-", lw=2, label="(f∘g)(x)=2x²+1")
ax3.plot(x, gof, "r-", lw=2, label="(g∘f)(x)=4x²+12x+8")
ax3.axhline(0,"black",lw=0.6); ax3.axvline(0,"black",lw=0.6)
ax3.set_ylim(-5, 20); ax3.grid(True, alpha=0.3); ax3.legend(fontsize=8)

# Plot 4: Even/Odd
ax4 = axes[1,1]
ax4.set_title("Genap vs Ganjil: x² (genap), x³ (ganjil)")
ax4.plot(x, x**2, "b-", lw=2, label="x² (genap: f(-x)=f(x))")
ax4.plot(x, x**3/8, "r-", lw=2, label="x³/8 (ganjil: f(-x)=-f(x))")
ax4.axhline(0,"black",lw=0.8); ax4.axvline(0,"black",lw=0.8)
ax4.grid(True, alpha=0.3); ax4.legend(fontsize=8)

plt.tight_layout()
plt.savefig("/home/therabitt/Projects/Math/01_Algebra/13_Functions_and_Relations/functions.png",
            dpi=110, bbox_inches="tight")
print("Saved: functions.png"); plt.show()
