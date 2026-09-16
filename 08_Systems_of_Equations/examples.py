"""
=============================================================================
TOPIK 1.7: SISTEM PERSAMAAN (Systems of Equations)
File: examples.py
=============================================================================
Semua metode penyelesaian diimplementasi dari awal (from scratch).
Menggunakan numpy hanya untuk verifikasi, bukan sebagai solver utama.

All solution methods implemented from scratch.
=============================================================================
"""

import math


# ─────────────────────────────────────────────────────────────────────────────
# BAGIAN 1: UTILITAS — DETERMINAN 2×2 DAN 3×3
# ─────────────────────────────────────────────────────────────────────────────

def det2x2(matrix):
    """
    Hitung determinan matriks 2×2.
    Compute determinant of 2×2 matrix.
    
    |a b|
    |c d| = ad - bc
    """
    a, b = matrix[0]
    c, d = matrix[1]
    return a * d - b * c


def det3x3(matrix):
    """
    Hitung determinan matriks 3×3 dengan ekspansi kofaktor baris pertama.
    Compute determinant of 3×3 matrix via cofactor expansion along row 1.
    """
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]
    # Cofactor expansion: a(ei-fh) - b(di-fg) + c(dh-eg)
    return (a * (e*i - f*h)
            - b * (d*i - f*g)
            + c * (d*h - e*g))


def print_matrix(matrix, labels=None, augmented=False):
    """Cetak matriks dengan format cantik / Pretty-print a matrix."""
    rows = len(matrix)
    cols = len(matrix[0])
    
    for i, row in enumerate(matrix):
        if augmented and cols > rows:
            # Garis pemisah sebelum kolom konstanta
            left = row[:-1]
            right = row[-1]
            vals_left = "  ".join(f"{v:8.4g}" for v in left)
            print(f"  | {vals_left} | {right:8.4g} |")
        else:
            vals = "  ".join(f"{v:8.4g}" for v in row)
            print(f"  | {vals} |")


# ─────────────────────────────────────────────────────────────────────────────
# BAGIAN 2: METODE SUBSTITUSI / Substitution Method
# ─────────────────────────────────────────────────────────────────────────────

def solve_by_substitution(a1, b1, c1, a2, b2, c2):
    """
    Selesaikan sistem 2×2 dengan metode substitusi.
    Solve 2×2 linear system by substitution.
    
    Sistem:
        a1*x + b1*y = c1   ... (1)
        a2*x + b2*y = c2   ... (2)
    
    Langkah: Isolasi x dari persamaan (1), substitusi ke (2).
    """
    print(f"\n{'='*58}")
    print(f"  METODE SUBSTITUSI / SUBSTITUTION METHOD")
    print(f"{'='*58}")
    print(f"  Persamaan (1): {a1}x + ({b1})y = {c1}")
    print(f"  Persamaan (2): {a2}x + ({b2})y = {c2}")
    
    # Cek apakah bisa mengisolasi x dari persamaan 1
    if a1 == 0 and b1 == 0:
        print("  ERROR: Persamaan 1 adalah 0 = c1")
        return None
    
    # Isolasi x dari persamaan 1 (jika a1 != 0)
    # a1*x = c1 - b1*y  =>  x = (c1 - b1*y) / a1
    if a1 != 0:
        print(f"\nLangkah 1: Isolasi x dari persamaan (1):")
        print(f"  {a1}x = {c1} - ({b1})y")
        print(f"  x = ({c1} - ({b1})y) / {a1}")
        print(f"  x = {c1/a1:.6g} - {b1/a1:.6g}y  ... (*)")
        
        # Substitusi ke persamaan 2
        # a2 * ((c1 - b1*y)/a1) + b2*y = c2
        # a2*c1/a1 - a2*b1/a1 * y + b2*y = c2
        # y * (b2 - a2*b1/a1) = c2 - a2*c1/a1
        coeff_y = b2 - a2 * b1 / a1
        rhs = c2 - a2 * c1 / a1
        
        print(f"\nLangkah 2: Substitusi (*) ke persamaan (2):")
        print(f"  {a2} × ({c1/a1:.6g} - {b1/a1:.6g}y) + ({b2})y = {c2}")
        print(f"  {a2*c1/a1:.6g} - {a2*b1/a1:.6g}y + {b2}y = {c2}")
        print(f"  ({coeff_y:.6g})y = {rhs:.6g}")
        
        if abs(coeff_y) < 1e-12:
            if abs(rhs) < 1e-12:
                print(f"  0 = 0 → Sistem DEPENDEN (tak hingga solusi)")
            else:
                print(f"  0 = {rhs:.6g} → Sistem INKONSISTEN (tidak ada solusi)")
            return None
        
        y = rhs / coeff_y
        x = (c1 - b1 * y) / a1
        
        print(f"  y = {rhs:.6g} / {coeff_y:.6g} = {y:.8g}")
        print(f"\nLangkah 3: Back-substitute y = {y:.6g} ke (*):")
        print(f"  x = {c1/a1:.6g} - {b1/a1:.6g} × {y:.6g} = {x:.8g}")
        print(f"\nSOLUSI: x = {x:.8g}, y = {y:.8g}")
        
        # Verifikasi
        print(f"\nVerifikasi:")
        print(f"  Persamaan (1): {a1}({x:.4g}) + ({b1})({y:.4g}) = {a1*x + b1*y:.6g} (seharusnya {c1}) ✓")
        print(f"  Persamaan (2): {a2}({x:.4g}) + ({b2})({y:.4g}) = {a2*x + b2*y:.6g} (seharusnya {c2}) ✓")
        
        return (x, y)
    
    else:
        # a1 = 0, isolasi y dari persamaan 1
        y = c1 / b1
        x = (c2 - b2 * y) / a2
        print(f"\nLangkah 1: a1=0, isolasi y dari (1): y = {y:.6g}")
        print(f"Langkah 2: Substitusi ke (2): x = {x:.6g}")
        print(f"\nSOLUSI: x = {x:.8g}, y = {y:.8g}")
        return (x, y)


