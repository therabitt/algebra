"""
=============================================================================
TOPIK 1.6: PERSAMAAN KUADRAT (Quadratic Equations)
File: examples.py
=============================================================================
Implementasi semua metode dari awal (from scratch) tanpa menggunakan
fungsi solve/roots bawaan — semua logika kita tulis sendiri!

All solving methods implemented from scratch without using built-in solve/roots.
=============================================================================
"""

import math
import cmath  # for complex number math

# ─────────────────────────────────────────────────────────────────────────────
# BAGIAN 1: ANALISIS DISKRIMINAN / Discriminant Analysis
# ─────────────────────────────────────────────────────────────────────────────

def discriminant(a, b, c):
    """
    Hitung diskriminan D = b² - 4ac
    Compute discriminant D = b^2 - 4ac
    
    Args:
        a, b, c: Koefisien ax² + bx + c = 0
    Returns:
        float: Nilai diskriminan
    """
    return b**2 - 4*a*c


def analyze_discriminant(a, b, c):
    """
    Analisis jenis akar berdasarkan diskriminan.
    Analyze the nature of roots based on discriminant.
    """
    D = discriminant(a, b, c)
    
    print(f"\n{'='*55}")
    print(f"  Persamaan: {a}x² + ({b})x + ({c}) = 0")
    print(f"  Diskriminan D = b² - 4ac = ({b})² - 4({a})({c})")
    print(f"  D = {b**2} - {4*a*c} = {D}")
    print(f"{'='*55}")
    
    if D > 0:
        # Cek apakah D adalah kuadrat sempurna
        sqrt_D = math.sqrt(D)
        if sqrt_D == int(sqrt_D):
            print(f"  D > 0 dan √D = {int(sqrt_D)} (bilangan bulat)")
            print(f"  → DUA AKAR REAL RASIONAL BERBEDA")
        else:
            print(f"  D > 0 dan √D = {sqrt_D:.6f} (irasional)")
            print(f"  → DUA AKAR REAL IRASIONAL BERBEDA (conjugate surds)")
    elif D == 0:
        print(f"  D = 0")
        print(f"  → SATU AKAR REAL KEMBAR (repeated root)")
    else:
        print(f"  D < 0 (D = {D})")
        print(f"  → DUA AKAR KOMPLEKS KONJUGAT (non-real)")
    
    return D


# ─────────────────────────────────────────────────────────────────────────────
# BAGIAN 2: METODE FAKTORISASI / Factoring Method
# ─────────────────────────────────────────────────────────────────────────────

def solve_by_factoring_integer(a, b, c):
    """
    Selesaikan ax² + bx + c = 0 dengan faktorisasi integer.
    Solve by integer factoring (works when roots are integers).
    
    Strategi: Cari dua bilangan p, q sedemikian hingga p+q = b dan p*q = a*c
    Strategy: Find p, q such that p+q = b and p*q = a*c
    """
    print(f"\n--- METODE FAKTORISASI ---")
    print(f"Persamaan: {a}x² + {b}x + {c} = 0")
    
    # Cari faktorisasi: ax² + bx + c = a(x - r1)(x - r2)
    # Dengan ac = a*c, kita cari p, q: p + q = b, p * q = a * c
    target_product = a * c
    print(f"Cari p, q dengan: p + q = {b} dan p × q = {target_product}")
    
    found = False
    for p in range(-abs(target_product) - 1, abs(target_product) + 2):
        if p != 0 and target_product % p == 0:
            q = target_product // p
            if p + q == b:
                print(f"Ditemukan: p = {p}, q = {q}")
                found = True
                break
    
    if not found:
        print("Tidak ada faktorisasi integer! Gunakan rumus kuadrat.")
        return None
    
    # Penyelesaian via zero product property
    # ax² + bx + c = ax² + px + qx + c = x(ax + p) + (c/a)(ax + q)
    # Lebih mudah: akar adalah solusi langsung dari rumus
    D = discriminant(a, b, c)
    if D < 0:
        return None
    
    sqrt_D = math.sqrt(D)
    r1 = (-b + sqrt_D) / (2*a)
    r2 = (-b - sqrt_D) / (2*a)
    
    print(f"Faktorisasi: {a}(x - {r1:.4g})(x - {r2:.4g}) = 0")
    print(f"Akar: x₁ = {r1:.6g}, x₂ = {r2:.6g}")
    return (r1, r2)


