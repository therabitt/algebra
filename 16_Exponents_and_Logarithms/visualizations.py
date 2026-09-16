"""
Visualizations: Exponents and Logarithms  |  Phase 1 — Topic 1.11
"""
try:
    import matplotlib.pyplot as plt
    import numpy as np
    import math
except ImportError:
    print("pip install matplotlib numpy"); exit()

fig, axes = plt.subplots(1, 3, figsize=(16, 5))
fig.suptitle("1.11 Eksponen dan Logaritma", fontsize=14, fontweight="bold")

x = np.linspace(-3, 4, 400)
x_pos = np.linspace(0.01, 6, 400)

# Plot 1: Exponential functions
ax1 = axes[0]
ax1.set_title("Fungsi Eksponensial")
ax1.plot(x, 2**x,           "b-",  lw=2, label="2^x")
ax1.plot(x, np.e**x,        "r-",  lw=2, label="e^x")
ax1.plot(x, 0.5**x,         "g-",  lw=2, label="(0.5)^x (peluruhan)")
ax1.plot(x, 10**x,          "m--", lw=1.5, label="10^x")
ax1.axhline(0,"black",lw=0.6); ax1.axvline(0,"black",lw=0.6)
ax1.set_ylim(-0.5, 15); ax1.grid(True,alpha=0.3); ax1.legend(fontsize=8)

# Plot 2: Logarithm functions
ax2 = axes[1]
ax2.set_title("Fungsi Logaritma")
ax2.plot(x_pos, np.log2(x_pos),  "b-",  lw=2, label="log₂(x)")
ax2.plot(x_pos, np.log(x_pos),   "r-",  lw=2, label="ln(x)")
ax2.plot(x_pos, np.log10(x_pos), "g-",  lw=2, label="log₁₀(x)")
ax2.axhline(0,"black",lw=0.6); ax2.axvline(0,"black",lw=0.5)
ax2.set_ylim(-4, 4); ax2.grid(True,alpha=0.3); ax2.legend()

# Plot 3: Inverse relationship e^x and ln(x)
ax3 = axes[2]
ax3.set_title("Fungsi Invers: e^x dan ln(x)")
xall = np.linspace(-3, 3, 400)
ax3.plot(xall, np.e**xall, "b-", lw=2, label="e^x")
ax3.plot(x_pos[:150], np.log(x_pos[:150]), "r-", lw=2, label="ln(x)")
ax3.plot(xall, xall, "k--", lw=1, alpha=0.5, label="y=x")
ax3.axhline(0,"black",lw=0.6); ax3.axvline(0,"black",lw=0.6)
ax3.set_xlim(-3,3); ax3.set_ylim(-3,5)
ax3.grid(True,alpha=0.3); ax3.legend()

plt.tight_layout()
plt.savefig("/home/therabitt/Projects/Math/Algebra/11_Exponents_and_Logarithms/exp_log.png",
            dpi=110, bbox_inches="tight")
print("Saved: exp_log.png"); plt.show()