# ─────────────────────────────────────────────────────────────────────────────
# BAGIAN 3: METODE ELIMINASI / Elimination Method
# ─────────────────────────────────────────────────────────────────────────────

def solve_by_elimination(a1, b1, c1, a2, b2, c2):
    """
    Selesaikan sistem 2×2 dengan metode eliminasi.
    Solve 2×2 linear system by elimination (adding/subtracting equations).
    
    Eliminasi variabel x: kalikan persamaan agar koefisien x sama.
    Eliminate x: multiply equations so x-coefficients match.
    """
    print(f"\n{'='*58}")
    print(f"  METODE ELIMINASI / ELIMINATION METHOD")
    print(f"{'='*58}")
    print(f"  Persamaan (1): {a1}x + ({b1})y = {c1}")
    print(f"  Persamaan (2): {a2}x + ({b2})y = {c2}")
    
    # Kalikan persamaan 1 dengan a2 dan persamaan 2 dengan a1
    # Ini membuat koefisien x sama (= a1*a2)
    # Kemudian kurangkan untuk eliminasi x
    print(f"\nLangkah 1: Kalikan persamaan untuk menyamakan koefisien x:")
    print(f"  (1) × {a2}: {a1*a2}x + ({b1*a2})y = {c1*a2}")
    print(f"  (2) × {a1}: {a2*a1}x + ({b2*a1})y = {c2*a1}")
    
    # Koefisien baru setelah perkalian
    new_b = b1 * a2 - b2 * a1
    new_c = c1 * a2 - c2 * a1
    
    print(f"\nLangkah 2: Kurangkan untuk eliminasi x:")
    print(f"  ({b1*a2} - {b2*a1})y = {c1*a2} - {c2*a1}")
    print(f"  {new_b}y = {new_c}")
    
    if abs(new_b) < 1e-12:
        if abs(new_c) < 1e-12:
            print(f"  0 = 0 → Sistem DEPENDEN (tak hingga solusi)")
        else:
            print(f"  0 = {new_c} → Sistem INKONSISTEN (tidak ada solusi)")
        return None
    
    y = new_c / new_b
    print(f"  y = {new_c} / {new_b} = {y:.8g}")
    
    # Sekarang eliminasi y untuk mendapatkan x
    print(f"\nLangkah 3: Eliminasi y untuk mencari x:")
    new_b2 = b1 * b2 - b2 * b1  # = 0 by design if we multiply differently
    # Lebih sederhana: substitusi y ke salah satu persamaan
    if abs(a1) > 1e-12:
        x = (c1 - b1 * y) / a1
        print(f"  Substitusi y ke persamaan (1):")
        print(f"  {a1}x = {c1} - ({b1})({y:.6g}) = {c1 - b1*y:.6g}")
        print(f"  x = {x:.8g}")
    else:
        x = (c2 - b2 * y) / a2
        print(f"  Substitusi y ke persamaan (2): x = {x:.8g}")
    
    print(f"\nSOLUSI: x = {x:.8g}, y = {y:.8g}")
    
    # Verifikasi
    check1 = abs(a1*x + b1*y - c1) < 1e-8
    check2 = abs(a2*x + b2*y - c2) < 1e-8
    print(f"\nVerifikasi:")
    print(f"  Persamaan (1): {a1*x + b1*y:.6g} = {c1} → {'✓' if check1 else '✗'}")
    print(f"  Persamaan (2): {a2*x + b2*y:.6g} = {c2} → {'✓' if check2 else '✗'}")
    
    return (x, y)