# ─────────────────────────────────────────────────────────────────────────────
# BAGIAN 3: COMPLETING THE SQUARE (Melengkapkan Kuadrat)
# ─────────────────────────────────────────────────────────────────────────────

def solve_by_completing_square(a, b, c, verbose=True):
    """
    Selesaikan ax² + bx + c = 0 dengan metode melengkapkan kuadrat.
    Solve by completing the square — shows every algebraic step.
    """
    if verbose:
        print(f"\n--- MELENGKAPKAN KUADRAT / COMPLETING THE SQUARE ---")
        print(f"Persamaan awal: {a}x² + ({b})x + ({c}) = 0\n")
        
        # Langkah 1: Bagi dengan a
        print(f"Langkah 1: Bagi semua suku dengan a = {a}:")
        print(f"  x² + ({b}/{a})x + ({c}/{a}) = 0")
        print(f"  x² + ({b/a:.6g})x + ({c/a:.6g}) = 0\n")
        
        # Langkah 2: Pindahkan konstanta
        print(f"Langkah 2: Pindahkan konstanta ke kanan:")
        print(f"  x² + ({b/a:.6g})x = {-c/a:.6g}\n")
        
        # Langkah 3: Tambahkan (b/2a)² = (b/(2a))²
        half_b_over_a = b / (2 * a)
        square_term = half_b_over_a**2
        print(f"Langkah 3: Tambahkan (b/2a)² = ({b}/2·{a})² = ({half_b_over_a:.6g})² = {square_term:.6g} ke kedua ruas:")
        print(f"  x² + ({b/a:.6g})x + {square_term:.6g} = {-c/a:.6g} + {square_term:.6g}")
        
        right_side = -c/a + square_term
        print(f"  x² + ({b/a:.6g})x + {square_term:.6g} = {right_side:.6g}\n")
        
        # Langkah 4: Ruas kiri adalah kuadrat sempurna
        print(f"Langkah 4: Ruas kiri adalah kuadrat sempurna (x + b/2a)²:")
        print(f"  (x + {half_b_over_a:.6g})² = {right_side:.6g}\n")
        
        # Langkah 5: Akar kuadrat kedua ruas
        print(f"Langkah 5: Ambil akar kuadrat:")
        if right_side < 0:
            print(f"  x + {half_b_over_a:.6g} = ±i√{abs(right_side):.6g}")
            print(f"  x + {half_b_over_a:.6g} = ±{math.sqrt(abs(right_side)):.6g}i")
        else:
            print(f"  x + {half_b_over_a:.6g} = ±√{right_side:.6g}")
            print(f"  x + {half_b_over_a:.6g} = ±{math.sqrt(right_side):.6g}")
        
        # Langkah 6: Selesaikan x
        print(f"\nLangkah 6: Selesaikan x:")
        print(f"  x = -{half_b_over_a:.6g} ± {math.sqrt(abs(right_side)):.6g}{'i' if right_side < 0 else ''}")
    
    # Hitung akar
    D = discriminant(a, b, c)
    
    if D >= 0:
        sqrt_D = math.sqrt(D)
        x1 = (-b + sqrt_D) / (2 * a)
        x2 = (-b - sqrt_D) / (2 * a)
        if verbose:
            print(f"\n  x₁ = {x1:.6g}")
            print(f"  x₂ = {x2:.6g}")
        return (x1, x2)
    else:
        real_part = -b / (2 * a)
        imag_part = math.sqrt(-D) / (2 * a)
        x1 = complex(real_part, imag_part)
        x2 = complex(real_part, -imag_part)
        if verbose:
            print(f"\n  x₁ = {real_part:.6g} + {imag_part:.6g}i")
            print(f"  x₂ = {real_part:.6g} - {imag_part:.6g}i")
        return (x1, x2)


# ─────────────────────────────────────────────────────────────────────────────
# BAGIAN 4: RUMUS KUADRAT / Quadratic Formula
# ─────────────────────────────────────────────────────────────────────────────

