"""
Module  : Algebraic Expressions (Ekspresi Aljabar)
Phase   : 1 - Algebra  |  Topic: 1.3
Project : MathCode Learning
Jalankan: python3 examples.py
"""

try:
    import sympy as sp
    HAS_SYMPY = True
except ImportError:
    HAS_SYMPY = False
    print("sympy tidak ada. Install: pip install sympy")

print("=" * 60)
print("EKSPRESI ALJABAR — CONTOH IMPLEMENTASI")
print("=" * 60)

# ─── 1. Evaluasi ekspresi ─────────────────────────────────────
print("\n[1] Evaluasi Ekspresi — Substitusi Nilai")

def evaluate(expr_fn, val, var_name="x"):
    """Evaluasi fungsi ekspresi dengan substitusi nilai."""
    result = expr_fn(val)
    print(f"  f({var_name}={val}) = {result}")
    return result

# f(x) = 3x^2 - 5x + 2
def f(x):
    return 3*x**2 - 5*x + 2

print("f(x) = 3x^2 - 5x + 2")
for val in [-2, 0, 1, 3, 5]:
    evaluate(f, val)

# ─── 2. Menyederhanakan: suku sejenis ─────────────────────────
print("\n[2] Menyederhanakan Suku Sejenis (Like Terms)")
print("Contoh: 3x^2 + 5x - 2x^2 + 7x - 4")
print("  Kelompok x^2: 3x^2 - 2x^2 = 1x^2")
print("  Kelompok x  : 5x + 7x     = 12x")
print("  Konstanta   : -4")
print("  Hasil: x^2 + 12x - 4")

def combine_like_terms(terms):
    """
    terms: dict {degree: coefficient}
    Contoh: {2:3, 1:5, 0:-4} = 3x^2 + 5x - 4
    """
    from collections import defaultdict
    combined = defaultdict(int)
    for deg, coef in terms:
        combined[deg] += coef
    return dict(combined)

expr1 = [(2, 3), (1, 5), (2, -2), (1, 7), (0, -4)]
result = combine_like_terms(expr1)
print(f"\n  Terms: {expr1}")
print(f"  Simplified: {result}")

def poly_to_str(poly_dict):
    """Konversi dict koefisien ke string."""
    terms = []
    for deg in sorted(poly_dict.keys(), reverse=True):
        coef = poly_dict[deg]
        if coef == 0:
            continue
        if deg == 0:
            terms.append(f"{coef}")
        elif deg == 1:
            terms.append(f"{coef}x" if coef != 1 else "x")
        else:
            terms.append(f"{coef}x^{deg}" if coef != 1 else f"x^{deg}")
    return " + ".join(terms).replace("+ -", "- ")

print(f"  Ekspresi: {poly_to_str(result)}")

# ─── 3. Perkalian ekspresi — FOIL ────────────────────────────
print("\n[3] Perkalian Ekspresi — Metode FOIL")
print("(a + b)(c + d) = ac + ad + bc + bd")
print("(x + 3)(x - 2):")
print("  F (First)  : x * x  = x^2")
print("  O (Outer)  : x * -2 = -2x")
print("  I (Inner)  : 3 * x  =  3x")
print("  L (Last)   : 3 * -2 =  -6")
print("  Hasil: x^2 + x - 6")

def foil(a, b, c, d):
    """Kalikan (a*x + b)(c*x + d) → koefisien [x^2, x, konst]"""
    return [a*c, a*d + b*c, b*d]

coefs = foil(1, 3, 1, -2)
print(f"\n  foil(1,3,1,-2) = koefisien: {coefs}")
print(f"  = {coefs[0]}x^2 + {coefs[1]}x + {coefs[2]}")

# ─── 4. Produk Khusus (Special Products) ─────────────────────
print("\n[4] Produk Khusus (Special Products)")

def special_products(a, b):
    """Hitung semua produk khusus untuk (a+b) dan (a-b)."""
    print(f"  a = {a}, b = {b}")
    print(f"  (a+b)^2     = a^2+2ab+b^2 = {(a+b)**2} (verify: {a**2+2*a*b+b**2})")
    print(f"  (a-b)^2     = a^2-2ab+b^2 = {(a-b)**2} (verify: {a**2-2*a*b+b**2})")
    print(f"  (a+b)(a-b)  = a^2-b^2     = {(a+b)*(a-b)} (verify: {a**2-b**2})")
    print(f"  (a+b)^3     = a^3+3a^2b+3ab^2+b^3 = {(a+b)**3}")
    print(f"  (a-b)^3     = a^3-3a^2b+3ab^2-b^3 = {(a-b)**3}")

special_products(3, 4)

# ─── 5. Ekspresi Rasional — Domain ───────────────────────────
print("\n[5] Ekspresi Rasional — Domain dan Simplifikasi")
print("f(x) = (x^2 - 4)/(x - 2)")
print("  Domain: x != 2 (pembagi tidak boleh nol)")
print("  Faktorisasi: (x+2)(x-2)/(x-2) = x+2  (untuk x!=2)")

def rational_simplified(x):
    if abs(x - 2) < 1e-12:
        return float("nan")  # undefined
    return (x**2 - 4) / (x - 2)

def simplified(x):
    return x + 2

print("\n  x     f(x)=rational  simplified(x+2)")
for x in [-1, 0, 1, 1.99, 2.01, 3, 5]:
    print(f"  {x:5.2f}   {rational_simplified(x):10.4f}    {simplified(x):10.4f}")

# ─── 6. Sympy untuk ekspresi simbolik ────────────────────────
if HAS_SYMPY:
    print("\n[6] Ekspresi Simbolik dengan SymPy")
    x, y = sp.symbols("x y")
    
    expr = 3*x**2 - 5*x + 2
    print(f"  expr     = {expr}")
    print(f"  expand   = {sp.expand(expr)}")
    print(f"  factor   = {sp.factor(expr)}")
    print(f"  subs x=3 = {expr.subs(x, 3)}")
    
    expr2 = (x**2 - y**2) / (x - y)
    print(f"\n  (x^2-y^2)/(x-y) simplified = {sp.simplify(expr2)}")
    
    expr3 = sp.expand((x + 3)**3)
    print(f"  (x+3)^3 expanded = {expr3}")

print("\n[Selesai] Lanjut ke exercises.py")
