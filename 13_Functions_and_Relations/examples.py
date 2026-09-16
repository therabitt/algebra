"""
=============================================================================
TOPIK 1.8: FUNGSI DAN RELASI (Functions and Relations)
File: examples.py
=============================================================================
Implementasi konsep fungsi dari awal menggunakan Python.
Menggunakan sympy untuk komputasi simbolik (invers, domain analitis).

Concepts implemented from scratch using Python.
Uses sympy for symbolic computations.
=============================================================================
"""

import math
import sympy as sp


# ─────────────────────────────────────────────────────────────────────────────
# BAGIAN 1: MENDEFINISIKAN FUNGSI / Defining Functions
# ─────────────────────────────────────────────────────────────────────────────

def demo_function_definitions():
    """
    Berbagai cara mendefinisikan fungsi di Python.
    Various ways to define mathematical functions in Python.
    """
    print("\n--- MENDEFINISIKAN FUNGSI / DEFINING FUNCTIONS ---")
    
    # Cara 1: Fungsi biasa (regular function)
    def f(x):
        """f(x) = x² + 2x - 3"""
        return x**2 + 2*x - 3
    
    # Cara 2: Lambda (fungsi anonim / anonymous function)
    g = lambda x: 2*x + 1
    
    # Cara 3: Fungsi matematika dengan penanganan domain
    def h(x):
        """h(x) = √(x - 1), hanya terdefinisi untuk x ≥ 1"""
        if x < 1:
            raise ValueError(f"h({x}) tidak terdefinisi: x harus ≥ 1")
        return math.sqrt(x - 1)
    
    # Cara 4: Fungsi rasional
    def r(x):
        """r(x) = (x+2)/(x-3), tidak terdefinisi di x=3"""
        if x == 3:
            raise ValueError(f"r(3) tidak terdefinisi: pembagi nol")
        return (x + 2) / (x - 3)
    
    # Evaluasi
    print(f"\nf(x) = x² + 2x - 3:")
    for x in [-2, 0, 1, 3, 5]:
        print(f"  f({x}) = {f(x)}")
    
    print(f"\ng(x) = 2x + 1:")
    for x in [-1, 0, 2, 4]:
        print(f"  g({x}) = {g(x)}")
    
    print(f"\nh(x) = √(x-1)  [domain: x ≥ 1]:")
    for x in [1, 2, 5, 10, 26]:
        print(f"  h({x}) = {h(x):.6g}")
    
    print(f"\nr(x) = (x+2)/(x-3)  [domain: x ≠ 3]:")
    for x in [0, 2, 4, 5, -1]:
        print(f"  r({x}) = {r(x):.6g}")
    
    return f, g, h, r


# ─────────────────────────────────────────────────────────────────────────────
# BAGIAN 2: DOMAIN DAN RANGE / Domain and Range
# ─────────────────────────────────────────────────────────────────────────────

def analyze_domain_range():
    """
    Analisis domain dan range menggunakan sympy.
    Analyze domain and range using sympy symbolic computation.
    """
    print("\n--- DOMAIN DAN RANGE ---")
    
    x = sp.Symbol('x', real=True)
    
    # Fungsi-fungsi untuk dianalisis
    functions = [
        (x**2 + 2*x - 3,        "f(x) = x² + 2x - 3"),
        (sp.sqrt(x - 1),         "g(x) = √(x - 1)"),
        (1 / (x - 3),            "h(x) = 1/(x - 3)"),
        (sp.sqrt(4 - x**2),      "k(x) = √(4 - x²)"),
        (sp.log(x),              "p(x) = ln(x)"),
        ((x + 2)/(x**2 - x - 6),"q(x) = (x+2)/(x²-x-6)"),
    ]
    
    for expr, name in functions:
        print(f"\n{name}")
        try:
            domain = sp.calculus.util.continuous_domain(expr, x, sp.S.Reals)
            print(f"  Domain: {domain}")
        except Exception as e:
            print(f"  Domain: [tidak dapat dihitung otomatis — periksa secara manual]")
        
        try:
            # Range menggunakan image
            range_ = sp.calculus.util.function_range(expr, x, sp.S.Reals)
            print(f"  Range:  {range_}")
        except Exception as e:
            print(f"  Range: [perlu analisis manual]")