def solve_quadratic_formula(a, b, c, verbose=True):
    """
    Selesaikan ax² + bx + c = 0 menggunakan rumus kuadrat.
    Solve using the quadratic formula: x = (-b ± √(b²-4ac)) / 2a
    
    Menangani semua kasus: D>0, D=0, D<0 (termasuk akar kompleks)
    Handles all cases including complex roots.
    """
    if verbose:
        print(f"\n--- RUMUS KUADRAT / QUADRATIC FORMULA ---")
        print(f"Persamaan: {a}x² + ({b})x + ({c}) = 0")
        print(f"Formula: x = (-b ± √(b²-4ac)) / 2a")
        print(f"         x = (-({b}) ± √(({b})²-4·({a})·({c}))) / 2·({a})")
    
    D = discriminant(a, b, c)
    
    if verbose:
        print(f"\nD = {b}² - 4·{a}·{c} = {b**2} - {4*a*c} = {D}")
    
    if D > 0:
        sqrt_D = math.sqrt(D)
        x1 = (-b + sqrt_D) / (2 * a)
        x2 = (-b - sqrt_D) / (2 * a)
        if verbose:
            print(f"D = {D} > 0 → DUA AKAR REAL BERBEDA")
            print(f"x₁ = ({-b} + √{D}) / {2*a} = ({-b} + {sqrt_D:.6g}) / {2*a} = {x1:.8g}")
            print(f"x₂ = ({-b} - √{D}) / {2*a} = ({-b} - {sqrt_D:.6g}) / {2*a} = {x2:.8g}")
        return (x1, x2)
    
    elif D == 0:
        x = -b / (2 * a)
        if verbose:
            print(f"D = 0 → SATU AKAR KEMBAR")
            print(f"x₁ = x₂ = -b/(2a) = {-b}/{2*a} = {x:.8g}")
        return (x, x)
    
    else:  # D < 0
        real_part = -b / (2 * a)
        imag_part = math.sqrt(-D) / (2 * a)
        x1 = complex(real_part, imag_part)
        x2 = complex(real_part, -imag_part)
        if verbose:
            print(f"D = {D} < 0 → DUA AKAR KOMPLEKS KONJUGAT")
            print(f"√D = √({D}) = {math.sqrt(-D):.6g}i")
            print(f"x₁ = {real_part:.6g} + {imag_part:.6g}i")
            print(f"x₂ = {real_part:.6g} - {imag_part:.6g}i")
        return (x1, x2)


# ─────────────────────────────────────────────────────────────────────────────
# BAGIAN 5: RUMUS VIETA / Vieta's Formulas
# ─────────────────────────────────────────────────────────────────────────────

def vietas_formulas(a, b, c):
    """
    Demonstrasi Rumus Vieta dan verifikasi dengan akar yang dihitung.
    Demonstrate Vieta's formulas and verify with computed roots.
    
    Vieta's formulas:
    - Sum of roots:     x₁ + x₂ = -b/a
    - Product of roots: x₁ · x₂ = c/a
    """
    print(f"\n--- RUMUS VIETA / VIETA'S FORMULAS ---")
    print(f"Persamaan: {a}x² + ({b})x + ({c}) = 0")
    
    # Rumus Vieta secara teoritis
    sum_vieta = -b / a
    product_vieta = c / a
    print(f"\nMenurut Rumus Vieta:")
    print(f"  Jumlah akar (sum):    x₁ + x₂ = -b/a = -({b})/{a} = {sum_vieta:.6g}")
    print(f"  Hasil kali (product): x₁ × x₂ = c/a = ({c})/{a} = {product_vieta:.6g}")
    
    # Hitung akar aktual untuk verifikasi
    roots = solve_quadratic_formula(a, b, c, verbose=False)
    x1, x2 = roots
    
    print(f"\nVerifikasi dengan akar yang dihitung:")
    print(f"  Akar: x₁ = {x1}, x₂ = {x2}")
    
    actual_sum = x1 + x2
    actual_product = x1 * x2
    
    print(f"  x₁ + x₂ = {actual_sum:.6g}  (Vieta: {sum_vieta:.6g})  ✓ Match: {abs(actual_sum - sum_vieta) < 1e-9}")
    print(f"  x₁ × x₂ = {actual_product:.6g}  (Vieta: {product_vieta:.6g})  ✓ Match: {abs(actual_product - product_vieta) < 1e-9}")
    
    return sum_vieta, product_vieta


