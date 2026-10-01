"""
Exercises: Factorization  |  Phase 1 — Topic 1.10
"""
print("LATIHAN 1.10 — FAKTORISASI")
print("=" * 50)

try:
    import sympy as sp
    x = sp.Symbol("x")
    problems = [
        ("x^2 - 16",           x**2-16,       "(x+4)(x-4)"),
        ("x^2 + 8x + 16",      x**2+8*x+16,   "(x+4)^2"),
        ("2x^2 + 7x + 3",      2*x**2+7*x+3,  "(2x+1)(x+3)"),
        ("x^3 - 27",           x**3-27,        "(x-3)(x^2+3x+9)"),
        ("x^2 - 5x + 6",       x**2-5*x+6,    "(x-2)(x-3)"),
        ("6x^2 - 11x + 4",     6*x**2-11*x+4, "(2x-1)(3x-4)"),
        ("x^4 - 81",           x**4-81,        "(x^2+9)(x+3)(x-3)"),
        ("4x^2 - 12x + 9",     4*x**2-12*x+9, "(2x-3)^2"),
    ]
    print(f"  {'Ekspresi':>25} | {'Faktorisasi':>25} | {'Benar?':>8}")
    print("-" * 70)
    for label, expr, expected in problems:
        result = sp.factor(expr)
        verify = sp.expand(result) == sp.expand(expr)
        print(f"  {label:>25} | {str(result):>25} | {str(verify):>8}")
except ImportError:
    print("[Manual solutions]")
    print("  x^2-16 = (x+4)(x-4)")
    print("  x^2+8x+16 = (x+4)^2")
    print("  x^3-27 = (x-3)(x^2+3x+9)")
    print("  (verify by expansion)")

print("\n[Selesai]")