# ─────────────────────────────────────────────────────────────────────────────
# BAGIAN 3: KOMPOSISI FUNGSI / Function Composition
# ─────────────────────────────────────────────────────────────────────────────

def demo_composition():
    """
    Demonstrasi komposisi fungsi (f∘g)(x) = f(g(x)).
    Demonstrate function composition.
    """
    print("\n--- KOMPOSISI FUNGSI / FUNCTION COMPOSITION ---")
    
    # Definisi fungsi
    def f(x): return x**2 + 1       # f(x) = x² + 1
    def g(x): return 2*x - 3        # g(x) = 2x - 3
    def h(x): return math.sqrt(abs(x))  # h(x) = √|x|
    
    print("f(x) = x² + 1")
    print("g(x) = 2x - 3")
    print("h(x) = √|x|")
    
    # (f∘g)(x) = f(g(x))
    def fog(x): return f(g(x))  # f(2x-3) = (2x-3)² + 1
    
    # (g∘f)(x) = g(f(x))
    def gof(x): return g(f(x))  # g(x²+1) = 2(x²+1) - 3 = 2x² - 1
    
    # (f∘g∘h)(x) = f(g(h(x)))
    def fogoh(x): return f(g(h(x)))
    
    print(f"\n(f∘g)(x) = f(g(x)) = f(2x-3) = (2x-3)² + 1:")
    for x in [-2, 0, 1, 3]:
        print(f"  (f∘g)({x}) = f(g({x})) = f({g(x)}) = {fog(x)}")
    
    print(f"\n(g∘f)(x) = g(f(x)) = g(x²+1) = 2(x²+1) - 3 = 2x² - 1:")
    for x in [-2, 0, 1, 3]:
        print(f"  (g∘f)({x}) = g(f({x})) = g({f(x)}) = {gof(x)}")
    
    print(f"\nCatatan: f∘g ≠ g∘f! (komposisi tidak komutatif)")
    print(f"  (f∘g)(2) = {fog(2)}")
    print(f"  (g∘f)(2) = {gof(2)}")
    
    # Verifikasi dengan sympy
    print(f"\n--- Verifikasi simbolik dengan Sympy ---")
    x = sp.Symbol('x')
    f_expr = x**2 + 1
    g_expr = 2*x - 3
    
    fog_expr = f_expr.subs(x, g_expr)
    gof_expr = g_expr.subs(x, f_expr)
    
    print(f"  (f∘g)(x) = f(g(x)) = f(2x-3) = {sp.expand(fog_expr)}")
    print(f"  (g∘f)(x) = g(f(x)) = g(x²+1) = {sp.expand(gof_expr)}")


# ─────────────────────────────────────────────────────────────────────────────
# BAGIAN 4: FUNGSI INVERS / Inverse Functions
# ─────────────────────────────────────────────────────────────────────────────

def find_inverse_algebraically(expr_str, var='x'):
    """
    Temukan invers fungsi secara aljabar menggunakan sympy.
    Find function inverse algebraically using sympy.
    """
    print(f"\n--- MENCARI INVERS FUNGSI ---")
    
    x, y = sp.symbols('x y')
    
    expr = sp.sympify(expr_str)
    print(f"f(x) = {expr}")
    print(f"\nLangkah 1: Tulis y = f(x)")
    print(f"  y = {expr}")
    
    print(f"\nLangkah 2: Tukar x dan y")
    swapped = expr.subs(x, y)
    print(f"  x = {swapped}")
    
    print(f"\nLangkah 3: Selesaikan untuk y")
    try:
        solutions = sp.solve(sp.Eq(x, swapped), y)
        if solutions:
            for sol in solutions:
                print(f"  y = {sol}")
                print(f"  f⁻¹(x) = {sol}")
            
            inv = solutions[0]
            print(f"\nLangkah 4: Verifikasi f(f⁻¹(x)) = x")
            composed = expr.subs(x, inv)
            simplified = sp.simplify(composed)
            print(f"  f(f⁻¹(x)) = {composed} = {simplified}")
            print(f"  = x? {'✓ YA' if simplified == x else str(simplified)}")
            
            print(f"\nLangkah 5: Verifikasi f⁻¹(f(x)) = x")
            composed2 = inv.subs(x, expr)
            simplified2 = sp.simplify(composed2)
            print(f"  f⁻¹(f(x)) = {simplified2}")
            print(f"  = x? {'✓ YA' if simplified2 == x else str(simplified2)}")
            
            return inv
    except Exception as e:
        print(f"  Tidak dapat diselesaikan secara simbolik: {e}")
        return None