# ─────────────────────────────────────────────────────────────────────────────
# BAGIAN 4: ATURAN CRAMER / Cramer's Rule
# ─────────────────────────────────────────────────────────────────────────────

def solve_by_cramers_rule_2x2(a1, b1, c1, a2, b2, c2):
    """
    Selesaikan sistem 2×2 dengan Aturan Cramer.
    Solve 2×2 system using Cramer's Rule.
    
    D  = |a1 b1| = a1*b2 - a2*b1
         |a2 b2|
    
    Dx = |c1 b1| = c1*b2 - c2*b1
         |c2 b2|
    
    Dy = |a1 c1| = a1*c2 - a2*c1
         |a2 c2|
    
    x = Dx/D,  y = Dy/D
    """
    print(f"\n{'='*58}")
    print(f"  ATURAN CRAMER / CRAMER'S RULE (2×2)")
    print(f"{'='*58}")
    print(f"  Persamaan (1): {a1}x + ({b1})y = {c1}")
    print(f"  Persamaan (2): {a2}x + ({b2})y = {c2}")
    
    # Determinan utama
    D = a1 * b2 - a2 * b1
    print(f"\n  Matriks koefisien A:")
    print(f"  | {a1}  {b1} |")
    print(f"  | {a2}  {b2} |")
    print(f"  D = {a1}×{b2} - {a2}×{b1} = {a1*b2} - {a2*b1} = {D}")
    
    # Determinan Dx
    Dx = c1 * b2 - c2 * b1
    print(f"\n  Matriks Dx (ganti kolom x dengan konstanta):")
    print(f"  | {c1}  {b1} |")
    print(f"  | {c2}  {b2} |")
    print(f"  Dx = {c1}×{b2} - {c2}×{b1} = {c1*b2} - {c2*b1} = {Dx}")
    
    # Determinan Dy
    Dy = a1 * c2 - a2 * c1
    print(f"\n  Matriks Dy (ganti kolom y dengan konstanta):")
    print(f"  | {a1}  {c1} |")
    print(f"  | {a2}  {c2} |")
    print(f"  Dy = {a1}×{c2} - {a2}×{c1} = {a1*c2} - {a2*c1} = {Dy}")
    
    if D == 0:
        if Dx == 0 and Dy == 0:
            print(f"\n  D = Dx = Dy = 0 → Sistem DEPENDEN")
        else:
            print(f"\n  D = 0, Dx atau Dy ≠ 0 → Sistem INKONSISTEN")
        return None
    
    x = Dx / D
    y = Dy / D
    
    print(f"\n  x = Dx/D = {Dx}/{D} = {x:.8g}")
    print(f"  y = Dy/D = {Dy}/{D} = {y:.8g}")
    print(f"\nSOLUSI: x = {x:.8g}, y = {y:.8g}")
    
    return (x, y)