# ─────────────────────────────────────────────────────────────────────────────
# BAGIAN 6: KONVERSI ANTAR BENTUK / Converting Between Forms
# ─────────────────────────────────────────────────────────────────────────────

def standard_to_vertex_form(a, b, c):
    """
    Konversi dari bentuk standar ax² + bx + c ke bentuk vertex a(x-h)² + k
    Convert from standard form to vertex form.
    
    h = -b/(2a)  (x-koordinat vertex)
    k = c - b²/(4a)  (y-koordinat vertex)
    """
    print(f"\n--- KONVERSI KE BENTUK VERTEX / VERTEX FORM CONVERSION ---")
    print(f"Bentuk standar: f(x) = {a}x² + ({b})x + ({c})")
    
    h = -b / (2 * a)
    k = c - b**2 / (4 * a)
    
    print(f"\nMenghitung vertex:")
    print(f"  h = -b/(2a) = -({b})/(2·{a}) = {h:.6g}")
    print(f"  k = c - b²/(4a) = {c} - ({b})²/(4·{a}) = {c} - {b**2/(4*a):.6g} = {k:.6g}")
    
    sign_h = "-" if h >= 0 else "+"
    abs_h = abs(h)
    sign_k = "+" if k >= 0 else "-"
    abs_k = abs(k)
    
    print(f"\nBentuk vertex: f(x) = {a}(x {sign_h} {abs_h:.4g})² {sign_k} {abs_k:.4g}")
    print(f"Vertex (titik puncak): ({h:.4g}, {k:.4g})")
    print(f"Poros simetri: x = {h:.4g}")
    
    # Nilai extremum
    if a > 0:
        print(f"Nilai minimum: {k:.4g} (dicapai di x = {h:.4g})")
    else:
        print(f"Nilai maksimum: {k:.4g} (dicapai di x = {h:.4g})")
    
    return h, k


def vertex_to_standard_form(a, h, k):
    """
    Konversi dari bentuk vertex a(x-h)² + k ke bentuk standar ax² + bx + c
    Convert from vertex form to standard form.
    
    a(x-h)² + k = a(x² - 2hx + h²) + k = ax² - 2ahx + ah² + k
    """
    print(f"\n--- KONVERSI KE BENTUK STANDAR / STANDARD FORM CONVERSION ---")
    print(f"Bentuk vertex: f(x) = {a}(x - {h})² + {k}")
    print(f"\nEkspansi: {a}(x - {h})² + {k}")
    print(f"= {a}(x² - 2·{h}·x + {h}²) + {k}")
    print(f"= {a}x² - {2*a*h}x + {a*h**2} + {k}")
    
    new_a = a
    new_b = -2 * a * h
    new_c = a * h**2 + k
    
    print(f"= {new_a}x² + ({new_b:.4g})x + ({new_c:.4g})")
    return new_a, new_b, new_c


# ─────────────────────────────────────────────────────────────────────────────
# BAGIAN 7: PERTIDAKSAMAAN KUADRAT / Quadratic Inequalities
# ─────────────────────────────────────────────────────────────────────────────