def demo_inverse_functions():
    """Demonstrasi mencari invers beberapa fungsi."""
    print("\n" + "="*55)
    print("  FUNGSI INVERS / INVERSE FUNCTIONS")
    print("="*55)
    
    test_functions = [
        "3*x + 2",
        "(x + 1)/(x - 2)",
        "x**3 - 1",
        "x**2 + 1",  # Bukan bijektif! (terbatas hanya x >= 0)
    ]
    
    for f_str in test_functions:
        print(f"\n{'─'*50}")
        find_inverse_algebraically(f_str)


# ─────────────────────────────────────────────────────────────────────────────
# BAGIAN 5: FUNGSI GENAP DAN GANJIL / Even and Odd Functions
# ─────────────────────────────────────────────────────────────────────────────

def test_even_odd(func, name, test_values=None):
    """
    Uji apakah fungsi genap, ganjil, atau tidak keduanya.
    Test if a function is even, odd, or neither.
    
    Genap (Even): f(-x) = f(x) untuk semua x
    Ganjil (Odd): f(-x) = -f(x) untuk semua x
    """
    if test_values is None:
        test_values = [-3, -2, -1, 1, 2, 3]
    
    print(f"\n  {name}")
    
    is_even = True
    is_odd = True
    
    for x in test_values:
        fx = func(x)
        f_neg_x = func(-x)
        
        # Cek genap: f(-x) == f(x)
        if abs(f_neg_x - fx) > 1e-9:
            is_even = False
        
        # Cek ganjil: f(-x) == -f(x)
        if abs(f_neg_x + fx) > 1e-9:
            is_odd = False
        
        print(f"    f({x:3}) = {fx:8.4g},  f({-x:3}) = {f_neg_x:8.4g},  "
              f"-f({x:3}) = {-fx:8.4g}")
    
    if is_even and is_odd:
        result = "GENAP DAN GANJIL (hanya f(x) = 0)"
    elif is_even:
        result = "✓ GENAP (Even) — simetri terhadap sumbu-y"
    elif is_odd:
        result = "✓ GANJIL (Odd) — simetri terhadap titik asal"
    else:
        result = "✗ TIDAK GENAP MAUPUN GANJIL (Neither)"
    
    print(f"    → {result}")
    return is_even, is_odd


def demo_even_odd():
    """Demonstrasi pengujian fungsi genap dan ganjil."""
    print("\n--- FUNGSI GENAP DAN GANJIL / EVEN AND ODD ---")
    print("Genap: f(-x) = f(x) | Ganjil: f(-x) = -f(x)")
    
    functions = [
        (lambda x: x**2,          "f(x) = x²"),
        (lambda x: x**3,          "f(x) = x³"),
        (lambda x: x**2 + x,      "f(x) = x² + x"),
        (lambda x: abs(x),        "f(x) = |x|"),
        (lambda x: x**4 - x**2,   "f(x) = x⁴ - x²"),
        (lambda x: x**3 - x,      "f(x) = x³ - x"),
        (lambda x: x + 1,         "f(x) = x + 1"),
        (lambda x: 0.0,           "f(x) = 0"),
    ]
    
    for func, name in functions:
        test_even_odd(func, name)


# ─────────────────────────────────────────────────────────────────────────────
# BAGIAN 6: FUNGSI PIECEWISE / Piecewise Functions
# ─────────────────────────────────────────────────────────────────────────────

def piecewise_absolute_value(x):
    """
    Implementasi nilai mutlak dari awal (tanpa abs bawaan).
    Implement absolute value from scratch.
    
    |x| = { x   jika x >= 0
           { -x  jika x < 0
    """
    if x >= 0:
        return x
    else:
        return -x