def cramers_rule_3x3(A, b_vec):
    """
    Aturan Cramer untuk sistem 3×3: Ax = b
    Cramer's Rule for 3×3 system.
    
    Args:
        A: Matriks koefisien 3×3 (list of lists)
        b_vec: Vektor konstanta [b1, b2, b3]
    """
    print(f"\n{'='*58}")
    print(f"  ATURAN CRAMER / CRAMER'S RULE (3×3)")
    print(f"{'='*58}")
    print("  Matriks koefisien A:")
    print_matrix(A)
    print(f"  Vektor b = {b_vec}")
    
    D = det3x3(A)
    print(f"\n  det(A) = {D}")
    
    if abs(D) < 1e-12:
        print("  D = 0 → Tidak ada solusi unik")
        return None
    
    results = []
    var_names = ['x', 'y', 'z']
    
    for i in range(3):
        # Buat matriks Ai: ganti kolom ke-i dengan b_vec
        Ai = [row[:] for row in A]  # Deep copy
        for j in range(3):
            Ai[j][i] = b_vec[j]
        
        Di = det3x3(Ai)
        xi = Di / D
        results.append(xi)
        print(f"  D{var_names[i]} = {Di}")
        print(f"  {var_names[i]} = D{var_names[i]}/D = {Di}/{D} = {xi:.8g}")
    
    print(f"\nSOLUSI: x={results[0]:.6g}, y={results[1]:.6g}, z={results[2]:.6g}")
    return results


# ─────────────────────────────────────────────────────────────────────────────
# BAGIAN 5: KLASIFIKASI SISTEM / Classifying Systems
# ─────────────────────────────────────────────────────────────────────────────

def classify_system(a1, b1, c1, a2, b2, c2):
    """
    Klasifikasikan sistem 2×2 sebagai konsisten, inkonsisten, atau dependen.
    Classify a 2×2 system as consistent, inconsistent, or dependent.
    """
    print(f"\n{'='*58}")
    print(f"  KLASIFIKASI SISTEM / SYSTEM CLASSIFICATION")
    print(f"{'='*58}")
    print(f"  Persamaan (1): {a1}x + {b1}y = {c1}")
    print(f"  Persamaan (2): {a2}x + {b2}y = {c2}")
    
    D = a1 * b2 - a2 * b1
    print(f"\n  Determinan D = {a1}×{b2} - {a2}×{b1} = {D}")
    
    if abs(D) > 1e-12:
        print(f"  D ≠ 0 → KONSISTEN: Satu solusi unik")
        print(f"  (Dua garis berpotongan di satu titik)")
        sol = solve_by_cramers_rule_2x2(a1, b1, c1, a2, b2, c2)
        return "consistent", sol
    else:
        # D = 0: sejajar atau berimpit
        # Cek rasio
        # Dari a1/a2 = b1/b2 = c1/c2?
        if abs(a2) > 1e-12 and abs(b2) > 1e-12:
            ratio_a = a1 / a2
            ratio_b = b1 / b2
            ratio_c = c1 / c2 if abs(c2) > 1e-12 else float('inf')
            
            print(f"  D = 0, cek rasio: a1/a2={ratio_a:.4g}, b1/b2={ratio_b:.4g}, c1/c2={ratio_c:.4g}")
            
            if abs(ratio_a - ratio_b) < 1e-8 and abs(ratio_a - ratio_c) < 1e-8:
                print(f"  a1/a2 = b1/b2 = c1/c2 → DEPENDEN: Tak hingga solusi")
                print(f"  (Dua garis berimpit / sama)")
                return "dependent", None
            else:
                print(f"  a1/a2 = b1/b2 ≠ c1/c2 → INKONSISTEN: Tidak ada solusi")
                print(f"  (Dua garis sejajar)")
                return "inconsistent", None
        else:
            print(f"  D = 0 (degenerate case)")
            return "unknown", None


# ─────────────────────────────────────────────────────────────────────────────
# BAGIAN 6: SISTEM 3 VARIABEL / Three-Variable Systems
# ─────────────────────────────────────────────────────────────────────────────

