"""
Exercises: Rational Expressions  |  Phase 1 — Topic 1.16
"""
print("LATIHAN 1.16 — PECAHAN ALJABAR")
print("=" * 50)

try:
    import sympy as sp
    x = sp.Symbol('x')

    # Ex 1: Simplify
    print("\n[Ex 1] Sederhanakan ekspresi rasional:")
    exprs = [
        ((x**2 - 9), (x-3),    "x^2-9 / x-3"),
        ((2*x**2-5*x-3), (x-3),"2x^2-5x-3 / x-3"),
        ((x**3-8), (x-2),      "x^3-8 / x-2"),
    ]
    for num, den, label in exprs:
        result = sp.simplify(num/den)
        print(f"  ({label}) = {result}")

    # Ex 2: Add/Subtract
    print("\n[Ex 2] Hitung:")
    print(f"  1/(x-1) + 2/(x+1) = {sp.simplify(1/(x-1) + 2/(x+1))}")
    print(f"  3/(x^2-4) - 1/(x+2) = {sp.simplify(3/(x**2-4) - 1/(x+2))}")

    # Ex 3: Solve rational equations
    print("\n[Ex 3] Selesaikan:")
    equations = [
        (sp.Eq(1/(x-2), 3/(x+2)),  "1/(x-2) = 3/(x+2)"),
        (sp.Eq((x+1)/(x-1) - 2/(x+1), 2), "(x+1)/(x-1) - 2/(x+1) = 2"),
    ]
    for eq, label in equations:
        sols = sp.solve(eq, x)
        print(f"  {label}")
        print(f"    Solusi: x = {sols}")

    # Ex 4: Partial fractions
    print("\n[Ex 4] Dekomposisi Parsial:")
    for frac, label in [
        ((3*x+5)/((x+1)*(x+2)),   "(3x+5)/((x+1)(x+2))"),
        ((x**2)/((x-1)*(x+1)**2), "x^2/((x-1)(x+1)^2)"),
    ]:
        print(f"  {label} = {sp.apart(frac, x)}")

except ImportError:
    print("  [Manual] sympy diperlukan: pip install sympy")
    print("  (x^2-9)/(x-3) = (x+3)(x-3)/(x-3) = x+3  (x≠3)")
    print("  1/(x-1)+2/(x+1) = (x+1+2(x-1))/((x-1)(x+1)) = (3x-1)/(x^2-1)")

print("\n[Selesai]")