def piecewise_example_1(x):
    """
    Fungsi piecewise contoh 1:
    f(x) = { x² + 1    jika x < 0
           { 2x         jika 0 <= x < 3
           { 7           jika x >= 3
    """
    if x < 0:
        return x**2 + 1
    elif x < 3:
        return 2 * x
    else:
        return 7


def piecewise_example_2(x):
    """
    Fungsi piecewise contoh 2 (SGN function — fungsi tanda):
    sgn(x) = { -1  jika x < 0
             {  0  jika x = 0
             {  1  jika x > 0
    """
    if x < 0:
        return -1
    elif x == 0:
        return 0
    else:
        return 1


def floor_function(x):
    """
    Fungsi floor/lantai ⌊x⌋ — bilangan bulat terbesar ≤ x
    Floor function — largest integer ≤ x
    """
    return int(math.floor(x))


def ceiling_function(x):
    """
    Fungsi ceiling/langit-langit ⌈x⌉ — bilangan bulat terkecil ≥ x
    Ceiling function — smallest integer ≥ x
    """
    return int(math.ceil(x))


def demo_piecewise():
    """Demonstrasi fungsi piecewise."""
    print("\n--- FUNGSI PIECEWISE ---")
    
    print("\nFungsi Nilai Mutlak |x|:")
    print("  x:    ", end="")
    vals = [-3, -2, -1, -0.5, 0, 0.5, 1, 2, 3]
    for v in vals:
        print(f"{v:6.1f}", end="")
    print()
    print("  |x|:  ", end="")
    for v in vals:
        print(f"{piecewise_absolute_value(v):6.1f}", end="")
    print()
    
    print("\nFungsi Piecewise f(x) = {x²+1 jika x<0; 2x jika 0≤x<3; 7 jika x≥3}:")
    test_vals = [-2, -1, 0, 1, 2, 3, 4, 5]
    for x in test_vals:
        print(f"  f({x:2}) = {piecewise_example_1(x)}")
    
    print("\nFungsi Tanda SGN(x):")
    for x in [-3, -1, -0.1, 0, 0.1, 1, 3]:
        print(f"  sgn({x:4.1f}) = {piecewise_example_2(x):2}")
    
    print("\nFungsi Floor ⌊x⌋ dan Ceiling ⌈x⌉:")
    vals = [-2.7, -1.1, 0, 0.5, 1.0, 2.3, 3.9]
    print(f"  {'x':>8}  {'⌊x⌋':>6}  {'⌈x⌉':>6}")
    for v in vals:
        print(f"  {v:8.1f}  {floor_function(v):6}  {ceiling_function(v):6}")


# ─────────────────────────────────────────────────────────────────────────────
# BAGIAN 7: TRANSFORMASI FUNGSI / Function Transformations
# ─────────────────────────────────────────────────────────────────────────────

def demo_transformations():
    """
    Demonstrasi transformasi fungsi.
    Demonstrate function transformations.
    """
    print("\n--- TRANSFORMASI FUNGSI / FUNCTION TRANSFORMATIONS ---")
    
    # Fungsi dasar
    def f(x): return x**2  # Parabola dasar
    
    print("Fungsi dasar: f(x) = x²")
    print("\nTransformasi dan evaluasi di x = 2:")
    x = 2
    
    transformations = [
        (lambda x: f(x),           "f(x) = x²                  (asli)"),
        (lambda x: f(x) + 3,       "f(x) + 3 = x² + 3          (geser atas 3)"),
        (lambda x: f(x) - 2,       "f(x) - 2 = x² - 2          (geser bawah 2)"),
        (lambda x: f(x - 1),       "f(x-1) = (x-1)²            (geser kanan 1)"),
        (lambda x: f(x + 2),       "f(x+2) = (x+2)²            (geser kiri 2)"),
        (lambda x: 2 * f(x),       "2f(x) = 2x²                (regangkan vertikal ×2)"),
        (lambda x: 0.5 * f(x),     "0.5f(x) = 0.5x²            (kompresi vertikal ×0.5)"),
        (lambda x: -f(x),          "-f(x) = -x²                (refleksi terhadap x-axis)"),
        (lambda x: f(-x),          "f(-x) = (-x)² = x²         (refleksi terhadap y-axis)"),
        (lambda x: f(2*x),         "f(2x) = (2x)² = 4x²        (kompresi horizontal)"),
        (lambda x: f(x/2),         "f(x/2) = (x/2)²            (regangkan horizontal)"),
        (lambda x: -f(x - 1) + 3, "-f(x-1)+3 = -(x-1)²+3     (gabungan transformasi)"),
    ]
    
    print(f"\n{'Transformasi':<45} {'Nilai di x=2':>15}")
    print("─" * 62)
    for transform, desc in transformations:
        try:
            val = transform(x)
            print(f"  {desc:<45} {val:>15.4g}")
        except:
            print(f"  {desc:<45} {'ERROR':>15}")


