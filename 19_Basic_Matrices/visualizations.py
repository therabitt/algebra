"""
Visualizations: Basic Matrices  |  Phase 1 — Topic 1.13
"""
try:
    import matplotlib.pyplot as plt
    import matplotlib.patches as patches
    import numpy as np
    import math
except ImportError:
    print("pip install matplotlib numpy"); exit()

fig, axes = plt.subplots(1, 2, figsize=(13, 6))
fig.suptitle("1.13 Matriks Dasar", fontsize=14, fontweight="bold")

# Plot 1: Transformasi Matriks pada titik-titik
ax1 = axes[0]
ax1.set_title("Transformasi Linear 2D\n(Rotasi 45°, Scaling ×2)")
ax1.set_aspect("equal")

# Titik-titik asal (kotak satuan)
points = np.array([[0,0],[1,0],[1,1],[0,1],[0,0]]).T  # 2×5

# Rotasi 45°
theta = math.pi/4
R = np.array([[math.cos(theta), -math.sin(theta)],
              [math.sin(theta),  math.cos(theta)]])

# Scale 2×
S = np.array([[2, 0],[0, 2]])

points_rot = R @ points
points_scale = S @ points

ax1.plot(points[0], points[1], "b-o", lw=2, label="Asli", markersize=6)
ax1.plot(points_rot[0], points_rot[1], "r--s", lw=2, label="Rotasi 45°", markersize=6)
ax1.plot(points_scale[0], points_scale[1], "g:^", lw=2, label="Scale ×2", markersize=6)
ax1.axhline(0,"black",lw=0.6); ax1.axvline(0,"black",lw=0.6)
ax1.grid(True,alpha=0.3); ax1.legend(fontsize=9)
ax1.set_xlim(-2.5, 2.5); ax1.set_ylim(-0.5, 2.5)

# Plot 2: Visualisasi matriks sebagai heatmap
ax2 = axes[1]
ax2.set_title("Heatmap Matriks 3×3")
M = np.array([[4,1,2],[3,5,1],[2,1,6]], dtype=float)
im = ax2.imshow(M, cmap="Blues", aspect="equal")
for i in range(3):
    for j in range(3):
        ax2.text(j, i, f"{M[i,j]:.0f}", ha="center", va="center",
                 fontsize=16, fontweight="bold",
                 color="white" if M[i,j] > 3 else "black")
ax2.set_xticks(range(3)); ax2.set_yticks(range(3))
ax2.set_xticklabels(["j=0","j=1","j=2"])
ax2.set_yticklabels(["i=0","i=1","i=2"])
plt.colorbar(im, ax=ax2, fraction=0.046, pad=0.04)
det = np.linalg.det(M)
ax2.set_xlabel(f"det = {det:.2f},  tr = {np.trace(M):.0f}", fontsize=10)

plt.tight_layout()
plt.savefig("/home/therabitt/Projects/Math/Algebra/13_Basic_Matrices/matrices.png",
            dpi=110, bbox_inches="tight")
print("Saved: matrices.png"); plt.show()