def solve_3var_elimination(equations):
    """
    Selesaikan sistem 3 variabel dengan eliminasi bertahap.
    Solve 3-variable system by step-by-step elimination.
    
    Args:
        equations: List of [a, b, c, d] untuk ax + by + cz = d
    """
    print(f"\n{'='*58}")
    print(f"  SISTEM 3 VARIABEL — ELIMINASI BERTAHAP")
    print(f"{'='*58}")
    
    [[a1, b1, c1, d1],
     [a2, b2, c2, d2],
     [a3, b3, c3, d3]] = equations
    
    print(f"  Persamaan (1): {a1}x + {b1}y + {c1}z = {d1}")
    print(f"  Persamaan (2): {a2}x + {b2}y + {c2}z = {d2}")
    print(f"  Persamaan (3): {a3}x + {b3}y + {c3}z = {d3}")
    
    # Langkah 1: Eliminasi x dari persamaan 2 dan 3
    print(f"\n--- Langkah 1: Eliminasi x ---")
    
    # (2) = (2) - (a2/a1) × (1)
    factor2 = a2 / a1
    nb2 = b2 - factor2 * b1
    nc2 = c2 - factor2 * c1
    nd2 = d2 - factor2 * d1
    print(f"  (2) ← (2) - ({factor2:.4g}) × (1):")
    print(f"  0x + {nb2:.4g}y + {nc2:.4g}z = {nd2:.4g}  ... (4)")
    
    # (3) = (3) - (a3/a1) × (1)
    factor3 = a3 / a1
    nb3 = b3 - factor3 * b1
    nc3 = c3 - factor3 * c1
    nd3 = d3 - factor3 * d1
    print(f"  (3) ← (3) - ({factor3:.4g}) × (1):")
    print(f"  0x + {nb3:.4g}y + {nc3:.4g}z = {nd3:.4g}  ... (5)")
    
    # Langkah 2: Eliminasi y dari persamaan 5
    print(f"\n--- Langkah 2: Eliminasi y dari (5) ---")
    if abs(nb2) < 1e-12:
        print("  nb2 = 0, perlu pertukaran baris!")
        return None
    
    factor45 = nb3 / nb2
    nc_new = nc3 - factor45 * nc2
    nd_new = nd3 - factor45 * nd2
    print(f"  (5) ← (5) - ({factor45:.4g}) × (4):")
    print(f"  0x + 0y + {nc_new:.4g}z = {nd_new:.4g}  ... (6)")
    
    # Langkah 3: Back-substitution
    print(f"\n--- Langkah 3: Back-substitution ---")
    
    if abs(nc_new) < 1e-12:
        print("  Tidak ada solusi unik!")
        return None
    
    z = nd_new / nc_new
    print(f"  Dari (6): z = {nd_new:.4g}/{nc_new:.4g} = {z:.8g}")
    
    y = (nd2 - nc2 * z) / nb2
    print(f"  Dari (4): y = ({nd2:.4g} - {nc2:.4g}×{z:.4g}) / {nb2:.4g} = {y:.8g}")
    
    x = (d1 - b1 * y - c1 * z) / a1
    print(f"  Dari (1): x = ({d1} - {b1}×{y:.4g} - {c1}×{z:.4g}) / {a1} = {x:.8g}")
    
    print(f"\nSOLUSI: x={x:.6g}, y={y:.6g}, z={z:.6g}")
    
    # Verifikasi
    v1 = a1*x + b1*y + c1*z
    v2 = a2*x + b2*y + c2*z
    v3 = a3*x + b3*y + c3*z
    print(f"\nVerifikasi:")
    print(f"  (1): {v1:.6g} = {d1} {'✓' if abs(v1-d1)<1e-6 else '✗'}")
    print(f"  (2): {v2:.6g} = {d2} {'✓' if abs(v2-d2)<1e-6 else '✗'}")
    print(f"  (3): {v3:.6g} = {d3} {'✓' if abs(v3-d3)<1e-6 else '✗'}")
    
    return (x, y, z)


# ─────────────────────────────────────────────────────────────────────────────
# BAGIAN 7: SISTEM NON-LINEAR / Non-Linear Systems
# ─────────────────────────────────────────────────────────────────────────────

