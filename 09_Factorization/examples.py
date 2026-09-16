"""
Module  : Factorization (Faktorisasi)
Phase   : 1 - Algebra  |  Topic: 1.10
Jalankan: python3 examples.py
"""
import math

print("=" * 60)
print("FAKTORISASI — CONTOH IMPLEMENTASI")
print("=" * 60)

def gcd(a, b):
    a, b = abs(a), abs(b)
    while b: a, b = b, a % b
    return a

# ─── 1. GCF ───────────────────────────────────────────────────
print("\n[1] Faktor Persekutuan Terbesar (GCF)")
terms = [(6,2),(9,1),(3,3)]  # 6x^2 + 9x + 3x^3
coefs = [t[0] for t in terms]
g = coefs[0]
for c in coefs[1:]: g = gcd(g, c)
powers = [t[1] for t in terms]
min_power = min(powers)
print(f"  6x^2 + 9x + 3x^3: GCF koefisien = {g}, pangkat min = x^{min_power}")
print(f"  = {g}x^{min_power}({6//g}x^{2-min_power} + {9//g} + {3//g}x^{3-min_power})")

# ─── 2. Pola Khusus ──────────────────────────────────────────
print("\n[2] Pola Khusus (Special Patterns)")

def verify_pattern(lhs_fn, rhs_fn, test_range=range(-10,11)):
    errors = [abs(lhs_fn(x)-rhs_fn(x)) for x in test_range]
    return max(errors) < 1e-10

# a^2 - b^2 = (a+b)(a-b)
a, b = 5, 3
print(f"  a^2-b^2: {a}^2-{b}^2 = {a**2-b**2}")
print(f"  (a+b)(a-b): ({a+b})({a-b}) = {(a+b)*(a-b)}")

# (a+b)^2 = a^2+2ab+b^2
lhs = (a+b)**2
rhs = a**2+2*a*b+b**2
print(f"  (a+b)^2 = ({a+b})^2 = {lhs}  vs  a^2+2ab+b^2 = {rhs}")

# Kubus
a, b = 2, 3
print(f"  a^3+b^3 = {a**3+b**3}")
print(f"  (a+b)(a^2-ab+b^2) = ({a+b})({a**2-a*b+b**2}) = {(a+b)*(a**2-a*b+b**2)}")
print(f"  a^3-b^3 = {a**3-b**3}")
print(f"  (a-b)(a^2+ab+b^2) = ({a-b})({a**2+a*b+b**2}) = {(a-b)*(a**2+a*b+b**2)}")

# ─── 3. Trinomial AC Method ───────────────────────────────────
print("\n[3] Metode AC untuk ax^2 + bx + c")
def factor_trinomial(a, b, c):
    """
    Faktorkan ax^2 + bx + c menggunakan metode AC.
    Cari m,n: m*n = a*c, m+n = b.
    """
    ac = a * c
    for m in range(-abs(ac)-1, abs(ac)+2):
        if ac == 0: break
        if m == 0: continue
        if ac % m == 0:
            n = ac // m
            if m + n == b:
                # ax^2 + mx + nx + c = group
                # Untuk kasus umum gunakan formula:
                # faktor: (ax + m)(ax + n) / a = (ax+m)(x+n/a) kalau a|m atau a|n
                from math import gcd as _gcd
                g1 = _gcd(abs(a), abs(m)); g2 = _gcd(abs(a), abs(n))
                print(f"  {a}x^2+{b}x+{c}: m={m}, n={n}")
                print(f"  = {a//g1}x({g1}x+{m//g1}) + {n//g2}({g2}x+{c*g2//n if n!=0 else c})")
                # Sympy untuk verifikasi
                try:
                    import sympy as sp
                    x = sp.Symbol("x")
                    expr = a*x**2 + b*x + c
                    print(f"  SymPy: {sp.factor(expr)}")
                except ImportError:
                    pass
                return (m, n)
    return None

factor_trinomial(6, 7, 2)
factor_trinomial(2, -5, 3)
factor_trinomial(1, -5, 6)

# ─── 4. Verifikasi dengan Ekspansi ───────────────────────────
print("\n[4] Verifikasi dengan Ekspansi Kembali")
try:
    import sympy as sp
    x = sp.Symbol("x")
    expressions = [
        x**2 - 9,
        x**2 + 6*x + 9,
        x**3 - 8,
        6*x**2 + 7*x + 2,
        x**4 - 16,
    ]
    print(f"  {'Ekspresi':>25} | {'Faktor':>30}")
    for expr in expressions:
        factored = sp.factor(expr)
        print(f"  {str(expr):>25} | {str(factored):>30}")
except ImportError:
    print("  (sympy tidak tersedia)")

print("\n[Selesai]")