def solve_quadratic_inequality(a, b, c, inequality):
    """
    Selesaikan pertidaksamaan kuadrat ax² + bx + c {>, <, >=, <=} 0
    Solve quadratic inequality ax² + bx + c {>, <, >=, <=} 0
    
    Args:
        inequality: '>', '<', '>=', '<='
    """
    print(f"\n--- PERTIDAKSAMAAN KUADRAT / QUADRATIC INEQUALITY ---")
    print(f"Selesaikan: {a}x² + ({b})x + ({c}) {inequality} 0")
    
    D = discriminant(a, b, c)
    print(f"\nLangkah 1: Temukan akar-akar (jika ada)")
    print(f"D = {D}")
    
    include_endpoints = '>=' in inequality or '<=' in inequality
    bracket_type = "[]" if include_endpoints else "()"
    
    if D > 0:
        sqrt_D = math.sqrt(D)
        x1 = (-b - sqrt_D) / (2 * a)  # Akar kecil
        x2 = (-b + sqrt_D) / (2 * a)  # Akar besar
        if a < 0:
            x1, x2 = x2, x1  # Pastikan x1 < x2
        
        print(f"Akar: x₁ = {x1:.6g}, x₂ = {x2:.6g}")
        print(f"Garis bilangan: ...(−∞)...{x1:.4g}...{x2:.4g}...(+∞)...")
        
        # Tentukan solusi berdasarkan a dan pertidaksamaan
        if a > 0:
            if '>' in inequality:
                print(f"\na > 0, parabola terbuka ke atas")
                if include_endpoints:
                    print(f"Solusi: x ≤ {x1:.6g} ATAU x ≥ {x2:.6g}")
                    print(f"Notasi: (-∞, {x1:.6g}] ∪ [{x2:.6g}, +∞)")
                else:
                    print(f"Solusi: x < {x1:.6g} ATAU x > {x2:.6g}")
                    print(f"Notasi: (-∞, {x1:.6g}) ∪ ({x2:.6g}, +∞)")
            else:  # '<'
                print(f"\na > 0, parabola terbuka ke atas")
                if include_endpoints:
                    print(f"Solusi: {x1:.6g} ≤ x ≤ {x2:.6g}")
                    print(f"Notasi: [{x1:.6g}, {x2:.6g}]")
                else:
                    print(f"Solusi: {x1:.6g} < x < {x2:.6g}")
                    print(f"Notasi: ({x1:.6g}, {x2:.6g})")
        else:  # a < 0
            if '>' in inequality:
                print(f"\na < 0, parabola terbuka ke bawah")
                if include_endpoints:
                    print(f"Solusi: {x1:.6g} ≤ x ≤ {x2:.6g}")
                else:
                    print(f"Solusi: {x1:.6g} < x < {x2:.6g}")
            else:  # '<'
                print(f"\na < 0, parabola terbuka ke bawah")
                if include_endpoints:
                    print(f"Solusi: x ≤ {x1:.6g} ATAU x ≥ {x2:.6g}")
                else:
                    print(f"Solusi: x < {x1:.6g} ATAU x > {x2:.6g}")
    
    elif D == 0:
        x_double = -b / (2 * a)
        print(f"Akar kembar: x = {x_double:.6g}")
        if a > 0:
            if '>' in inequality:
                print(f"Solusi: semua x kecuali x = {x_double:.6g}")
                print(f"Notasi: (-∞, {x_double:.6g}) ∪ ({x_double:.6g}, +∞)")
            else:
                print(f"Solusi: hanya x = {x_double:.6g}")
        else:  # a < 0
            if '>' in inequality:
                print(f"Solusi: Tidak ada solusi (parabola terbuka ke bawah, max = 0)")
            else:
                print(f"Solusi: Semua bilangan real (nilai selalu ≤ 0)")
    
    else:  # D < 0
        print(f"D < 0: tidak ada akar real")
        test_val = a * 0**2 + b * 0 + c  # Test di x=0
        if a > 0:  # Fungsi selalu positif
            print(f"a > 0, D < 0: ekspresi selalu positif")
            if '>' in inequality:
                print(f"Solusi: Semua bilangan real ℝ = (-∞, +∞)")
            else:
                print(f"Solusi: Tidak ada solusi ∅")
        else:  # a < 0: Fungsi selalu negatif
            print(f"a < 0, D < 0: ekspresi selalu negatif")
            if '<' in inequality:
                print(f"Solusi: Semua bilangan real ℝ = (-∞, +∞)")
            else:
                print(f"Solusi: Tidak ada solusi ∅")


# ─────────────────────────────────────────────────────────────────────────────
# BAGIAN 8: SOAL CERITA / Word Problems
# ─────────────────────────────────────────────────────────────────────────────