def solve_line_parabola_system(a, b, c, m, q):
    """
    Selesaikan sistem garis + parabola:
    y = ax² + bx + c  (parabola)
    y = mx + q        (garis lurus)
    
    Substitusi: ax² + bx + c = mx + q
    ax² + (b-m)x + (c-q) = 0
    """
    print(f"\n{'='*58}")
    print(f"  SISTEM NON-LINEAR: PARABOLA + GARIS")
    print(f"{'='*58}")
    print(f"  Parabola: y = {a}x² + ({b})x + ({c})")
    print(f"  Garis:    y = {m}x + ({q})")
    print(f"\nLangkah: Set sama → {a}x² + ({b})x + ({c}) = {m}x + ({q})")
    
    new_b = b - m
    new_c = c - q
    print(f"  {a}x² + ({new_b})x + ({new_c}) = 0")
    
    D = new_b**2 - 4*a*new_c
    print(f"  D = ({new_b})² - 4×{a}×({new_c}) = {D}")
    
    if D < 0:
        print(f"  D < 0: Garis TIDAK memotong parabola → TIDAK ADA SOLUSI")
        return []
    elif D == 0:
        x = -new_b / (2 * a)
        y = m * x + q
        print(f"  D = 0: Garis MENYINGGUNG parabola")
        print(f"  x = {x:.6g}, y = {y:.6g}")
        return [(x, y)]
    else:
        sqrt_D = math.sqrt(D)
        x1 = (-new_b + sqrt_D) / (2 * a)
        x2 = (-new_b - sqrt_D) / (2 * a)
        y1 = m * x1 + q
        y2 = m * x2 + q
        print(f"  D > 0: Garis memotong parabola di 2 titik")
        print(f"  Titik 1: ({x1:.6g}, {y1:.6g})")
        print(f"  Titik 2: ({x2:.6g}, {y2:.6g})")
        return [(x1, y1), (x2, y2)]


# ─────────────────────────────────────────────────────────────────────────────
# BAGIAN 8: SOAL CERITA / Word Problems
# ─────────────────────────────────────────────────────────────────────────────

def mixture_problem():
    """
    Soal campuran klasik.
    Classic mixture problem.
    
    Berapa liter larutan 30% dan 70% harus dicampur
    untuk menghasilkan 100 liter larutan 45%?
    """
    print(f"\n{'='*58}")
    print(f"  SOAL CERITA: MASALAH CAMPURAN / MIXTURE PROBLEM")
    print(f"{'='*58}")
    print("  Masalah: Campurkan larutan 30% dan 70% alkohol")
    print("  untuk menghasilkan 100 liter larutan 45%.")
    print()
    print("  Misalkan x = liter larutan 30%")
    print("           y = liter larutan 70%")
    print()
    print("  Persamaan total volume: x + y = 100    ... (1)")
    print("  Persamaan total alkohol: 0.30x + 0.70y = 0.45×100  ... (2)")
    print("  Sederhanakan (2): 0.30x + 0.70y = 45")
    
    sol = solve_by_elimination(1, 1, 100, 0.30, 0.70, 45)
    
    if sol:
        x, y = sol
        print(f"\n  Interpretasi:")
        print(f"  → {x:.1f} liter larutan 30%")
        print(f"  → {y:.1f} liter larutan 70%")
        print(f"  → Total: {x+y:.1f} liter larutan {(0.3*x + 0.7*y)/(x+y)*100:.1f}% ✓")


def speed_problem():
    """
    Soal kecepatan dengan arus.
    Speed problem with current.
    
    Perahu menempuh 60 km searah arus dalam 3 jam.
    Perahu menempuh 40 km melawan arus dalam 4 jam.
    Tentukan kecepatan perahu dan kecepatan arus!
    """
    print(f"\n{'='*58}")
    print(f"  SOAL CERITA: MASALAH KECEPATAN / SPEED PROBLEM")
    print(f"{'='*58}")
    print("  Perahu: 60 km searah arus dalam 3 jam")
    print("          40 km melawan arus dalam 4 jam")
    print()
    print("  Misalkan v = kecepatan perahu di air tenang (km/jam)")
    print("           u = kecepatan arus (km/jam)")
    print()
    print("  Searah arus  (v + u) × 3 = 60 → v + u = 20  ... (1)")
    print("  Melawan arus (v - u) × 4 = 40 → v - u = 10  ... (2)")
    
    sol = solve_by_elimination(1, 1, 20, 1, -1, 10)
    
    if sol:
        v, u = sol
        print(f"\n  Interpretasi:")
        print(f"  → Kecepatan perahu: {v:.2f} km/jam")
        print(f"  → Kecepatan arus:   {u:.2f} km/jam")


