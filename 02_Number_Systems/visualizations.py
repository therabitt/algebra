"""
Visualizations: Number Systems
Phase 1 — Topic 1.1

Jalankan: python3 visualizations.py
Requires: matplotlib, numpy
"""

import math
try:
    import matplotlib.pyplot as plt
    import matplotlib.patches as mpatches
    import numpy as np
    HAS_PLOT = True
except ImportError:
    print("matplotlib/numpy tidak tersedia. Install dengan: pip install matplotlib numpy")
    HAS_PLOT = False

if not HAS_PLOT:
    exit()

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("1.1 Sistem Bilangan (Number Systems)", fontsize=16, fontweight="bold")

# ── Plot 1: Garis Bilangan dengan berbagai tipe ──────────────
ax1 = axes[0, 0]
ax1.set_title("Garis Bilangan — Berbagai Tipe Bilangan", fontsize=11)
ax1.axhline(y=0, color="black", linewidth=2)
ax1.set_xlim(-4.5, 4.5)
ax1.set_ylim(-1, 1)

points = [
    (-3,   "−3\n(Z)",  "blue"),
    (0,    "0\n(W)",   "green"),
    (2,    "2\n(N)",   "green"),
    (-1.5, "−3/2\n(Q)","orange"),
    (0.75, "3/4\n(Q)", "orange"),
    (math.sqrt(2), "√2\n(irr)","red"),
    (-math.pi,     "−π\n(irr)","red"),
]

for xval, label, color in points:
    ax1.plot(xval, 0, "o", color=color, markersize=12, zorder=5)
    ax1.text(xval, 0.15, label, ha="center", fontsize=8, color=color)

ax1.set_yticks([])
ax1.set_xticks(range(-4, 5))
legend_elements = [
    mpatches.Patch(color="green",  label="Natural/Whole (N/W)"),
    mpatches.Patch(color="blue",   label="Integer negatif (Z)"),
    mpatches.Patch(color="orange", label="Rasional (Q)"),
    mpatches.Patch(color="red",    label="Irasional"),
]
ax1.legend(handles=legend_elements, loc="lower right", fontsize=8)

# ── Plot 2: Diagram Venn hierarki ───────────────────────────
ax2 = axes[0, 1]
ax2.set_title("Hierarki Sistem Bilangan (N ⊂ W ⊂ Z ⊂ Q ⊂ R ⊂ C)", fontsize=10)
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 10)
ax2.set_aspect("equal")
ax2.axis("off")

circles = [
    (5, 5, 4.5, "#e8f4f8", "C (Kompleks)"),
    (5, 4.5, 3.8, "#d0e8f0", "R (Real)"),
    (5, 4.2, 3.1, "#b8d8e8", "Q (Rasional)"),
    (5, 4.0, 2.4, "#98c4d8", "Z (Bulat)"),
    (5, 3.8, 1.7, "#78b0c8", "W (Cacah)"),
    (5, 3.6, 1.0, "#4a90b8", "N (Asli)"),
]

for cx, cy, r, color, label in circles:
    circle = plt.Circle((cx, cy), r, color=color, fill=True, linewidth=1.5, edgecolor="gray")
    ax2.add_patch(circle)
    ax2.text(cx, cy + r - 0.3, label, ha="center", va="top", fontsize=8.5, fontweight="bold")

# ── Plot 3: Bidang Kompleks ───────────────────────────────────
ax3 = axes[1, 0]
ax3.set_title("Bidang Kompleks (Complex Plane)", fontsize=11)
ax3.axhline(y=0, color="black", linewidth=0.8)
ax3.axvline(x=0, color="black", linewidth=0.8)
ax3.set_xlabel("Real")
ax3.set_ylabel("Imaginer")
ax3.set_xlim(-4, 5)
ax3.set_ylim(-4, 5)
ax3.grid(True, alpha=0.3)

complex_points = [
    (3, 4, "z₁ = 3+4i", "blue"),
    (-2, 1, "z₂ = −2+i", "red"),
    (1, -3, "z₃ = 1−3i", "green"),
    (-3, -2, "z₄ = −3−2i", "purple"),
    (2, 0, "z₅ = 2 (real)", "orange"),
]

for re, im, label, color in complex_points:
    ax3.plot(re, im, "o", color=color, markersize=10)
    ax3.text(re+0.15, im+0.15, label, fontsize=8, color=color)
    ax3.plot([0, re], [0, im], "--", color=color, alpha=0.4, linewidth=1)

# Tampilkan modulus z1
z1_re, z1_im = 3, 4
ax3.annotate("", xy=(z1_re, z1_im), xytext=(0,0),
             arrowprops=dict(arrowstyle="->", color="blue", lw=2))
ax3.text(1.2, 2.2, f"|z₁| = 5", fontsize=9, color="blue")

# ── Plot 4: Ekspansi desimal bilangan irasional ───────────────
ax4 = axes[1, 1]
ax4.set_title("Desimal Irasional (tidak berakhir, tidak berulang)", fontsize=10)
ax4.axis("off")

irrationals = [
    ("√2", math.sqrt(2)),
    ("π",  math.pi),
    ("e",  math.e),
    ("φ",  (1+math.sqrt(5))/2),
]

y_pos = 0.85
ax4.text(0.05, 0.95, "Bilangan Irasional Terkenal:", fontsize=11, fontweight="bold",
         transform=ax4.transAxes)
for name, val in irrationals:
    decimal_str = f"{val:.30f}"
    ax4.text(0.05, y_pos, f"{name} = {decimal_str}...", fontsize=9,
             transform=ax4.transAxes, family="monospace")
    y_pos -= 0.15

ax4.text(0.05, 0.15,
         "Tidak pernah berulang atau berakhir!\nBukti: tidak bisa ditulis sebagai p/q",
         fontsize=9, transform=ax4.transAxes,
         bbox=dict(boxstyle="round", facecolor="#fff3cd", alpha=0.8))

plt.tight_layout()
plt.savefig("/home/therabitt/Projects/Math/01_Algebra/02_Number_Systems/number_systems.png",
            dpi=120, bbox_inches="tight")
print("Plot disimpan: number_systems.png")
plt.show()