# ─────────────────────────────────────────────────────────────────────────────
# BAGIAN 8: ANALISIS FUNGSI / Function Analysis
# ─────────────────────────────────────────────────────────────────────────────

def analyze_function(expr_str):
    """
    Analisis lengkap sebuah fungsi menggunakan sympy.
    Complete function analysis using sympy.
    
    Mencari: x-intercepts, y-intercept, vertex (untuk kuadrat), monoton
    Finding: x-intercepts, y-intercept, vertex (for quadratics), monotone
    """
    print(f"\n--- ANALISIS FUNGSI / FUNCTION ANALYSIS ---")
    
    x = sp.Symbol('x', real=True)
    expr = sp.sympify(expr_str)
    f = sp.Function('f')
    
    print(f"f(x) = {expr}")
    
    # y-intercept: f(0)
    try:
        y_int = expr.subs(x, 0)
        print(f"\ny-intercept: f(0) = {y_int}")
    except:
        print(f"\ny-intercept: tidak terdefinisi di x=0")
    
    # x-intercepts (zeros/roots): f(x) = 0
    try:
        zeros = sp.solve(expr, x)
        print(f"\nx-intercept(s) [f(x) = 0]: x = {zeros}")
    except:
        print(f"\nx-intercept: tidak dapat dihitung")
    
    # Turunan pertama
    try:
        f_prime = sp.diff(expr, x)
        print(f"\nf'(x) = {sp.expand(f_prime)}")
        
        # Titik kritis
        critical = sp.solve(f_prime, x)
        print(f"Titik kritis (f'(x) = 0): x = {critical}")
        
        for cp in critical:
            cp_val = expr.subs(x, cp)
            f_pp = sp.diff(f_prime, x)
            f_pp_at_cp = f_pp.subs(x, cp)
            
            if f_pp_at_cp > 0:
                print(f"  x = {cp}: Minimum lokal, f({cp}) = {cp_val}")
            elif f_pp_at_cp < 0:
                print(f"  x = {cp}: Maksimum lokal, f({cp}) = {cp_val}")
            else:
                print(f"  x = {cp}: Titik belok (inflection), f({cp}) = {cp_val}")
    except Exception as e:
        print(f"\nTidak dapat menghitung turunan: {e}")
    
    # Monotonisitas
    try:
        incr = sp.calculus.util.monotonicity_helper(expr, x, sp.S.Reals, 'increasing')
        print(f"\nMonoton naik pada: {incr}")
        
        decr = sp.calculus.util.monotonicity_helper(expr, x, sp.S.Reals, 'decreasing')
        print(f"Monoton turun pada: {decr}")
    except:
        pass  # Tidak semua versi sympy punya fungsi ini


def demo_function_analysis():
    """Analisis beberapa fungsi."""
    print("\n" + "="*55)
    print("  ANALISIS FUNGSI / FUNCTION ANALYSIS")
    print("="*55)
    
    exprs = [
        "x**2 - 4*x + 3",
        "-x**2 + 6*x - 5",
        "x**3 - 3*x",
    ]
    
    for expr in exprs:
        analyze_function(expr)
        print()


# ─────────────────────────────────────────────────────────────────────────────
# BAGIAN 9: UJI FUNGSI / Function Tests
# ─────────────────────────────────────────────────────────────────────────────