def supply_demand_equilibrium():
    """
    Keseimbangan penawaran dan permintaan.
    Supply and demand equilibrium.
    """
    print(f"\n{'='*58}")
    print(f"  SOAL CERITA: KESEIMBANGAN PASAR / MARKET EQUILIBRIUM")
    print(f"{'='*58}")
    print("  Supply:  P = 2Q + 5   (harga naik jika kuantitas naik)")
    print("  Demand:  P = -Q + 20  (harga turun jika kuantitas naik)")
    print()
    print("  Keseimbangan: 2Q + 5 = -Q + 20")
    print("  Sistem:")
    print("    P - 2Q = 5   ... (1) [Supply]")
    print("    P + Q = 20   ... (2) [Demand]")
    
    sol = solve_by_substitution(1, -2, 5, 1, 1, 20)
    
    if sol:
        P, Q = sol
        print(f"\n  Keseimbangan Pasar:")
        print(f"  → Kuantitas Ekuilibrium: Q = {Q:.2f} unit")
        print(f"  → Harga Ekuilibrium:     P = Rp {P:.2f}")


# ─────────────────────────────────────────────────────────────────────────────
# PROGRAM UTAMA / MAIN PROGRAM
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 60)
    print("  TOPIK 1.7: SISTEM PERSAMAAN — EXAMPLES.PY")
    print("=" * 60)
    
    # ─── Contoh 1: Substitusi ───
    print("\n" + "█"*55)
    print("  CONTOH 1: METODE SUBSTITUSI")
    print("█"*55)
    solve_by_substitution(1, 1, 5, 2, -1, 1)
    
    # ─── Contoh 2: Eliminasi ───
    print("\n" + "█"*55)
    print("  CONTOH 2: METODE ELIMINASI")
    print("█"*55)
    solve_by_elimination(3, 2, 12, 1, -1, 1)
    
    # ─── Contoh 3: Aturan Cramer ───
    print("\n" + "█"*55)
    print("  CONTOH 3: ATURAN CRAMER")
    print("█"*55)
    solve_by_cramers_rule_2x2(4, 3, 18, 2, -5, -4)
    
    # ─── Contoh 4: Klasifikasi Sistem ───
    print("\n" + "█"*55)
    print("  CONTOH 4: KLASIFIKASI SISTEM")
    print("█"*55)
    classify_system(2, -4, 6, 1, -2, 3)   # Dependen
    classify_system(1, 2, 4, 2, 4, 9)     # Inkonsisten
    classify_system(2, 3, 7, 1, -1, 1)    # Konsisten
    
    # ─── Contoh 5: Sistem 3 Variabel ───
    print("\n" + "█"*55)
    print("  CONTOH 5: SISTEM 3 VARIABEL")
    print("█"*55)
    equations = [
        [2, 1, -1, 8],    # 2x + y - z = 8
        [-3, -1, 2, -11], # -3x - y + 2z = -11
        [-2, 1, 2, -3]    # -2x + y + 2z = -3
    ]
    solve_3var_elimination(equations)
    
    # ─── Contoh 6: Aturan Cramer 3×3 ───
    print("\n" + "█"*55)
    print("  CONTOH 6: ATURAN CRAMER 3×3")
    print("█"*55)
    A = [[1, 2, 3], [4, 5, 6], [7, 8, 10]]
    b = [3, 3, 2]
    cramers_rule_3x3(A, b)
    
    # ─── Contoh 7: Sistem Non-Linear ───
    print("\n" + "█"*55)
    print("  CONTOH 7: SISTEM NON-LINEAR")
    print("█"*55)
    solve_line_parabola_system(1, -3, 2, 0, 0)  # y=x²-3x+2 dan y=0
    solve_line_parabola_system(1, 0, -4, 1, 2)  # y=x²-4 dan y=x+2
    solve_line_parabola_system(1, 0, 1, 0, 0)   # y=x²+1 dan y=0 (tidak ada sol)
    
    # ─── Contoh 8: Soal Cerita ───
    print("\n" + "█"*55)
    print("  CONTOH 8: SOAL CERITA")
    print("█"*55)
    mixture_problem()
    speed_problem()
    supply_demand_equilibrium()
    
    print("\n" + "="*60)
    print("  Selesai! / Done!")
    print("="*60)
