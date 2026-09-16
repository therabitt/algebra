"""
Module  : Rational Expressions (Pecahan Aljabar)
Phase   : 1 - Algebra  |  Topic: 1.16
Jalankan: python3 examples.py
"""
try:
    import sympy as sp
    HAS_SYMPY = True
except ImportError:
    HAS_SYMPY = False

print("=" * 60)
print("PECAHAN ALJABAR — CONTOH IMPLEMENTASI")
print("=" * 60)

# ─── 1. Domain ─────────────────────────────────────────────────
print("\n[1] Domain Ekspresi Rasional")

def find_domain_exclusions(Q_coeffs):
    """
    Temukan nilai x yang harus dikecualikan dari domain
    (akar-akar Q(x) dimana Q bukan polinomial yang kita tahu).
    Gunakan sympy untuk akar umum.
    """
    if HAS_SYMPY:
        x = sp.Symbol('x')
        Q = sum(c * x**i for i, c in enumerate(Q_coeffs))
        roots = sp.solve(Q, x)
        return roots
    return []

# f(x) = (x+1)/(x^2-4) -> Q = x^2-4 = (x+2)(x-2)
Q = [(-4), 0, 1]   # -4 + 0x + 1x^2
exclusions = find_domain_exclusions(Q)
print(f"  f(x) = (x+1)/(x^2-4)")
if HAS_SYMPY:
    print(f"  Penyebut=0 saat x = {exclusions}")
    print(f"  Domain: semua real kecuali x ∈ {exclusions}")
else:
    print("  Penyebut = x^2-4 = (x+2)(x-2) = 0 saat x=2 atau x=-2")

# ─── 2. Simplifikasi ──────────────────────────────────────────
print("\n[2] Simplifikasi Pecahan Aljabar")

if HAS_SYMPY:
    x = sp.Symbol('x')
    expressions = [
        ((x**2-1),  (x-1),        "(x^2-1)/(x-1)"),
        ((x**2-4),  (x+2),        "(x^2-4)/(x+2)"),
        ((6*x**2 - x - 2), (3*x-2), "(6x^2-x-2)/(3x-2)"),
        ((x**3-x),  (x**2-1),     "(x^3-x)/(x^2-1)"),
    ]
    print(f"  {'Ekspresi':>30} | {'Simplified':>20}")
    print("  " + "-"*55)
    for num, den, label in expressions:
        expr = num / den
        simplified = sp.simplify(expr)
        factored = sp.factor(expr)
        print(f"  {label:>30} | {str(factored):>20}")
else:
    print("  (x^2-1)/(x-1) = (x+1)(x-1)/(x-1) = x+1  (untuk x≠1)")
    print("  (x^2-4)/(x+2) = (x+2)(x-2)/(x+2) = x-2  (untuk x≠-2)")

# ─── 3. Operasi Aritmetika ────────────────────────────────────
print("\n[3] Operasi Aritmetika Pecahan Aljabar")

if HAS_SYMPY:
    x = sp.Symbol('x')
    
    # Penjumlahan
    f1 = sp.Rational(1)*x / (x**2 - 1)   # x/(x^2-1)
    f2 = sp.Rational(1) / (x + 1)          # 1/(x+1)
    print(f"  x/(x^2-1) + 1/(x+1)")
    print(f"    = {sp.simplify(f1 + f2)}")
    
    # Pengurangan
    g1 = (2*x + 1) / (x**2 - x - 6)  # (2x+1)/((x-3)(x+2))
    g2 = 1 / (x - 3)
    print(f"\n  (2x+1)/(x^2-x-6) - 1/(x-3)")
    print(f"    = {sp.simplify(g1 - g2)}")
    
    # Perkalian
    h1 = (x**2 - 4) / (x + 3)
    h2 = (x + 3) / (x + 2)
    print(f"\n  (x^2-4)/(x+3) × (x+3)/(x+2)")
    print(f"    = {sp.simplify(h1 * h2)}")
    
    # Pembagian
    k1 = (x**2 - 9) / (x**2 + x)
    k2 = (x + 3) / x
    print(f"\n  (x^2-9)/(x^2+x) ÷ (x+3)/x")
    print(f"    = {sp.simplify(k1 / k2)}")

# ─── 4. Persamaan Rasional ────────────────────────────────────
print("\n[4] Menyelesaikan Persamaan Rasional")

if HAS_SYMPY:
    x = sp.Symbol('x')
    equations = [
        (1/x + 1/(x+1), sp.Rational(1,2), "1/x + 1/(x+1) = 1/2"),
        ((x+2)/(x-1), 3/(x-1) + 1, "(x+2)/(x-1) = 3/(x-1) + 1"),
        (2/(x-3), (x-1)/(x+3), "2/(x-3) = (x-1)/(x+3)"),
    ]
    for lhs, rhs, label in equations:
        print(f"\n  Selesaikan: {label}")
        try:
            eq = sp.Eq(lhs, rhs)
            sols = sp.solve(eq, x)
            # Cek solusi extraneous
            valid = []
            for s in sols:
                # Cek apakah membuat penyebut = 0
                denom_ok = True
                for expr in [lhs, rhs]:
                    try:
                        # Coba evaluasi
                        val = float(expr.subs(x, s).evalf())
                        if not sp.isfinite(val):
                            denom_ok = False
                    except:
                        denom_ok = False
                if denom_ok:
                    valid.append(s)
                else:
                    print(f"    x = {s} -> EXTRANEOUS (buat penyebut = 0)!")
            print(f"    Solusi valid: x = {valid}")
        except Exception as e:
            print(f"    Error: {e}")

# ─── 5. Dekomposisi Parsial ───────────────────────────────────
print("\n[5] Dekomposisi Parsial (Partial Fraction Decomposition)")

if HAS_SYMPY:
    x = sp.Symbol('x')
    fractions = [
        (5*x + 1) / ((x+1)*(x-2)),
        (x**2 + 1) / (x*(x-1)*(x+2)),
        3 / ((x+1)*(x**2+1)),
        (2*x + 3) / (x**2*(x-1)),
    ]
    for frac in fractions:
        decomp = sp.apart(frac, x)
        print(f"  {str(frac):>40}  =  {decomp}")
    
# ─── 6. Asymptotes ────────────────────────────────────────────
print("\n[6] Asymptotes Fungsi Rasional")

if HAS_SYMPY:
    x = sp.Symbol('x')
    functions = [
        ((2*x+3), (x-1),      "f(x) = (2x+3)/(x-1)"),
        ((x**2+1), (x**2-4),  "g(x) = (x^2+1)/(x^2-4)"),
        ((x**3), (x**2+1),    "h(x) = x^3/(x^2+1)"),
    ]
    for num, den, label in functions:
        f = num/den
        vert = sp.solve(den, x)
        horiz_limit_pos = sp.limit(f, x, sp.oo)
        horiz_limit_neg = sp.limit(f, x, -sp.oo)
        print(f"\n  {label}")
        print(f"    Vertical asymptote  : x = {vert}")
        print(f"    Limit x→+∞          : {horiz_limit_pos}")
        print(f"    Limit x→-∞          : {horiz_limit_neg}")

print("\n[Selesai] Lanjut ke exercises.py")