def is_function_relation(pairs):
    """
    Uji apakah himpunan pasangan terurut merepresentasikan fungsi.
    Test if a set of ordered pairs represents a function.
    
    Syarat fungsi: setiap x dipetakan ke tepat satu y.
    Function condition: every x maps to exactly one y.
    """
    print(f"\n--- UJI APAKAH RELASI ADALAH FUNGSI ---")
    print(f"Pasangan terurut: {pairs}")
    
    # Kumpulkan semua domain values
    domain_dict = {}
    for x, y in pairs:
        if x in domain_dict:
            domain_dict[x].append(y)
        else:
            domain_dict[x] = [y]
    
    print(f"Pemetaan: {dict((k, v) for k, v in domain_dict.items())}")
    
    is_func = all(len(vals) == 1 for vals in domain_dict.values())
    
    if is_func:
        domain = set(domain_dict.keys())
        range_ = set(y for _, y in pairs)
        print(f"✓ Ini adalah FUNGSI")
        print(f"  Domain: {sorted(domain)}")
        print(f"  Range:  {sorted(range_)}")
    else:
        problematic = {k: v for k, v in domain_dict.items() if len(v) > 1}
        print(f"✗ Ini BUKAN fungsi")
        print(f"  Masalah: {problematic} (satu x memiliki lebih dari satu y)")
    
    return is_func


def vertical_line_test_discrete(pairs):
    """
    Uji garis vertikal untuk himpunan diskret.
    Vertical line test for discrete set.
    """
    return is_function_relation(pairs)  # Logika sama untuk kasus diskret


# ─────────────────────────────────────────────────────────────────────────────
# PROGRAM UTAMA / MAIN PROGRAM
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 60)
    print("  TOPIK 1.8: FUNGSI DAN RELASI — EXAMPLES.PY")
    print("=" * 60)
    
    # ─── Contoh 1: Mendefinisikan Fungsi ───
    print("\n" + "█"*55)
    print("  CONTOH 1: MENDEFINISIKAN FUNGSI")
    print("█"*55)
    demo_function_definitions()
    
    # ─── Contoh 2: Domain dan Range ───
    print("\n" + "█"*55)
    print("  CONTOH 2: DOMAIN DAN RANGE")
    print("█"*55)
    analyze_domain_range()
    
    # ─── Contoh 3: Komposisi Fungsi ───
    print("\n" + "█"*55)
    print("  CONTOH 3: KOMPOSISI FUNGSI")
    print("█"*55)
    demo_composition()
    
    # ─── Contoh 4: Fungsi Invers ───
    print("\n" + "█"*55)
    print("  CONTOH 4: FUNGSI INVERS")
    print("█"*55)
    demo_inverse_functions()
    
    # ─── Contoh 5: Fungsi Genap dan Ganjil ───
    print("\n" + "█"*55)
    print("  CONTOH 5: FUNGSI GENAP DAN GANJIL")
    print("█"*55)
    demo_even_odd()
    
    # ─── Contoh 6: Fungsi Piecewise ───
    print("\n" + "█"*55)
    print("  CONTOH 6: FUNGSI PIECEWISE")
    print("█"*55)
    demo_piecewise()
    
    # ─── Contoh 7: Transformasi Fungsi ───
    print("\n" + "█"*55)
    print("  CONTOH 7: TRANSFORMASI FUNGSI")
    print("█"*55)
    demo_transformations()
    
    # ─── Contoh 8: Analisis Fungsi ───
    print("\n" + "█"*55)
    print("  CONTOH 8: ANALISIS FUNGSI")
    print("█"*55)
    demo_function_analysis()
    
    # ─── Contoh 9: Uji Fungsi ───
    print("\n" + "█"*55)
    print("  CONTOH 9: UJI APAKAH RELASI ADALAH FUNGSI")
    print("█"*55)
    is_function_relation([(1,2), (2,3), (3,4)])           # Fungsi
    is_function_relation([(1,2), (2,3), (1,5)])           # Bukan fungsi
    is_function_relation([(1,2), (2,2), (3,2)])           # Fungsi (many-to-one)
    is_function_relation([(0,0), (1,1), (-1,1), (4,2)])  # Fungsi (seperti y=x²)
    
    print("\n" + "="*60)
    print("  Selesai! / Done!")
    print("="*60)
