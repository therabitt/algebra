"""
=============================================================================
visualizations.py — Visualisasi Operasi Dasar / Basic Operations Visualizations
=============================================================================
Menghasilkan 5 visualisasi matplotlib untuk membantu pemahaman konsep.
Produces 5 matplotlib visualizations to aid concept understanding.

Visualisasi / Visualizations:
  1. Garis bilangan untuk penjumlahan/pengurangan / Number line for addition/subtraction
  2. Model area untuk perkalian / Area model for multiplication
  3. Diagram pohon urutan operasi / Order of operations tree diagram
  4. Jam aritmatika modular / Modular arithmetic clock
  5. Grafik pertumbuhan eksponen / Exponent growth chart

Jalankan / Run:
  python3 visualizations.py
  (Menyimpan semua gambar ke file PNG dan menampilkannya / Saves all PNGs and displays them)
=============================================================================
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.patches as patches
from matplotlib.patches import FancyArrowPatch, Arc
import matplotlib.gridspec as gridspec
from matplotlib.patches import FancyBboxPatch
import math

# Konfigurasi global / Global configuration
plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 11,
    'axes.titlesize': 14,
    'axes.titleweight': 'bold',
    'figure.facecolor': '#FAFAFA',
    'axes.facecolor': '#FFFFFF',
    'axes.grid': False,
})

COLORS = {
    'primary':   '#2196F3',   # biru / blue
    'secondary': '#4CAF50',   # hijau / green
    'accent':    '#FF5722',   # oranye / orange
    'purple':    '#9C27B0',
    'teal':      '#009688',
    'yellow':    '#FFC107',
    'red':       '#F44336',
    'dark':      '#212121',
    'light':     '#ECEFF1',
}


# =============================================================================
# VISUALISASI 1: GARIS BILANGAN / NUMBER LINE
# =============================================================================

def plot_number_line():
    """
    Visualisasi penjumlahan dan pengurangan pada garis bilangan.
    Visualization of addition and subtraction on a number line.
    """
    fig, axes = plt.subplots(3, 1, figsize=(12, 8))
    fig.suptitle('Visualisasi 1: Garis Bilangan\nNumber Line Visualization',
                 fontsize=16, fontweight='bold', y=0.98)

    examples = [
        # (start, operation, amount, title_id, title_en, color)
        (3,   'tambah/add',  '+5',  'penjumlahan / addition',     '+',  COLORS['secondary']),
        (8,   'kurang/sub',  '-5',  'pengurangan / subtraction',  '-',  COLORS['accent']),
        (-2,  'tambah/add',  '+7',  'tambah negatif / add negative', '+', COLORS['purple']),
    ]

    for ax, (start, op_type, amount_str, title, op_sym, color) in zip(axes, examples):
        amount = int(amount_str)
        end = start + amount

        # Batas garis / Line bounds
        lo = min(start, end) - 2
        hi = max(start, end) + 2

        # Gambar garis bilangan / Draw number line
        ax.axhline(y=0, color=COLORS['dark'], linewidth=2, zorder=1)

        # Tanda-tanda / Tick marks
        for x in range(int(lo), int(hi)+1):
            ax.plot([x, x], [-0.1, 0.1], color=COLORS['dark'], linewidth=1, zorder=2)
            ax.text(x, -0.25, str(x), ha='center', va='top', fontsize=9)

        # Panah untuk operasi / Arrow for operation
        style = "Simple,tail_width=3,head_width=12,head_length=8"
        arrow_color = color if amount > 0 else COLORS['red']
        ax.annotate('',
                    xy=(end, 0.3), xytext=(start, 0.3),
                    arrowprops=dict(arrowstyle='->', color=arrow_color,
                                   lw=2.5, mutation_scale=20))

        # Label titik / Point labels
        ax.plot(start, 0, 'o', color=COLORS['primary'], markersize=12, zorder=5)
        ax.text(start, 0.55, f'mulai\n{start}', ha='center', va='bottom',
                fontsize=9, color=COLORS['primary'], fontweight='bold')

        ax.plot(end, 0, 's', color=color, markersize=12, zorder=5)
        ax.text(end, 0.55, f'hasil\n{end}', ha='center', va='bottom',
                fontsize=9, color=color, fontweight='bold')

        # Label operasi di tengah panah / Operation label at arrow midpoint
        mid_x = (start + end) / 2
        ax.text(mid_x, 0.45, f'{amount_str}', ha='center', va='bottom',
                fontsize=12, fontweight='bold', color=arrow_color,
                bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                         edgecolor=arrow_color, alpha=0.9))

        # Ekspresi matematika / Math expression
        ax.text(hi - 0.5, 0.7, f'{start} {op_sym} {abs(amount)} = {end}',
                ha='right', va='bottom', fontsize=12, fontweight='bold',
                color=COLORS['dark'],
                bbox=dict(boxstyle='round,pad=0.3', facecolor=COLORS['light'],
                         edgecolor=COLORS['dark'], alpha=0.8))

        ax.set_xlim(lo - 0.5, hi + 0.5)
        ax.set_ylim(-0.5, 1.0)
        ax.set_yticks([])
        ax.spines['left'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.set_title(f'  {title}: {start} {op_sym} {abs(amount)} = {end}',
                     loc='left', fontsize=11, color=color)

    plt.tight_layout()
    plt.savefig('viz1_number_line.png', dpi=120, bbox_inches='tight',
                facecolor=fig.get_facecolor())
    print("Tersimpan / Saved: viz1_number_line.png")
    return fig


# =============================================================================
# VISUALISASI 2: MODEL AREA UNTUK PERKALIAN / AREA MODEL FOR MULTIPLICATION
# =============================================================================

def plot_area_model():
    """
    Visualisasi perkalian sebagai luas persegi panjang.
    Visualization of multiplication as area of rectangle.
    Juga menampilkan sifat distributif!
    Also demonstrates the distributive property!
    """
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    fig.suptitle('Visualisasi 2: Model Area untuk Perkalian\nArea Model for Multiplication',
                 fontsize=16, fontweight='bold')

    # --- Panel kiri: Perkalian sederhana / Left panel: Simple multiplication ---
    ax1 = axes[0]
    a, b = 4, 6

    # Gambar grid unit / Draw unit grid
    for i in range(a):
        for j in range(b):
            rect = patches.Rectangle((j, i), 1, 1,
                                      linewidth=0.5, edgecolor='white',
                                      facecolor=COLORS['primary'], alpha=0.7)
            ax1.add_patch(rect)
            ax1.text(j + 0.5, i + 0.5, '1', ha='center', va='center',
                    fontsize=7, color='white', alpha=0.8)

    # Kotak utama / Main rectangle
    rect_main = patches.Rectangle((0, 0), b, a,
                                   linewidth=2.5, edgecolor=COLORS['primary'],
                                   facecolor='none', zorder=5)
    ax1.add_patch(rect_main)

    # Label dimensi / Dimension labels
    ax1.text(b/2, -0.4, f'b = {b}', ha='center', va='top',
             fontsize=13, fontweight='bold', color=COLORS['primary'])
    ax1.text(-0.4, a/2, f'a = {a}', ha='right', va='center',
             fontsize=13, fontweight='bold', color=COLORS['primary'], rotation=90)

    # Label area / Area label
    ax1.text(b/2, a/2, f'{a} × {b} = {a*b}',
             ha='center', va='center', fontsize=16, fontweight='bold',
             color='white',
             bbox=dict(boxstyle='round,pad=0.4', facecolor=COLORS['dark'],
                      edgecolor='white', alpha=0.85))

    ax1.set_xlim(-1, b+1)
    ax1.set_ylim(-0.8, a+0.8)
    ax1.set_aspect('equal')
    ax1.set_title(f'Perkalian / Multiplication\n{a} × {b} = {a*b}',
                  fontsize=12, fontweight='bold')
    ax1.axis('off')

    # --- Panel kanan: Sifat Distributif / Right panel: Distributive Property ---
    ax2 = axes[1]
    # 4 × (3 + 2) = 4×3 + 4×2
    a2, b1, b2 = 4, 3, 2

    # Bagian kiri (a × b1) / Left part
    for i in range(a2):
        for j in range(b1):
            rect = patches.Rectangle((j, i), 1, 1,
                                      linewidth=0.5, edgecolor='white',
                                      facecolor=COLORS['secondary'], alpha=0.75)
            ax2.add_patch(rect)

    # Bagian kanan (a × b2) / Right part
    for i in range(a2):
        for j in range(b2):
            rect = patches.Rectangle((b1+j, i), 1, 1,
                                      linewidth=0.5, edgecolor='white',
                                      facecolor=COLORS['accent'], alpha=0.75)
            ax2.add_patch(rect)

    # Batas / Borders
    rect_l = patches.Rectangle((0, 0), b1, a2, linewidth=2.5,
                                 edgecolor=COLORS['secondary'], facecolor='none', zorder=5)
    rect_r = patches.Rectangle((b1, 0), b2, a2, linewidth=2.5,
                                 edgecolor=COLORS['accent'], facecolor='none', zorder=5)
    ax2.add_patch(rect_l)
    ax2.add_patch(rect_r)

    # Garis pemisah / Divider line
    ax2.axvline(x=b1, color=COLORS['dark'], linewidth=2.5, linestyle='--', zorder=6)

    # Label / Labels
    ax2.text(b1/2, -0.4, f'b₁ = {b1}', ha='center', va='top',
             fontsize=11, fontweight='bold', color=COLORS['secondary'])
    ax2.text(b1+b2/2, -0.4, f'b₂ = {b2}', ha='center', va='top',
             fontsize=11, fontweight='bold', color=COLORS['accent'])
    ax2.text(-0.5, a2/2, f'a = {a2}', ha='right', va='center',
             fontsize=11, fontweight='bold', rotation=90)

    ax2.text(b1/2, a2/2, f'{a2}×{b1}={a2*b1}',
             ha='center', va='center', fontsize=13, fontweight='bold', color='white')
    ax2.text(b1+b2/2, a2/2, f'{a2}×{b2}={a2*b2}',
             ha='center', va='center', fontsize=13, fontweight='bold', color='white')

    total = a2 * (b1 + b2)
    ax2.text((b1+b2)/2, a2+0.3,
             f'{a2}×({b1}+{b2}) = {a2}×{b1} + {a2}×{b2} = {a2*b1}+{a2*b2} = {total}',
             ha='center', va='bottom', fontsize=11, fontweight='bold',
             bbox=dict(boxstyle='round,pad=0.3', facecolor=COLORS['light'],
                      edgecolor=COLORS['dark'], alpha=0.9))

    ax2.set_xlim(-1, b1+b2+1)
    ax2.set_ylim(-0.8, a2+1.2)
    ax2.set_aspect('equal')
    ax2.set_title(f'Sifat Distributif / Distributive Property\n{a2}×({b1}+{b2}) = {a2}×{b1} + {a2}×{b2}',
                  fontsize=12, fontweight='bold')
    ax2.axis('off')

    plt.tight_layout()
    plt.savefig('viz2_area_model.png', dpi=120, bbox_inches='tight',
                facecolor=fig.get_facecolor())
    print("Tersimpan / Saved: viz2_area_model.png")
    return fig


# =============================================================================
# VISUALISASI 3: URUTAN OPERASI / ORDER OF OPERATIONS
# =============================================================================

def plot_order_of_operations():
    """
    Diagram pohon untuk evaluasi ekspresi.
    Tree diagram for expression evaluation.
    """
    fig, ax = plt.subplots(1, 1, figsize=(14, 9))
    fig.suptitle('Visualisasi 3: Urutan Operasi / Order of Operations\n'
                 'Ekspresi / Expression: 2 + 3 × 4² − (6 ÷ 2)',
                 fontsize=15, fontweight='bold')

    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Data pohon evaluasi / Evaluation tree data
    # Format: (x, y, text, color, step_num)
    nodes = [
        # Level 0: Ekspresi awal / Original expression
        (7, 9.0, '2 + 3 × 4² − (6 ÷ 2)', '#37474F', None),

        # Level 1: Langkah 1 - Kurung / Step 1 - Parentheses
        (7, 7.5, 'Langkah 1: Kurung\n(6 ÷ 2) = 3', COLORS['red'], '①'),
        (3.5, 7.5, '2 + 3 × 4² − 3', '#37474F', None),

        # Level 2: Langkah 2 - Eksponen
        (10.5, 6.0, 'Langkah 2: Eksponen\n4² = 16', COLORS['accent'], '②'),
        (3.5, 6.0, '2 + 3 × 16 − 3', '#37474F', None),

        # Level 3: Langkah 3 - Perkalian
        (10.5, 4.5, 'Langkah 3: Perkalian\n3 × 16 = 48', COLORS['primary'], '③'),
        (3.5, 4.5, '2 + 48 − 3', '#37474F', None),

        # Level 4: Langkah 4 - Kiri ke kanan
        (10.5, 3.0, 'Langkah 4: Penjumlahan\n2 + 48 = 50', COLORS['secondary'], '④'),
        (3.5, 3.0, '50 − 3', '#37474F', None),

        # Level 5: Hasil akhir
        (10.5, 1.5, 'Langkah 5: Pengurangan\n50 − 3 = 47', COLORS['teal'], '⑤'),
        (3.5, 1.5, '= 47', COLORS['secondary'], None),
    ]

    # PEMDAS Legend
    pemdas = [
        ('P', 'Parentheses\n(Kurung)', COLORS['red']),
        ('E', 'Exponents\n(Eksponen)', COLORS['accent']),
        ('M', 'Multiplication\n(Perkalian)', COLORS['primary']),
        ('D', 'Division\n(Pembagian)', COLORS['primary']),
        ('A', 'Addition\n(Penjumlahan)', COLORS['secondary']),
        ('S', 'Subtraction\n(Pengurangan)', COLORS['teal']),
    ]

    # Gambar legend PEMDAS
    for i, (letter, name, color) in enumerate(pemdas):
        x_leg = 0.3 + i * 2.2
        y_leg = 0.4
        circ = plt.Circle((x_leg, y_leg), 0.35, color=color, zorder=5)
        ax.add_patch(circ)
        ax.text(x_leg, y_leg, letter, ha='center', va='center',
                fontsize=14, fontweight='bold', color='white', zorder=6)
        ax.text(x_leg, y_leg-0.55, name, ha='center', va='top',
                fontsize=7, color=color, fontweight='bold')

    # Gambar garis penghubung / Draw connector lines
    connections = [
        (7, 8.75, 7, 7.85),        # ekspresi → langkah 1
        (7, 7.15, 3.5, 6.35),      # hasil 1 → langkah 2
        (7, 7.85, 3.5, 7.65),
        (3.5, 7.15, 10.5, 5.85),
        (3.5, 5.65, 3.5, 4.85),
        (10.5, 5.65, 10.5, 4.85),
        (3.5, 4.15, 10.5, 3.35),
        (3.5, 3.65, 3.5, 3.35),
        (3.5, 2.65, 10.5, 2.15),
        (3.5, 2.65, 3.5, 2.15),
    ]

    # Gambar node / Draw nodes
    step_colors = {
        'Langkah 1': COLORS['red'],
        'Langkah 2': COLORS['accent'],
        'Langkah 3': COLORS['primary'],
        'Langkah 4': COLORS['secondary'],
        'Langkah 5': COLORS['teal'],
    }

    for x, y, text, color, step_num in nodes:
        # Kotak node / Node box
        is_step = text.startswith('Langkah')
        is_result = text.startswith('=')

        if is_step:
            bbox_style = dict(boxstyle='round,pad=0.5', facecolor=color, edgecolor='white', alpha=0.9)
            txt_color = 'white'
            fontsize = 10
        elif is_result:
            bbox_style = dict(boxstyle='round,pad=0.5', facecolor=COLORS['secondary'],
                            edgecolor=COLORS['dark'], linewidth=2, alpha=0.9)
            txt_color = 'white'
            fontsize = 16
        else:
            bbox_style = dict(boxstyle='round,pad=0.4', facecolor=COLORS['light'],
                            edgecolor=COLORS['dark'], alpha=0.9)
            txt_color = COLORS['dark']
            fontsize = 10

        ax.text(x, y, text, ha='center', va='center', fontsize=fontsize,
                fontweight='bold' if is_step or is_result else 'normal',
                color=txt_color, bbox=bbox_style, zorder=10)

        # Nomor langkah / Step number
        if step_num:
            ax.text(x - 1.3, y, step_num, ha='center', va='center',
                   fontsize=14, fontweight='bold', color=color)

    # Panah dari langkah ke hasil / Arrows from step to result
    arrow_pairs = [
        (7, 9.0, 7, 7.85),
        (7, 7.15, 3.5, 7.65),
        (3.5, 7.15, 3.5, 6.35),
        (10.5, 6.6, 3.5, 6.35),
        (3.5, 5.65, 3.5, 4.85),
        (10.5, 5.4, 3.5, 4.85),
        (3.5, 4.15, 3.5, 3.35),
        (10.5, 3.9, 3.5, 3.35),
        (3.5, 2.65, 3.5, 2.0),
        (10.5, 2.4, 3.5, 2.0),
    ]

    for x1, y1, x2, y2 in arrow_pairs:
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                   arrowprops=dict(arrowstyle='->', color='#607D8B', lw=1.5))

    ax.text(7, 0.9, 'Hasil / Answer: 2 + 3 × 4² − (6 ÷ 2) = 47',
            ha='center', va='center', fontsize=13, fontweight='bold',
            color=COLORS['dark'],
            bbox=dict(boxstyle='round,pad=0.4', facecolor=COLORS['yellow'],
                     edgecolor=COLORS['dark'], alpha=0.9))

    plt.tight_layout()
    plt.savefig('viz3_order_of_operations.png', dpi=120, bbox_inches='tight',
                facecolor=fig.get_facecolor())
    print("Tersimpan / Saved: viz3_order_of_operations.png")
    return fig


# =============================================================================
# VISUALISASI 4: JAM ARITMATIKA MODULAR / MODULAR ARITHMETIC CLOCK
# =============================================================================

def plot_modular_clock():
    """
    Visualisasi aritmatika modular sebagai jam.
    Visualization of modular arithmetic as a clock.
    """
    fig, axes = plt.subplots(1, 2, figsize=(14, 7))
    fig.suptitle('Visualisasi 4: Jam Aritmatika Modular / Modular Arithmetic Clock',
                 fontsize=15, fontweight='bold')

    def draw_clock(ax, modulus, start, addition, title):
        """Gambar jam modular / Draw modular clock."""
        ax.set_xlim(-1.5, 1.5)
        ax.set_ylim(-1.5, 1.7)
        ax.set_aspect('equal')
        ax.axis('off')
        ax.set_title(title, fontsize=12, fontweight='bold', pad=10)

        # Lingkaran jam / Clock circle
        theta = np.linspace(0, 2*np.pi, 300)
        ax.plot(np.cos(theta), np.sin(theta), color=COLORS['dark'], linewidth=2.5)
        ax.fill(np.cos(theta), np.sin(theta), alpha=0.05, color=COLORS['primary'])

        # Nomor pada jam / Numbers on clock
        positions = []
        for i in range(modulus):
            angle = np.pi/2 - (2*np.pi*i/modulus)  # mulai dari atas / start from top
            x = 1.15 * np.cos(angle)
            y = 1.15 * np.sin(angle)
            positions.append((x, y, angle))

            # Highlight start dan end / Highlight start and end
            result = (start + addition) % modulus
            color = COLORS['accent'] if i == start else \
                    (COLORS['secondary'] if i == result else COLORS['dark'])
            size = 14 if i in [start, result] else 10
            weight = 'bold' if i in [start, result] else 'normal'

            ax.text(x, y, str(i), ha='center', va='center',
                   fontsize=size, fontweight=weight, color=color,
                   bbox=dict(boxstyle='circle,pad=0.2',
                            facecolor=COLORS['yellow'] if i == start else
                            (COLORS['secondary'] if i == result else 'white'),
                            edgecolor=color, alpha=0.9, linewidth=1.5))

            # Garis jam / Clock tick
            x_in = 0.92 * np.cos(angle)
            y_in = 0.92 * np.sin(angle)
            x_out = np.cos(angle)
            y_out = np.sin(angle)
            ax.plot([x_in, x_out], [y_in, y_out], color=COLORS['dark'], linewidth=1)

        # Gambar panah busur / Draw arc arrow
        result = (start + addition) % modulus
        start_angle_deg = 90 - (360*start/modulus)
        end_angle_deg = 90 - (360*result/modulus)

        # Panah melingkar / Circular arrow
        n_arrow_pts = 50
        if addition > 0:
            angles = np.linspace(np.radians(start_angle_deg),
                                np.radians(end_angle_deg - 360 if end_angle_deg > start_angle_deg else end_angle_deg),
                                n_arrow_pts)
        else:
            angles = np.linspace(np.radians(start_angle_deg), np.radians(end_angle_deg), n_arrow_pts)

        r = 0.7
        ax.plot(r * np.cos(angles), r * np.sin(angles),
               color=COLORS['primary'], linewidth=3, alpha=0.8)

        # Ujung panah / Arrowhead
        ax.annotate('',
                   xy=(r * np.cos(angles[-1]), r * np.sin(angles[-1])),
                   xytext=(r * np.cos(angles[-2]), r * np.sin(angles[-2])),
                   arrowprops=dict(arrowstyle='->', color=COLORS['primary'],
                                 lw=2, mutation_scale=15))

        # Label / Labels
        ax.text(0, 0, f'mod {modulus}', ha='center', va='center',
               fontsize=13, fontweight='bold', color=COLORS['dark'])

        ax.text(0, -1.4, f'{start} + {addition} ≡ {result} (mod {modulus})',
               ha='center', va='center', fontsize=11, fontweight='bold',
               color=COLORS['dark'],
               bbox=dict(boxstyle='round,pad=0.4', facecolor=COLORS['light'],
                        edgecolor=COLORS['dark'], alpha=0.9))

        # Legend
        from matplotlib.patches import Patch
        legend_elements = [
            Patch(facecolor=COLORS['yellow'], edgecolor=COLORS['accent'],
                 label=f'Start: {start}'),
            Patch(facecolor=COLORS['secondary'], edgecolor=COLORS['secondary'],
                 label=f'Result: {result}'),
        ]
        ax.legend(handles=legend_elements, loc='upper right', fontsize=9,
                 bbox_to_anchor=(1.35, 1.05))

    draw_clock(axes[0], 12, 9, 5,
               'Jam 12 / 12-Clock\n9 + 5 ≡ 2 (mod 12)')
    draw_clock(axes[1], 7, 3, 10,
               'Minggu/Week (mod 7)\n3 + 10 ≡ 6 (mod 7)\n[0=Sen/Mon,...,6=Min/Sun]')

    plt.tight_layout()
    plt.savefig('viz4_modular_clock.png', dpi=120, bbox_inches='tight',
                facecolor=fig.get_facecolor())
    print("Tersimpan / Saved: viz4_modular_clock.png")
    return fig


# =============================================================================
# VISUALISASI 5: PERTUMBUHAN EKSPONEN / EXPONENT GROWTH CHART
# =============================================================================

def plot_exponent_growth():
    """
    Grafik perbandingan pertumbuhan berbagai fungsi eksponen.
    Chart comparing growth of various exponential functions.
    """
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))
    fig.suptitle('Visualisasi 5: Pertumbuhan Eksponen / Exponent Growth Chart',
                 fontsize=15, fontweight='bold')

    n = np.arange(0, 11)

    # Fungsi-fungsi yang dibandingkan / Functions to compare
    functions = [
        (n**2,    r'$n^2$',       COLORS['primary'],   '-o',  'Kuadrat / Square'),
        (2**n,    r'$2^n$',       COLORS['secondary'], '-s',  'Eksponen 2 / Exp base 2'),
        (3**n,    r'$3^n$',       COLORS['accent'],    '-^',  'Eksponen 3 / Exp base 3'),
        (n**3,    r'$n^3$',       COLORS['purple'],    '-D',  'Kubik / Cubic'),
    ]

    # --- Panel kiri: Skala linear / Left panel: Linear scale ---
    ax1 = axes[0]
    for values, label, color, style, desc in functions:
        # Hanya plot hingga nilai masuk akal / Only plot to reasonable values
        mask = values <= 60000
        ax1.plot(n[mask], values[mask], style, label=f'{label} ({desc})',
                color=color, linewidth=2, markersize=8, alpha=0.85)

    ax1.set_xlabel('n', fontsize=12)
    ax1.set_ylabel('Nilai / Value', fontsize=12)
    ax1.set_title('Skala Linear / Linear Scale', fontsize=12, fontweight='bold')
    ax1.legend(fontsize=9, loc='upper left')
    ax1.grid(True, alpha=0.3)
    ax1.set_xlim(-0.3, 10.3)

    # Anotasi / Annotations
    ax1.annotate('3^n tumbuh jauh\nlebih cepat!\n3^n grows much\nfaster!',
                xy=(7, 3**7), xytext=(5, 3**7 * 0.7),
                arrowprops=dict(arrowstyle='->', color=COLORS['accent']),
                fontsize=9, color=COLORS['accent'], fontweight='bold')

    # --- Panel kanan: Skala log / Right panel: Log scale ---
    ax2 = axes[1]

    n_dense = np.linspace(0.1, 15, 200)
    funcs_cont = [
        (n_dense**2,         r'$n^2$',   COLORS['primary'],   '-',  'Polinomial kuadrat / Quadratic polynomial'),
        (2**n_dense,         r'$2^n$',   COLORS['secondary'], '--', 'Eksponen 2 / Exponential base 2'),
        (3**n_dense,         r'$3^n$',   COLORS['accent'],    ':',  'Eksponen 3 / Exponential base 3'),
        (n_dense**3,         r'$n^3$',   COLORS['purple'],    '-.',  'Kubik / Cubic polynomial'),
        (np.log2(n_dense),   r'$\log_2 n$', COLORS['teal'],  '-',  'Logaritma / Logarithm'),
    ]

    for values, label, color, style, desc in funcs_cont:
        ax2.semilogy(n_dense, np.clip(values, 1e-6, 1e20), style,
                    label=f'{label} ({desc})', color=color, linewidth=2, alpha=0.85)

    ax2.set_xlabel('n', fontsize=12)
    ax2.set_ylabel('log(Nilai / Value)', fontsize=12)
    ax2.set_title('Skala Logaritmik / Logarithmic Scale', fontsize=12, fontweight='bold')
    ax2.legend(fontsize=8, loc='upper left')
    ax2.grid(True, which='both', alpha=0.3)
    ax2.set_xlim(0, 15)
    ax2.set_ylim(0.1, 1e15)

    # Tambahkan tabel nilai / Add value table
    table_data = []
    headers = ['n', 'n²', '2ⁿ', '3ⁿ', 'n³']
    for ni in [0, 2, 4, 6, 8, 10]:
        table_data.append([ni, ni**2, 2**ni, 3**ni, ni**3])

    # Tabel di bawah grafik / Table below chart
    from matplotlib.gridspec import GridSpec

    fig2, ax_table = plt.subplots(figsize=(10, 3.5))
    fig2.suptitle('Tabel Perbandingan / Comparison Table: n², 2ⁿ, 3ⁿ, n³',
                  fontsize=13, fontweight='bold')
    ax_table.axis('off')

    col_labels = headers
    table = ax_table.table(
        cellText=[[str(row[i]) for i in range(len(row))] for row in table_data],
        colLabels=col_labels,
        loc='center',
        cellLoc='center'
    )
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    table.scale(1.5, 2.0)

    # Warnai header / Color headers
    header_colors = ['#37474F', COLORS['primary'], COLORS['secondary'],
                     COLORS['accent'], COLORS['purple']]
    for j, color in enumerate(header_colors):
        table[0, j].set_facecolor(color)
        table[0, j].set_text_props(color='white', fontweight='bold')

    # Warnai baris bergantian / Alternating row colors
    for i in range(1, len(table_data)+1):
        for j in range(len(headers)):
            if i % 2 == 0:
                table[i, j].set_facecolor('#ECEFF1')

    fig2.tight_layout()
    fig2.savefig('viz5b_exponent_table.png', dpi=120, bbox_inches='tight',
                facecolor='white')
    print("Tersimpan / Saved: viz5b_exponent_table.png")
    plt.close(fig2)

    # Simpan grafik utama / Save main chart
    plt.figure(fig.number)
    plt.tight_layout()
    plt.savefig('viz5_exponent_growth.png', dpi=120, bbox_inches='tight',
                facecolor=fig.get_facecolor())
    print("Tersimpan / Saved: viz5_exponent_growth.png")
    return fig


# =============================================================================
# MAIN: Jalankan Semua Visualisasi / Run All Visualizations
# =============================================================================

if __name__ == '__main__':
    print("=" * 60)
    print("  Membuat Visualisasi / Creating Visualizations...")
    print("=" * 60)
    print()

    figs = []
    figs.append(plot_number_line())
    print()
    figs.append(plot_area_model())
    print()
    figs.append(plot_order_of_operations())
    print()
    figs.append(plot_modular_clock())
    print()
    figs.append(plot_exponent_growth())
    print()

    print("=" * 60)
    print("  Semua visualisasi berhasil dibuat! / All visualizations created!")
    print("  File yang dibuat / Files created:")
    print("    viz1_number_line.png")
    print("    viz2_area_model.png")
    print("    viz3_order_of_operations.png")
    print("    viz4_modular_clock.png")
    print("    viz5_exponent_growth.png")
    print("    viz5b_exponent_table.png")
    print("=" * 60)

    # Tampilkan semua / Display all
    plt.show()