def projectile_motion_example():
    """
    Soal cerita gerak proyektil.
    Word problem: Projectile motion.
    
    Sebuah bola dilempar ke atas dengan kecepatan awal 20 m/s dari ketinggian 5 m.
    h(t) = -5t² + 20t + 5  (g ≈ 10 m/s²)
    """
    print(f"\n--- SOAL CERITA: GERAK PROYEKTIL ---")
    print("Sebuah bola dilempar ke atas dengan v₀ = 20 m/s dari h₀ = 5 m")
    print("Model: h(t) = -5t² + 20t + 5")
    print()
    
    a, b, c = -5, 20, 5
    
    # a. Kapan bola mencapai ketinggian maksimum?
    t_max = -b / (2 * a)
    h_max = a * t_max**2 + b * t_max + c
    print(f"a) Ketinggian maksimum:")
    print(f"   t = -b/(2a) = -{b}/(2×{a}) = {t_max} detik")
    print(f"   h_max = {a}({t_max})² + {b}({t_max}) + {c} = {h_max} meter")
    
    # b. Kapan bola menyentuh tanah?
    print(f"\nb) Kapan bola menyentuh tanah (h=0)?")
    roots = solve_quadratic_formula(a, b, c, verbose=False)
    t1, t2 = roots
    t_land = max(t1, t2)  # Ambil waktu positif
    print(f"   -5t² + 20t + 5 = 0")
    print(f"   D = {discriminant(a,b,c)}")
    print(f"   t = {t1:.4f} atau t = {t2:.4f}")
    print(f"   Bola menyentuh tanah pada t ≈ {t_land:.4f} detik")
    
    # c. Kapan ketinggian bola > 15 meter?
    print(f"\nc) Kapan h(t) > 15 meter?")
    print(f"   -5t² + 20t + 5 > 15")
    print(f"   -5t² + 20t - 10 > 0")
    print(f"   t² - 4t + 2 < 0  (bagi dengan -5, balik tanda)")
    a2, b2, c2 = 1, -4, 2
    D2 = discriminant(a2, b2, c2)
    t_a = (-b2 - math.sqrt(D2)) / (2*a2)
    t_b = (-b2 + math.sqrt(D2)) / (2*a2)
    print(f"   Akar: t = {t_a:.4f} dan t = {t_b:.4f}")
    print(f"   Solusi: {t_a:.4f} < t < {t_b:.4f}")


def area_problem_example():
    """
    Soal cerita tentang luas / Word problem about area.
    
    Panjang persegi panjang 3 cm lebih dari lebarnya. Luas = 54 cm².
    Tentukan dimensinya!
    """
    print(f"\n--- SOAL CERITA: LUAS PERSEGI PANJANG ---")
    print("Panjang = lebar + 3, Luas = 54 cm²")
    print("Misalkan lebar = x, maka panjang = x + 3")
    print("Persamaan: x(x + 3) = 54")
    print("           x² + 3x - 54 = 0")
    print()
    
    roots = solve_quadratic_formula(1, 3, -54, verbose=False)
    x1, x2 = roots
    print(f"Akar: x₁ = {x1:.4g}, x₂ = {x2:.4g}")
    
    # Hanya ambil nilai positif
    width = x1 if x1 > 0 else x2
    length = width + 3
    print(f"\nKarena lebar harus positif: x = {width:.4g}")
    print(f"Lebar = {width:.4g} cm")
    print(f"Panjang = {length:.4g} cm")
    print(f"Verifikasi: {width:.4g} × {length:.4g} = {width * length:.4g} cm² ✓")


# ─────────────────────────────────────────────────────────────────────────────
# BAGIAN 9: MEMBENTUK PERSAMAAN DARI AKAR / Forming Equation from Roots
# ─────────────────────────────────────────────────────────────────────────────

def form_equation_from_roots(r1, r2, a=1):
    """
    Bentuk persamaan kuadrat dari akar-akar yang diketahui.
    Form quadratic equation given its roots.
    
    Persamaan: a(x - r1)(x - r2) = 0
    Expanded: a[x² - (r1+r2)x + r1*r2] = 0
    """
    print(f"\n--- MEMBENTUK PERSAMAAN DARI AKAR ---")
    print(f"Diketahui akar: x₁ = {r1}, x₂ = {r2}")
    
    S = r1 + r2  # Sum of roots
    P = r1 * r2  # Product of roots
    
    print(f"\nJumlah akar (S) = x₁ + x₂ = {r1} + {r2} = {S}")
    print(f"Hasil kali (P) = x₁ × x₂ = {r1} × {r2} = {P}")
    print(f"\nPersamaan: x² - Sx + P = 0")
    print(f"           x² - ({S})x + ({P}) = 0")
    
    new_b = -a * S
    new_c = a * P
    
    if a != 1:
        print(f"Dengan a = {a}: {a}x² + ({new_b})x + ({new_c}) = 0")
    
    # Verifikasi
    print(f"\nVerifikasi substitusi x₁ = {r1}:")
    val1 = a * r1**2 + new_b * r1 + new_c
    print(f"  {a}({r1})² + ({new_b})({r1}) + ({new_c}) = {val1:.8g}")
    
    return a, new_b, new_c


