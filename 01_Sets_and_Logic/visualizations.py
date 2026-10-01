"""
Visualizations: Sets and Logic  |  Phase 1 — Topic 1.14
"""
try:
    import matplotlib.pyplot as plt
    import matplotlib.patches as patches
    import numpy as np
except ImportError:
    print("pip install matplotlib numpy"); exit()

fig, axes = plt.subplots(1, 2, figsize=(13, 6))
fig.suptitle("1.14 Himpunan dan Logika", fontsize=14, fontweight="bold")

# Plot 1: Venn Diagram 3 sets
ax1 = axes[0]
ax1.set_title("Diagram Venn: A, B, C", fontsize=12)
ax1.set_xlim(0, 10); ax1.set_ylim(0, 9); ax1.set_aspect("equal"); ax1.axis("off")

# Draw circles
circles = [
    patches.Circle((3.5, 5.5), 2.5, alpha=0.3, facecolor="blue",  edgecolor="blue",  lw=2, label="A"),
    patches.Circle((6.5, 5.5), 2.5, alpha=0.3, facecolor="red",   edgecolor="red",   lw=2, label="B"),
    patches.Circle((5.0, 3.0), 2.5, alpha=0.3, facecolor="green", edgecolor="green", lw=2, label="C"),
]
for c in circles: ax1.add_patch(c)
ax1.text(2.0, 6.2, "A", fontsize=16, fontweight="bold", color="blue")
ax1.text(7.8, 6.2, "B", fontsize=16, fontweight="bold", color="red")
ax1.text(5.0, 1.2, "C", fontsize=16, fontweight="bold", color="green")

# Label regions
ax1.text(2.5, 7.0, "hanya A", fontsize=8, ha="center")
ax1.text(7.5, 7.0, "hanya B", fontsize=8, ha="center")
ax1.text(5.0, 1.8, "hanya C", fontsize=8, ha="center")
ax1.text(5.0, 6.5, "A∩B", fontsize=8, ha="center")
ax1.text(3.2, 4.0, "A∩C", fontsize=8, ha="center")
ax1.text(6.8, 4.0, "B∩C", fontsize=8, ha="center")
ax1.text(5.0, 5.0, "A∩B∩C", fontsize=7, ha="center")
ax1.set_facecolor("#f8f8f8")

# Plot 2: Truth table visualization
ax2 = axes[1]
ax2.set_title("Tabel Kebenaran: p → q", fontsize=12)
ax2.axis("off")

rows = [["p","q","p→q","¬p∨q","Setara?"],
        ["T","T","T","T","✓"],
        ["T","F","F","F","✓"],
        ["F","T","T","T","✓"],
        ["F","F","T","T","✓"]]

colors_header = ["#2196F3","#2196F3","#F44336","#4CAF50","#9C27B0"]
colors_T = "#C8E6C9"; colors_F = "#FFCDD2"; colors_eq = "#E3F2FD"

table = ax2.table(
    cellText=rows[1:],
    colLabels=rows[0],
    cellLoc="center",
    loc="center",
    bbox=[0.05, 0.1, 0.9, 0.8]
)
table.auto_set_font_size(False); table.set_fontsize(13)
for (r,c), cell in table.get_celld().items():
    cell.set_edgecolor("gray")
    if r == 0:
        cell.set_facecolor(colors_header[c])
        cell.set_text_props(color="white", fontweight="bold")
    else:
        text = cell.get_text().get_text()
        if text == "T": cell.set_facecolor(colors_T)
        elif text == "F": cell.set_facecolor(colors_F)
        elif text == "✓": cell.set_facecolor(colors_eq)

plt.tight_layout()
plt.savefig("/home/therabitt/Projects/Math/01_Algebra/01_Sets_and_Logic/sets_logic.png",
            dpi=110, bbox_inches="tight")
print("Saved: sets_logic.png"); plt.show()
