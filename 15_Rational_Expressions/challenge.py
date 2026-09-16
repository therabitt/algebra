"""
Challenge: Rational Expressions  |  Phase 1 — Topic 1.16
"""
print("CHALLENGE 1.16 — PECAHAN ALJABAR")

try:
    import sympy as sp
    x = sp.Symbol('x')

    # Challenge 1: Build partial fraction integrator
    print("\n[Ch1] Integrasi melalui Dekomposisi Parsial")
    print("  ∫ (2x+3)/((x+1)(x-2)) dx")
    integrand = (2*x+3)/((x+1)*(x-2))
    decomposed = sp.apart(integrand, x)
    integral = sp.integrate(decomposed, x)
    print(f"  Dekomposisi : {decomposed}")
    print(f"  Integral    : {integral} + C")
    print(f"  Verifikasi  : d/dx[hasil] = {sp.simplify(sp.diff(integral, x))}")

    # Challenge 2: Continued fractions as rational expressions
    print("\n[Ch2] Continued Fraction sebagai Ekspresi Rasional")
    print("  1 + 1/(1 + 1/(1 + 1/x))")
    expr = 1 + 1/(1 + 1/(1 + 1/x))
    simplified = sp.simplify(expr)
    print(f"  = {simplified}")

    # Challenge 3: Rational function interpolation
    print("\n[Ch3] Interpolasi Rasional — Padé Approximant")
    print("  Aproksimasi e^x dengan ekspresi rasional [1,1] Padé:")
    print("  e^x ≈ (1 + x/2) / (1 - x/2)  (lebih akurat dari Taylor derajat 1!)")
    import math
    print(f"  {'x':>6} | {'e^x':>12} | {'Padé [1,1]':>12} | {'Taylor x+1':>12}")
    for xv in [-1, -0.5, 0, 0.5, 1, 2]:
        exact = math.e**xv
        pade = (1 + xv/2)/(1 - xv/2) if abs(1-xv/2) > 1e-10 else float('nan')
        taylor = 1 + xv
        print(f"  {xv:>6.2f} | {exact:>12.6f} | {pade:>12.6f} | {taylor:>12.6f}")

except ImportError:
    print("  sympy diperlukan: pip install sympy")

print("\n[Selesai Challenge 1.16]")