# ─────────────────────────────────────────────────────────────────────────────
# PROGRAM UTAMA / MAIN PROGRAM
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 60)
    print("  TOPIK 1.6: PERSAMAAN KUADRAT — EXAMPLES.PY")
    print("=" * 60)
    
    # ─── Contoh 1: Diskriminan ───
    print("\n" + "█"*55)
    print("  CONTOH 1: ANALISIS DISKRIMINAN")
    print("█"*55)
    analyze_discriminant(1, -5, 6)    # D > 0, rasional
    analyze_discriminant(1, -2, 1)    # D = 0
    analyze_discriminant(1, 1, 1)     # D < 0, kompleks
    analyze_discriminant(1, -2, -1)   # D > 0, irasional
    
    # ─── Contoh 2: Faktorisasi ───
    print("\n" + "█"*55)
    print("  CONTOH 2: METODE FAKTORISASI")
    print("█"*55)
    solve_by_factoring_integer(1, -5, 6)
    solve_by_factoring_integer(2, -3, -2)
    
    # ─── Contoh 3: Completing the Square ───
    print("\n" + "█"*55)
    print("  CONTOH 3: MELENGKAPKAN KUADRAT")
    print("█"*55)
    solve_by_completing_square(1, -4, 3)
    solve_by_completing_square(2, 4, 5)  # D < 0
    
    # ─── Contoh 4: Rumus Kuadrat ───
    print("\n" + "█"*55)
    print("  CONTOH 4: RUMUS KUADRAT")
    print("█"*55)
    solve_quadratic_formula(3, -7, 2)
    solve_quadratic_formula(1, -2, 2)   # Kompleks
    solve_quadratic_formula(4, -12, 9)  # Akar kembar
    
    # ─── Contoh 5: Vieta's Formulas ───
    print("\n" + "█"*55)
    print("  CONTOH 5: RUMUS VIETA")
    print("█"*55)
    vietas_formulas(2, -7, 3)
    vietas_formulas(1, 0, -4)
    
    # ─── Contoh 6: Konversi Bentuk ───
    print("\n" + "█"*55)
    print("  CONTOH 6: KONVERSI ANTAR BENTUK")
    print("█"*55)
    standard_to_vertex_form(2, -8, 3)
    vertex_to_standard_form(1, 3, -4)
    
    # ─── Contoh 7: Pertidaksamaan Kuadrat ───
    print("\n" + "█"*55)
    print("  CONTOH 7: PERTIDAKSAMAAN KUADRAT")
    print("█"*55)
    solve_quadratic_inequality(1, -5, 6, ">")
    solve_quadratic_inequality(1, -5, 6, "<")
    solve_quadratic_inequality(-1, 4, -3, ">=")
    
    # ─── Contoh 8: Soal Cerita ───
    print("\n" + "█"*55)
    print("  CONTOH 8: SOAL CERITA")
    print("█"*55)
    projectile_motion_example()
    area_problem_example()
    
    # ─── Contoh 9: Membentuk Persamaan dari Akar ───
    print("\n" + "█"*55)
    print("  CONTOH 9: MEMBENTUK PERSAMAAN DARI AKAR")
    print("█"*55)
    form_equation_from_roots(3, -5)
    form_equation_from_roots(2 + 3**0.5, 2 - 3**0.5)
    form_equation_from_roots(2, -1, a=3)
    
    print("\n" + "="*60)
    print("  Selesai! / Done!")
    print("  Jalankan visualizations.py untuk grafik")
    print("="*60)
