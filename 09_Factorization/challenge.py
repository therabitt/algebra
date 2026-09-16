"""
Challenge: Factorization  |  Phase 1 — Topic 1.10
"""
print("CHALLENGE 1.10 — FAKTORISASI")

# Faktorisasi atas berbagai field
try:
    import sympy as sp
    x = sp.Symbol("x")
    
    print("\n[Ch1] Faktorisasi atas berbagai bilangan:")
    expr = x**4 + 4
    print(f"  {expr}:")
    print(f"    Atas Q: tidak bisa difaktorkan lebih lanjut? {sp.factor(expr)}")
    # Sophie Germain identity: a^4+4b^4 = (a^2+2b^2+2ab)(a^2+2b^2-2ab)
    # x^4+4 = (x^2+2+2x)(x^2+2-2x)
    print(f"    Sophie Germain: (x^2+2x+2)(x^2-2x+2)")
    f1 = sp.factor(x**2+2*x+2); f2 = sp.factor(x**2-2*x+2)
    print(f"    Verifikasi: {sp.expand((x**2+2*x+2)*(x**2-2*x+2))}")
    
    print("\n[Ch2] GCF Polinomial:")
    from sympy import gcd, Poly
    p1 = Poly(x**3 - x, x)
    p2 = Poly(x**2 - 1, x)
    print(f"  gcd(x^3-x, x^2-1) = {gcd(p1,p2).as_expr()}")
    
    print("\n[Ch3] Akar kompleks menggunakan faktorisasi:")
    expr2 = x**4 + 1
    roots = sp.solve(expr2, x)
    print(f"  Akar x^4+1=0: {roots}")
    print(f"  Semua akar kompleks? {all(not sp.im(r)==0 for r in roots)}")

except ImportError:
    print("sympy diperlukan untuk challenge ini: pip install sympy")

print("\n[Selesai Challenge 1.10]")
