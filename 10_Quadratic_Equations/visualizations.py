"""
Visualizations: Quadratic Equations  |  Phase 1 — Topic 1.6
"""
try:
    import matplotlib.pyplot as plt
    import numpy as np
    import math
except ImportError:
    print("pip install matplotlib numpy"); exit()

fig, axes = plt.subplots(1, 3, figsize=(15, 5))
fig.suptitle("1.6 Persamaan Kuadrat", fontsize=14, fontweight="bold")

x = np.linspace(-3, 6, 500)

# Plot 1: Parabola dengan akar dan vertex
ax1 = axes[0]
ax1.set_title("Parabola: x² - 3x - 4 = 0")
a,b,c = 1,-3,-4
y = a*x**2 + b*x + c
ax1.plot(x, y, "b-", lw=2)
ax1.axhline(0, color="black", lw=0.8)
ax1.axvline(0, color="black", lw=0.8)
# roots
D = b**2-4*a*c
x1 = (-b+math.sqrt(D))/(2*a)
x2 = (-b-math.sqrt(D))/(2*a)
ax1.plot([x1,x2],[0,0],"ro",markersize=10,zorder=5,label=f"Akar: x={x2},{x1}")
# vertex
h = -b/(2*a); k = a*h**2+b*h+c
ax1.plot(h, k, "g^", markersize=12, zorder=5, label=f"Vertex ({h:.1f},{k:.1f})")
ax1.axvline(h, color="green", linestyle=":", lw=1.5, label="Axis of symmetry")
ax1.set_ylim(-8, 10); ax1.grid(True, alpha=0.3); ax1.legend(fontsize=8)

# Plot 2: Diskriminan — tiga kasus
ax2 = axes[1]
ax2.set_title("Kasus Diskriminan (D>0, D=0, D<0)")
x2 = np.linspace(-3, 3, 400)
ax2.plot(x2, x2**2-2*x2-3, "b-", lw=2, label="D>0: dua akar real")
ax2.plot(x2, x2**2-2*x2+1, "g-", lw=2, label="D=0: satu akar")
ax2.plot(x2, x2**2-2*x2+3, "r-", lw=2, label="D<0: akar kompleks")
ax2.axhline(0, color="black", lw=0.8)
ax2.set_ylim(-5, 8); ax2.grid(True, alpha=0.3); ax2.legend(fontsize=8)

# Plot 3: Proyektil h(t) = -5t^2+20t+15
ax3 = axes[2]
ax3.set_title("Proyektil: h(t) = -5t²+20t+15")
t = np.linspace(0, 5, 300)
h_func = -5*t**2 + 20*t + 15
valid = h_func >= 0
ax3.plot(t[valid], h_func[valid], "b-", lw=2, label="h(t)")
ax3.axhline(0, color="black", lw=0.8)
t_max = 2.0; h_max = -5*4+40+15
ax3.plot(t_max, h_max, "r*", markersize=15, label=f"Max: ({t_max}s, {h_max}m)")
ax3.set_xlabel("Waktu (s)"); ax3.set_ylabel("Ketinggian (m)")
ax3.grid(True, alpha=0.3); ax3.legend()

plt.tight_layout()
plt.savefig("/home/therabitt/Projects/Math/01_Algebra/10_Quadratic_Equations/quadratic.png",
            dpi=110, bbox_inches="tight")
print("Saved: quadratic.png"); plt.show()
